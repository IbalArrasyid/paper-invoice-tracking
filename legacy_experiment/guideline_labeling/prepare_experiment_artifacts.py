"""
Prepare experimental artifacts for the invoice priority thesis.

The script does not modify the source datasets or thesis chapters. It creates a
derived experiment package under experiment_artifacts/ containing validation
reports, predictions, metrics, figures, and error analysis tables.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree


ROOT = Path(__file__).resolve().parent
ARTIFACT_DIR = ROOT / "experiment_artifacts"

LABELED_XLSX = ROOT / "expert_labeling_sheet.xlsx"
LABELED_CSV = ROOT / "expert_labeling_sheet.csv"
RAW_XLSX = ROOT / "LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx"
LABELED_SHEET = "Data Labeling"

CLASS_LABELS = ["HIGH", "MEDIUM", "NORMAL"]
ALLOWED_CUTOFF_RULES = {
    "END_MONTH",
    "MONTHLY_DATE",
    "MULTIPLE_MONTHLY_DATE",
    "NEXT_MONTH_DATE",
    "NEXT_MONTH_WORKDAY",
    "NEXT_MONTH_FIRST_WEEK",
    "NO_CUTOFF",
}
ALLOWED_EXPERT_LABELS = set(CLASS_LABELS)
ALLOWED_MISSED_VALUES = {"No (On Schedule)", "Yes (Missed Schedule)", "Yes"}
ALLOWED_MONTH_END_VALUES = {"Yes", "No"}

REQUIRED_FEATURES = {
    "customer": ["customer_name_masking", "customer_name"],
    "receive_date": ["receive_date"],
    "cutoff_rule": ["cutoff_rule"],
    "cutoff_value": ["cutoff_value"],
    "receive_schedule": ["receive_schedule", "customer_receive_schedule"],
    "receive_day_code": ["receive_day_code"],
    "days_to_cutoff": ["days_to_cutoff"],
    "next_receive_day_gap": ["next_receive_day_gap"],
    "missed_receive_schedule": ["missed_receive_schedule"],
    "month_end_flag": ["month_end_flag"],
    "expert_label": ["expert_label"],
}

DT_FEATURES = [
    "customer_name_masking",
    "receive_date_feature",
    "cutoff_rule",
    "cutoff_value_feature",
    "receive_schedule",
    "receive_day_code_feature",
    "days_to_cutoff",
    "next_receive_day_gap_experiment",
    "missed_receive_schedule_experiment",
    "month_end_flag_experiment",
]


@dataclass
class ValidationIssue:
    severity: str
    dataset: str
    sheet: str
    column: str
    issue: str
    affected_rows: str
    recommendation: str


def ensure_dirs() -> None:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    (ARTIFACT_DIR / "figures").mkdir(exist_ok=True)
    (ARTIFACT_DIR / "tables").mkdir(exist_ok=True)
    (ARTIFACT_DIR / "models").mkdir(exist_ok=True)
    (ARTIFACT_DIR / "reports").mkdir(exist_ok=True)


def normalize_blank(value: object) -> object:
    if pd.isna(value):
        return np.nan
    if isinstance(value, str) and value.strip() == "":
        return np.nan
    return value


def clean_frame_blanks(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    for col in cleaned.columns:
        if cleaned[col].dtype == object:
            cleaned[col] = cleaned[col].map(normalize_blank)
    return cleaned


def meaningful_rows(df: pd.DataFrame) -> pd.DataFrame:
    if "invoice_no" in df.columns:
        return df[df["invoice_no"].notna()].copy()
    return df.dropna(how="all").copy()


def parse_day_codes(value: object) -> list[int]:
    if pd.isna(value):
        return []
    codes: list[int] = []
    for token in re.split(r"[,;/|]+", str(value)):
        token = token.strip()
        if not token:
            continue
        try:
            code = int(float(token))
        except ValueError:
            continue
        if 1 <= code <= 7:
            codes.append(code)
    return sorted(set(codes))


def next_receive_gap(date_value: object, receive_day_code: object) -> float:
    if pd.isna(date_value):
        return np.nan
    codes = parse_day_codes(receive_day_code)
    if not codes:
        return np.nan
    weekday_code = pd.Timestamp(date_value).weekday() + 1
    for gap in range(0, 8):
        candidate_code = ((weekday_code - 1 + gap) % 7) + 1
        if candidate_code in codes:
            return float(gap)
    return np.nan


def canonical_missed(value: object) -> str:
    text = "" if pd.isna(value) else str(value).strip()
    if text.lower().startswith("yes"):
        return "Yes (Missed Schedule)"
    return "No (On Schedule)"


def is_everyday(value: object) -> bool:
    if pd.isna(value):
        return False
    return str(value).strip().lower() == "everyday"


def rule_based_prediction(row: pd.Series) -> tuple[str, str, str]:
    cutoff_rule = str(row["cutoff_rule"]).strip()
    days = pd.to_numeric(row["days_to_cutoff"], errors="coerce")
    if pd.isna(days):
        days = 999
    receive_schedule = row["receive_schedule"]
    next_gap = pd.to_numeric(row["next_receive_day_gap_experiment"], errors="coerce")
    missed = str(row["missed_receive_schedule_experiment"]).strip()
    month_end = str(row["month_end_flag_experiment"]).strip()

    if missed.startswith("Yes"):
        return (
            "HIGH",
            "R1",
            "missed_receive_schedule = Yes; jadwal penerimaan pelanggan telah terlewat.",
        )

    if cutoff_rule != "NO_CUTOFF" and days < 0:
        return (
            "HIGH",
            "R2",
            "cutoff_rule != NO_CUTOFF dan days_to_cutoff < 0; batas cutoff telah lewat.",
        )

    if cutoff_rule != "NO_CUTOFF" and days == 0:
        return (
            "HIGH",
            "R3",
            "cutoff_rule != NO_CUTOFF dan days_to_cutoff = 0; hari observasi bertepatan dengan cutoff.",
        )

    if cutoff_rule in {"END_MONTH", "MONTHLY_DATE", "MULTIPLE_MONTHLY_DATE"} and 0 < days <= 2:
        return (
            "HIGH",
            "R4",
            "cutoff bulanan atau akhir bulan berada dalam 1-2 hari.",
        )

    if cutoff_rule in {"NEXT_MONTH_DATE", "NEXT_MONTH_WORKDAY", "NEXT_MONTH_FIRST_WEEK"} and 0 < days <= 2:
        return (
            "HIGH",
            "R5",
            "cutoff awal bulan berikutnya berada dalam 1-2 hari.",
        )

    if month_end == "Yes" and days <= 4:
        return (
            "HIGH",
            "R6",
            "month_end_flag = Yes dan days_to_cutoff <= 4; periode akhir bulan mendekati cutoff.",
        )

    if not is_everyday(receive_schedule) and not pd.isna(next_gap) and next_gap <= 1:
        return (
            "HIGH",
            "R7",
            "receive_schedule terbatas dan next_receive_day_gap <= 1.",
        )

    if cutoff_rule != "NO_CUTOFF" and 2 < days <= 10:
        return (
            "MEDIUM",
            "R8",
            "cutoff masih dalam rentang pemantauan 3-10 hari dan tidak memenuhi R1-R7.",
        )

    if not is_everyday(receive_schedule) and not pd.isna(next_gap) and next_gap > 1:
        return (
            "MEDIUM",
            "R9",
            "receive_schedule terbatas dan next_receive_day_gap > 1 tanpa kondisi HIGH.",
        )

    no_schedule_risk = is_everyday(receive_schedule) or (not pd.isna(next_gap) and next_gap > 1)
    if cutoff_rule == "NO_CUTOFF" and not missed.startswith("Yes") and no_schedule_risk:
        return (
            "NORMAL",
            "R10",
            "NO_CUTOFF, jadwal tidak terlewat, dan tidak terdapat risiko jadwal penerimaan.",
        )

    if cutoff_rule != "NO_CUTOFF" and days > 10:
        return (
            "NORMAL",
            "R11",
            "cutoff masih lebih dari 10 hari dan tidak memenuhi R1-R9.",
        )

    return (
        "NORMAL",
        "R12",
        "aturan penutup; tidak ada kondisi R1-R11 yang terpenuhi.",
    )


def profile_datasets() -> tuple[pd.DataFrame, list[ValidationIssue]]:
    inventory_rows: list[dict[str, object]] = []
    issues: list[ValidationIssue] = []

    for path in [LABELED_CSV, LABELED_XLSX, RAW_XLSX]:
        if not path.exists():
            issues.append(
                ValidationIssue(
                    "BLOCKER",
                    path.name,
                    "",
                    "",
                    "Dataset file is missing.",
                    "all",
                    "Provide the dataset file before running the experiment.",
                )
            )
            continue

        if path.suffix.lower() == ".csv":
            df = clean_frame_blanks(pd.read_csv(path))
            non_empty_rows = len(meaningful_rows(df))
            all_empty_cols = [c for c in df.columns if df[c].isna().all()]
            inventory_rows.append(
                {
                    "dataset": path.name,
                    "sheet": "",
                    "rows": len(df),
                    "columns": len(df.columns),
                    "non_empty_rows": non_empty_rows,
                    "column_names": "; ".join(map(str, df.columns)),
                    "all_empty_columns": "; ".join(map(str, all_empty_cols)),
                }
            )
            if "invoice_no" in df.columns and non_empty_rows < len(df):
                issues.append(
                    ValidationIssue(
                        "WARNING",
                        path.name,
                        "",
                        "invoice_no",
                        "CSV contains trailing blank rows.",
                        str(len(df) - non_empty_rows),
                        "Use the non-empty invoice rows or the XLSX Data Labeling sheet as the canonical labeled dataset.",
                    )
                )
            unnamed_cols = [c for c in df.columns if str(c).startswith("Unnamed")]
            if unnamed_cols:
                issues.append(
                    ValidationIssue(
                        "WARNING",
                        path.name,
                        "",
                        "; ".join(unnamed_cols),
                        "CSV contains unnamed extra columns.",
                        str(len(unnamed_cols)),
                        "Ignore unnamed columns during modeling.",
                    )
                )
        else:
            xl = pd.ExcelFile(path)
            for sheet in xl.sheet_names:
                df = clean_frame_blanks(pd.read_excel(path, sheet_name=sheet))
                non_empty_rows = len(meaningful_rows(df))
                all_empty_cols = [c for c in df.columns if df[c].isna().all()]
                inventory_rows.append(
                    {
                        "dataset": path.name,
                        "sheet": sheet,
                        "rows": len(df),
                        "columns": len(df.columns),
                        "non_empty_rows": non_empty_rows,
                        "column_names": "; ".join(map(str, df.columns)),
                        "all_empty_columns": "; ".join(map(str, all_empty_cols)),
                    }
                )
                if len(df.columns) == 0 or non_empty_rows == 0:
                    issues.append(
                        ValidationIssue(
                            "INFO",
                            path.name,
                            sheet,
                            "",
                            "Sheet is empty or contains no meaningful rows.",
                            str(len(df)),
                            "Exclude this sheet from the experiment dataset.",
                        )
                    )
                if all_empty_cols:
                    issues.append(
                        ValidationIssue(
                            "WARNING",
                            path.name,
                            sheet,
                            "; ".join(map(str, all_empty_cols)),
                            "Sheet contains all-empty columns.",
                            str(len(all_empty_cols)),
                            "Exclude empty columns unless they are intentionally derived later.",
                        )
                    )
                unnamed_cols = [c for c in df.columns if str(c).startswith("Unnamed")]
                if unnamed_cols:
                    issues.append(
                        ValidationIssue(
                            "INFO",
                            path.name,
                            sheet,
                            "; ".join(map(str, unnamed_cols)),
                            "Sheet contains unnamed/helper columns.",
                            str(len(unnamed_cols)),
                            "Inspect manually before using this sheet as a modeling dataset.",
                        )
                    )

    return pd.DataFrame(inventory_rows), issues


def validate_labeled_dataset(df: pd.DataFrame) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    dataset = LABELED_XLSX.name
    sheet = LABELED_SHEET

    missing = df.isna().sum().sort_values(ascending=False)
    missing.to_frame("missing_count").assign(
        missing_percent=lambda x: (x["missing_count"] / len(df) * 100).round(2)
    ).to_csv(ARTIFACT_DIR / "tables" / "labeled_dataset_missing_values.csv")

    all_empty_cols = [col for col in df.columns if df[col].isna().all()]
    for col in all_empty_cols:
        severity = "WARNING"
        recommendation = "Exclude from modeling unless a validated derivation is available."
        if col in {"next_receive_day_gap", "month_end_flag"}:
            recommendation = "Derive in the experiment copy using the definitions in the Guidelines sheet."
        issues.append(
            ValidationIssue(
                severity,
                dataset,
                sheet,
                col,
                "Required or helper column is completely empty in the source labeled dataset.",
                str(len(df)),
                recommendation,
            )
        )

    duplicate_all_mask = df.duplicated(keep=False)
    if duplicate_all_mask.any():
        affected = "; ".join(df.loc[duplicate_all_mask, "invoice_no"].astype(str).tolist())
        issues.append(
            ValidationIssue(
                "WARNING",
                dataset,
                sheet,
                "all columns",
                "Exact duplicated rows detected.",
                affected,
                "Review whether repeated invoices represent true repeat observations or accidental duplication.",
            )
        )

    duplicate_invoice_mask = df["invoice_no"].duplicated(keep=False)
    if duplicate_invoice_mask.any():
        affected = "; ".join(df.loc[duplicate_invoice_mask, "invoice_no"].astype(str).tolist())
        issues.append(
            ValidationIssue(
                "WARNING",
                dataset,
                sheet,
                "invoice_no",
                "Duplicate invoice numbers detected.",
                affected,
                "Confirm whether duplicate invoice numbers are legitimate repeated observations.",
            )
        )

    invalid_labels = sorted(set(df["expert_label"].dropna().astype(str)) - ALLOWED_EXPERT_LABELS)
    if invalid_labels:
        issues.append(
            ValidationIssue(
                "BLOCKER",
                dataset,
                sheet,
                "expert_label",
                f"Invalid expert labels: {', '.join(invalid_labels)}.",
                "unknown",
                "Restrict expert_label to HIGH, MEDIUM, or NORMAL.",
            )
        )

    absent_labels = [label for label in CLASS_LABELS if label not in set(df["expert_label"].dropna().astype(str))]
    if absent_labels:
        issues.append(
            ValidationIssue(
                "WARNING",
                dataset,
                sheet,
                "expert_label",
                f"Ground truth has no examples for class(es): {', '.join(absent_labels)}.",
                str(len(absent_labels)),
                "Report this as an experimental limitation; Decision Tree cannot learn a class absent from training data.",
            )
        )

    invalid_cutoff = sorted(set(df["cutoff_rule"].dropna().astype(str)) - ALLOWED_CUTOFF_RULES)
    if invalid_cutoff:
        issues.append(
            ValidationIssue(
                "BLOCKER",
                dataset,
                sheet,
                "cutoff_rule",
                f"Invalid cutoff_rule values: {', '.join(invalid_cutoff)}.",
                "unknown",
                "Map each invalid cutoff_rule to the formal rule categories before modeling.",
            )
        )

    code_problem_rows: list[str] = []
    for _, row in df.iterrows():
        codes = parse_day_codes(row.get("receive_day_code"))
        if pd.isna(row.get("receive_day_code")) or len(codes) == 0:
            code_problem_rows.append(str(row["invoice_no"]))
            continue
        raw_tokens = [t.strip() for t in re.split(r"[,;/|]+", str(row.get("receive_day_code"))) if t.strip()]
        if len(raw_tokens) != len(codes):
            code_problem_rows.append(str(row["invoice_no"]))
    if code_problem_rows:
        issues.append(
            ValidationIssue(
                "WARNING",
                dataset,
                sheet,
                "receive_day_code",
                "Missing or unparsable receive_day_code values detected.",
                "; ".join(code_problem_rows),
                "Derive from customer schedule or payment schedule before relying on schedule-based rules.",
            )
        )

    monthly_rules = {"MONTHLY_DATE", "MULTIPLE_MONTHLY_DATE", "NEXT_MONTH_DATE", "NEXT_MONTH_WORKDAY", "NEXT_MONTH_FIRST_WEEK"}
    missing_cutoff_value = df[df["cutoff_rule"].isin(monthly_rules) & df["cutoff_value"].isna()]
    if not missing_cutoff_value.empty:
        issues.append(
            ValidationIssue(
                "WARNING",
                dataset,
                sheet,
                "cutoff_value",
                "cutoff_value is missing for date-based cutoff rules.",
                "; ".join(missing_cutoff_value["invoice_no"].astype(str).tolist()),
                "Review source cutoff descriptions; current Rule-Based rules use days_to_cutoff, but cutoff_value is still required for traceability.",
            )
        )

    non_numeric_days = pd.to_numeric(df["days_to_cutoff"], errors="coerce").isna()
    if non_numeric_days.any():
        issues.append(
            ValidationIssue(
                "BLOCKER",
                dataset,
                sheet,
                "days_to_cutoff",
                "Non-numeric days_to_cutoff values detected.",
                "; ".join(df.loc[non_numeric_days, "invoice_no"].astype(str).tolist()),
                "Recalculate days_to_cutoff before model evaluation.",
            )
        )

    return issues


def build_experiment_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, list[ValidationIssue]]:
    issues: list[ValidationIssue] = []
    exp = df.copy()

    exp["receive_date"] = pd.to_datetime(exp["receive_date"], errors="coerce")
    exp["sent_date"] = pd.to_datetime(exp["sent_date"], errors="coerce")
    exp["days_to_cutoff"] = pd.to_numeric(exp["days_to_cutoff"], errors="coerce").fillna(999).astype(int)
    exp["cutoff_value_feature"] = pd.to_numeric(exp["cutoff_value"], errors="coerce").fillna(-1).astype(int)
    exp["receive_date_feature"] = exp["receive_date"].dt.strftime("%Y-%m-%d").fillna("MISSING")
    exp["receive_day_code_feature"] = exp["receive_day_code"].fillna("MISSING").astype(str)
    exp["customer_name_masking"] = exp["customer_name_masking"].fillna("MISSING").astype(str)
    exp["cutoff_rule"] = exp["cutoff_rule"].fillna("MISSING").astype(str).str.strip()
    exp["receive_schedule"] = exp["receive_schedule"].fillna("MISSING").astype(str).str.strip()
    exp["expert_label"] = exp["expert_label"].fillna("MISSING").astype(str).str.strip().str.upper()

    date_for_schedule = exp["sent_date"].where(exp["sent_date"].notna(), exp["receive_date"])
    exp["next_receive_day_gap_derived"] = [
        next_receive_gap(date_value, code)
        for date_value, code in zip(date_for_schedule, exp["receive_day_code"], strict=False)
    ]
    exp["next_receive_day_gap_experiment"] = pd.to_numeric(
        exp["next_receive_day_gap"], errors="coerce"
    ).where(
        pd.to_numeric(exp["next_receive_day_gap"], errors="coerce").notna(),
        exp["next_receive_day_gap_derived"],
    )

    exp["missed_receive_schedule_derived"] = pd.Series(pd.NA, index=exp.index, dtype="object")
    exp.loc[
        exp["next_receive_day_gap_derived"].notna() & (exp["next_receive_day_gap_derived"] > 0),
        "missed_receive_schedule_derived",
    ] = "Yes (Missed Schedule)"
    exp.loc[
        exp["next_receive_day_gap_derived"].notna() & (exp["next_receive_day_gap_derived"] == 0),
        "missed_receive_schedule_derived",
    ] = "No (On Schedule)"
    exp["missed_receive_schedule_experiment"] = exp["missed_receive_schedule_derived"].where(
        exp["missed_receive_schedule_derived"].notna(),
        exp["missed_receive_schedule"].map(canonical_missed),
    )

    exp["month_end_flag_derived"] = np.where(date_for_schedule.dt.day >= 25, "Yes", "No")
    exp["month_end_flag_experiment"] = exp["month_end_flag"].fillna(exp["month_end_flag_derived"])
    exp["month_end_flag_experiment"] = exp["month_end_flag_experiment"].map(
        lambda value: "Yes" if str(value).strip().lower() == "yes" else "No"
    )

    mismatch = exp[
        exp["missed_receive_schedule"].map(canonical_missed)
        != exp["missed_receive_schedule_experiment"].map(canonical_missed)
    ]
    if not mismatch.empty:
        issues.append(
            ValidationIssue(
                "WARNING",
                LABELED_XLSX.name,
                LABELED_SHEET,
                "missed_receive_schedule",
                "Source missed_receive_schedule differs from the derivation based on sent_date and receive_day_code.",
                "; ".join(mismatch["invoice_no"].astype(str).tolist()),
                "Use the derived experiment field for reproducibility and document the disagreement.",
            )
        )

    missing_gap = exp["next_receive_day_gap_experiment"].isna()
    if missing_gap.any():
        issues.append(
            ValidationIssue(
                "WARNING",
                LABELED_XLSX.name,
                LABELED_SHEET,
                "next_receive_day_gap",
                "next_receive_day_gap remains missing after derivation for rows without receive_day_code.",
                "; ".join(exp.loc[missing_gap, "invoice_no"].astype(str).tolist()),
                "Review the customer's payment schedule; rules R7 and R9 cannot use schedule gap for these rows.",
            )
        )

    predictions = exp.apply(rule_based_prediction, axis=1, result_type="expand")
    predictions.columns = ["Prediction_RuleBased", "RuleBased_RuleID", "RuleBased_Reason"]
    exp = pd.concat([exp, predictions], axis=1)

    return exp, issues


def summarize_feature_validation(df: pd.DataFrame, exp: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for feature, candidates in REQUIRED_FEATURES.items():
        found = [col for col in candidates if col in df.columns]
        if found:
            source_col = found[0]
            missing_count = int(df[source_col].isna().sum())
            status = "available"
            derivation = ""
            experiment_col = source_col
            if feature == "customer":
                status = "available_as_alias"
                derivation = "customer is represented by customer_name_masking for privacy; customer_name is retained only for traceability."
                experiment_col = "customer_name_masking"
            elif feature == "next_receive_day_gap" and missing_count == len(df):
                status = "derived_in_experiment_copy"
                derivation = "Derived from sent_date and receive_day_code as days to the next valid receiving day, based on the Guidelines sheet."
                experiment_col = "next_receive_day_gap_experiment"
            elif feature == "month_end_flag" and missing_count == len(df):
                status = "derived_in_experiment_copy"
                derivation = "Derived from sent_date day >= 25, based on the Guidelines sheet."
                experiment_col = "month_end_flag_experiment"
            elif feature == "missed_receive_schedule":
                status = "validated_with_derivation"
                derivation = "Recomputed from sent_date and receive_day_code; disagreements are reported in validation_issues.csv."
                experiment_col = "missed_receive_schedule_experiment"
        else:
            source_col = ""
            missing_count = math.nan
            status = "missing"
            derivation = "Derive from available operational fields before running the experiment."
            experiment_col = ""

        rows.append(
            {
                "required_feature": feature,
                "source_column": source_col,
                "experiment_column": experiment_col,
                "status": status,
                "source_missing_count": missing_count,
                "derivation_or_note": derivation,
            }
        )

    feature_df = pd.DataFrame(rows)
    feature_df.to_csv(ARTIFACT_DIR / "tables" / "feature_validation_table.csv", index=False)
    return feature_df


def build_decision_tree(exp: pd.DataFrame) -> tuple[pd.DataFrame, Pipeline, pd.DataFrame, pd.DataFrame]:
    model_df = exp[exp["expert_label"].isin(CLASS_LABELS)].copy()
    x = model_df[DT_FEATURES]
    y = model_df["expert_label"]

    x_train, x_test, y_train, y_test, train_idx, test_idx = train_test_split(
        x,
        y,
        model_df.index,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    categorical_features = [
        "customer_name_masking",
        "receive_date_feature",
        "cutoff_rule",
        "receive_schedule",
        "receive_day_code_feature",
        "missed_receive_schedule_experiment",
        "month_end_flag_experiment",
    ]
    numeric_features = [
        "cutoff_value_feature",
        "days_to_cutoff",
        "next_receive_day_gap_experiment",
    ]

    try:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse=False)

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", encoder, categorical_features),
            ("num", "passthrough", numeric_features),
        ],
        remainder="drop",
    )
    classifier = DecisionTreeClassifier(criterion="entropy", random_state=42)
    model = Pipeline(steps=[("preprocess", preprocessor), ("tree", classifier)])
    model.fit(x_train, y_train)

    exp["Experiment_Split"] = "unused"
    exp.loc[train_idx, "Experiment_Split"] = "train"
    exp.loc[test_idx, "Experiment_Split"] = "test"
    exp["Prediction_DT"] = model.predict(exp[DT_FEATURES])

    transformed_feature_names = list(model.named_steps["preprocess"].get_feature_names_out())
    importances = model.named_steps["tree"].feature_importances_
    importance_df = pd.DataFrame(
        {"encoded_feature": transformed_feature_names, "importance": importances}
    ).sort_values("importance", ascending=False)
    importance_df.to_csv(ARTIFACT_DIR / "tables" / "feature_importance_encoded.csv", index=False)

    grouped_rows = []
    for feature in DT_FEATURES:
        encoded_prefixes = [f"cat__{feature}_", f"num__{feature}"]
        total = importance_df[
            importance_df["encoded_feature"].map(lambda name: any(name.startswith(prefix) for prefix in encoded_prefixes))
        ]["importance"].sum()
        grouped_rows.append({"feature": feature, "importance": total})
    grouped_importance_df = pd.DataFrame(grouped_rows).sort_values("importance", ascending=False)
    grouped_importance_df.to_csv(ARTIFACT_DIR / "tables" / "feature_importance_grouped.csv", index=False)

    split_df = pd.DataFrame(
        {
            "invoice_no": exp.loc[list(train_idx) + list(test_idx), "invoice_no"].values,
            "split": ["train"] * len(train_idx) + ["test"] * len(test_idx),
        }
    )
    split_df.to_csv(ARTIFACT_DIR / "tables" / "train_test_split.csv", index=False)

    return exp, model, importance_df, grouped_importance_df


def metrics_for_scope(exp: pd.DataFrame, prediction_col: str, scope_name: str, mask: pd.Series) -> dict[str, object]:
    scoped = exp[mask & exp["expert_label"].isin(CLASS_LABELS)].copy()
    y_true = scoped["expert_label"]
    y_pred = scoped[prediction_col]
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=CLASS_LABELS,
        average="weighted",
        zero_division=0,
    )
    macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=CLASS_LABELS,
        average="macro",
        zero_division=0,
    )
    return {
        "scope": scope_name,
        "model": prediction_col.replace("Prediction_", ""),
        "n": len(scoped),
        "accuracy": accuracy_score(y_true, y_pred),
        "weighted_precision": precision,
        "weighted_recall": recall,
        "weighted_f1": f1,
        "macro_precision": macro_precision,
        "macro_recall": macro_recall,
        "macro_f1": macro_f1,
    }


def save_evaluation(exp: pd.DataFrame) -> pd.DataFrame:
    metric_rows = []
    scopes = {
        "full_dataset": pd.Series(True, index=exp.index),
        "test_split": exp["Experiment_Split"].eq("test"),
    }
    for scope_name, scope_mask in scopes.items():
        for prediction_col in ["Prediction_RuleBased", "Prediction_DT"]:
            metric_rows.append(metrics_for_scope(exp, prediction_col, scope_name, scope_mask))

            scoped = exp[scope_mask & exp["expert_label"].isin(CLASS_LABELS)]
            cm = confusion_matrix(scoped["expert_label"], scoped[prediction_col], labels=CLASS_LABELS)
            cm_df = pd.DataFrame(
                cm,
                index=[f"Actual_{label}" for label in CLASS_LABELS],
                columns=[f"Predicted_{label}" for label in CLASS_LABELS],
            )
            model_name = prediction_col.replace("Prediction_", "").lower()
            cm_df.to_csv(ARTIFACT_DIR / "tables" / f"confusion_matrix_{model_name}_{scope_name}.csv")

            fig, ax = plt.subplots(figsize=(6.4, 5.2))
            display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=CLASS_LABELS)
            display.plot(ax=ax, values_format="d", colorbar=False, cmap="Blues")
            ax.set_title(f"Confusion Matrix - {prediction_col.replace('Prediction_', '')} ({scope_name})")
            fig.tight_layout()
            fig.savefig(ARTIFACT_DIR / "figures" / f"confusion_matrix_{model_name}_{scope_name}.png", dpi=200)
            plt.close(fig)

            report = classification_report(
                scoped["expert_label"],
                scoped[prediction_col],
                labels=CLASS_LABELS,
                target_names=CLASS_LABELS,
                zero_division=0,
                output_dict=True,
            )
            pd.DataFrame(report).transpose().to_csv(
                ARTIFACT_DIR / "tables" / f"classification_report_{model_name}_{scope_name}.csv"
            )

    metrics_df = pd.DataFrame(metric_rows)
    for col in [
        "accuracy",
        "weighted_precision",
        "weighted_recall",
        "weighted_f1",
        "macro_precision",
        "macro_recall",
        "macro_f1",
    ]:
        metrics_df[col] = metrics_df[col].round(4)
    metrics_df.to_csv(ARTIFACT_DIR / "tables" / "metric_comparison_table.csv", index=False)
    return metrics_df


def save_figures(model: Pipeline, grouped_importance_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8.5, 5.4))
    plot_data = grouped_importance_df.sort_values("importance", ascending=True)
    ax.barh(plot_data["feature"], plot_data["importance"], color="#4C78A8")
    ax.set_xlabel("Importance")
    ax.set_title("Decision Tree Feature Importance")
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "figures" / "feature_importance_grouped.png", dpi=220)
    plt.close(fig)

    tree = model.named_steps["tree"]
    feature_names = list(model.named_steps["preprocess"].get_feature_names_out())
    fig, ax = plt.subplots(figsize=(22, 12))
    plot_tree(
        tree,
        feature_names=feature_names,
        class_names=list(tree.classes_),
        filled=True,
        rounded=True,
        fontsize=7,
        ax=ax,
    )
    fig.tight_layout()
    fig.savefig(ARTIFACT_DIR / "figures" / "decision_tree_visualization.png", dpi=220)
    plt.close(fig)

    tree_text = export_text(tree, feature_names=feature_names, max_depth=6)
    (ARTIFACT_DIR / "models" / "decision_tree_rules.txt").write_text(tree_text, encoding="utf-8")


def explain_difference(row: pd.Series, prediction_col: str) -> str:
    actual = row["expert_label"]
    pred = row[prediction_col]
    if actual == pred:
        return ""

    if prediction_col == "Prediction_RuleBased":
        rule_id = row["RuleBased_RuleID"]
        if pred == "MEDIUM" and actual == "NORMAL":
            return (
                f"Rule-Based memicu {rule_id}, sehingga dokumen dianggap perlu dipantau. "
                "Pakar memberi NORMAL, kemungkinan karena konteks operasional masih dianggap longgar walaupun kondisi cutoff/jadwal masuk rentang pemantauan."
            )
        if pred == "HIGH" and actual == "NORMAL":
            return (
                f"Rule-Based memicu {rule_id}. Perbedaan terjadi karena aturan operasional membaca risiko cutoff/jadwal sebagai mendesak, "
                "sedangkan pakar menilai dokumen belum memerlukan prioritas tinggi."
            )
        if pred == "NORMAL" and actual == "HIGH":
            return (
                f"Rule-Based berhenti pada {rule_id} dan tidak menangkap alasan pakar {row.get('expert_reason', '')}. "
                "Ini menunjukkan pengetahuan pakar pada baris tersebut belum sepenuhnya terwakili oleh kondisi R1-R12."
            )
        return (
            f"Rule-Based memicu {rule_id}, tetapi label pakar adalah {actual}. "
            "Perbedaan perlu ditelusuri melalui cutoff, jadwal penerimaan, dan alasan pakar."
        )

    if pred == "NORMAL" and actual == "HIGH":
        return (
            f"Decision Tree memprediksi NORMAL walaupun pakar memberi HIGH dengan alasan {row.get('expert_reason', '')}. "
            "Kemungkinan pola HIGH kurang kuat dipelajari karena data tidak seimbang dan kelas HIGH lebih sedikit dari NORMAL."
        )
    if pred == "HIGH" and actual == "NORMAL":
        return (
            "Decision Tree memprediksi HIGH pada dokumen aktual NORMAL. "
            "Kemungkinan terdapat kombinasi fitur cutoff/jadwal/customer yang mirip dengan contoh HIGH pada data latih."
        )
    if pred == "MEDIUM":
        return (
            "Decision Tree memprediksi MEDIUM, namun kelas MEDIUM tidak tersedia pada ground truth sehingga prediksi ini perlu diperiksa."
        )
    return "Prediksi Decision Tree berbeda dari label pakar; lihat fitur cutoff, jadwal, dan customer pada baris terkait."


def save_prediction_and_error_tables(exp: pd.DataFrame) -> None:
    columns = [
        "invoice_no",
        "customer_name_masking",
        "receive_date",
        "sent_date",
        "cutoff_rule",
        "cutoff_value",
        "receive_schedule",
        "receive_day_code",
        "days_to_cutoff",
        "next_receive_day_gap_experiment",
        "missed_receive_schedule_experiment",
        "month_end_flag_experiment",
        "expert_label",
        "expert_reason",
        "RuleBased_RuleID",
        "RuleBased_Reason",
        "Prediction_RuleBased",
        "Prediction_DT",
        "Experiment_Split",
    ]
    exp[columns].to_csv(ARTIFACT_DIR / "tables" / "prediction_comparison_table.csv", index=False)
    exp[["invoice_no", "Prediction_RuleBased", "RuleBased_RuleID", "RuleBased_Reason"]].to_csv(
        ARTIFACT_DIR / "tables" / "rule_based_predictions.csv", index=False
    )
    exp[["invoice_no", "Prediction_DT", "Experiment_Split"]].to_csv(
        ARTIFACT_DIR / "tables" / "decision_tree_predictions.csv", index=False
    )

    error_rows = []
    for _, row in exp.iterrows():
        for model_name, prediction_col in [
            ("RuleBased", "Prediction_RuleBased"),
            ("DecisionTree", "Prediction_DT"),
        ]:
            if row["expert_label"] == row[prediction_col]:
                continue
            error_rows.append(
                {
                    "model": model_name,
                    "scope": row["Experiment_Split"],
                    "invoice_no": row["invoice_no"],
                    "customer_name_masking": row["customer_name_masking"],
                    "cutoff_rule": row["cutoff_rule"],
                    "receive_schedule": row["receive_schedule"],
                    "days_to_cutoff": row["days_to_cutoff"],
                    "next_receive_day_gap": row["next_receive_day_gap_experiment"],
                    "missed_receive_schedule": row["missed_receive_schedule_experiment"],
                    "month_end_flag": row["month_end_flag_experiment"],
                    "expert_label": row["expert_label"],
                    "prediction": row[prediction_col],
                    "expert_reason": row["expert_reason"],
                    "triggered_rule": row["RuleBased_RuleID"] if model_name == "RuleBased" else "",
                    "operational_explanation": explain_difference(row, prediction_col),
                }
            )
    error_df = pd.DataFrame(error_rows)
    error_df.to_csv(ARTIFACT_DIR / "tables" / "error_analysis_table.csv", index=False)
    error_df[error_df["scope"].eq("test")].to_csv(
        ARTIFACT_DIR / "tables" / "error_analysis_test_only.csv", index=False
    )

    false_rows = []
    for model_name, prediction_col in [("RuleBased", "Prediction_RuleBased"), ("DecisionTree", "Prediction_DT")]:
        for label in CLASS_LABELS:
            fp = exp[(exp[prediction_col].eq(label)) & (~exp["expert_label"].eq(label))]
            fn = exp[(~exp[prediction_col].eq(label)) & (exp["expert_label"].eq(label))]
            false_rows.append({"model": model_name, "class": label, "error_type": "false_positive", "count": len(fp)})
            false_rows.append({"model": model_name, "class": label, "error_type": "false_negative", "count": len(fn)})
    pd.DataFrame(false_rows).to_csv(ARTIFACT_DIR / "tables" / "false_positive_false_negative_summary.csv", index=False)


def write_reports(
    inventory: pd.DataFrame,
    issues: list[ValidationIssue],
    feature_validation: pd.DataFrame,
    metrics: pd.DataFrame,
) -> None:
    def markdown_table(df: pd.DataFrame) -> str:
        if df.empty:
            return ""
        table_df = df.fillna("").astype(str)
        headers = list(table_df.columns)
        lines = [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join(["---"] * len(headers)) + " |",
        ]
        for _, row in table_df.iterrows():
            values = [str(row[col]).replace("\n", " ").replace("|", "\\|") for col in headers]
            lines.append("| " + " | ".join(values) + " |")
        return "\n".join(lines)

    issues_df = pd.DataFrame([issue.__dict__ for issue in issues])
    issues_df.to_csv(ARTIFACT_DIR / "reports" / "validation_issues.csv", index=False)
    inventory.to_csv(ARTIFACT_DIR / "reports" / "dataset_inventory.csv", index=False)

    blocker_count = int((issues_df["severity"] == "BLOCKER").sum()) if not issues_df.empty else 0
    warning_count = int((issues_df["severity"] == "WARNING").sum()) if not issues_df.empty else 0

    dataset_report = [
        "# Dataset Validation Report",
        "",
        f"Generated from project root: `{ROOT}`",
        "",
        "## Summary",
        "",
        f"- Dataset files inspected: {inventory['dataset'].nunique()}",
        f"- Sheets / sources inspected: {len(inventory)}",
        f"- Blockers: {blocker_count}",
        f"- Warnings: {warning_count}",
        "",
        "The canonical experiment dataset is `expert_labeling_sheet.xlsx` sheet `Data Labeling` because it contains 107 non-empty labeled invoice rows. The CSV export contains the same labeled rows but also trailing blank rows and unnamed columns.",
        "",
        "## Dataset Inventory",
        "",
        markdown_table(inventory[["dataset", "sheet", "rows", "columns", "non_empty_rows", "all_empty_columns"]]),
        "",
        "## Validation Issues",
        "",
        markdown_table(issues_df) if not issues_df.empty else "No validation issues detected.",
        "",
    ]
    (ARTIFACT_DIR / "reports" / "dataset_validation_report.md").write_text(
        "\n".join(dataset_report), encoding="utf-8"
    )

    feature_report = [
        "# Feature Validation Report",
        "",
        "## Required Feature Status",
        "",
        markdown_table(feature_validation),
        "",
        "## Modeling Notes",
        "",
        "- Source datasets were not modified.",
        "- `next_receive_day_gap_experiment` and `month_end_flag_experiment` were created only in the experiment copy because their derivation is defined in the Guidelines sheet.",
        "- `customer` is represented by `customer_name_masking` in the Decision Tree feature matrix.",
        "- `expert_label` contains HIGH and NORMAL only; MEDIUM has no ground-truth examples.",
        "",
    ]
    (ARTIFACT_DIR / "reports" / "feature_validation_report.md").write_text(
        "\n".join(feature_report), encoding="utf-8"
    )

    metric_report = [
        "# Evaluation Metrics",
        "",
        "Metrics are generated for the full dataset and for the 20% stratified test split.",
        "",
        markdown_table(metrics),
        "",
    ]
    (ARTIFACT_DIR / "reports" / "evaluation_metrics_report.md").write_text(
        "\n".join(metric_report), encoding="utf-8"
    )


def main() -> None:
    ensure_dirs()
    inventory, profile_issues = profile_datasets()

    labeled_df = clean_frame_blanks(pd.read_excel(LABELED_XLSX, sheet_name=LABELED_SHEET))
    labeled_df = meaningful_rows(labeled_df).reset_index(drop=True)

    validation_issues = profile_issues + validate_labeled_dataset(labeled_df)
    exp, derivation_issues = build_experiment_dataset(labeled_df)
    validation_issues.extend(derivation_issues)

    blockers = [issue for issue in validation_issues if issue.severity == "BLOCKER"]
    if blockers:
        feature_validation = summarize_feature_validation(labeled_df, exp)
        empty_metrics = pd.DataFrame()
        write_reports(inventory, validation_issues, feature_validation, empty_metrics)
        raise SystemExit(
            "Blocking validation issues detected. See experiment_artifacts/reports/validation_issues.csv"
        )

    feature_validation = summarize_feature_validation(labeled_df, exp)

    exp, model, _, grouped_importance_df = build_decision_tree(exp)
    metrics = save_evaluation(exp)
    save_figures(model, grouped_importance_df)
    save_prediction_and_error_tables(exp)

    exp.to_csv(ARTIFACT_DIR / "experiment_dataset_prepared.csv", index=False)
    write_reports(inventory, validation_issues, feature_validation, metrics)

    print(f"Experiment artifacts generated in: {ARTIFACT_DIR}")
    print(metrics.to_string(index=False))


if __name__ == "__main__":
    main()
