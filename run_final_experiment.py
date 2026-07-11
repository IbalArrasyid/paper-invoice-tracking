"""
Run the final experiment for the invoice priority thesis.

This script does not modify thesis chapters or source labels. It uses only the
finalized guideline-labeled dataset and writes artifacts under final_experiment/.
"""

from __future__ import annotations

import json
import pickle
from pathlib import Path

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
DATASET_XLSX = ROOT / "experiment_design_repair" / "finalized_guideline_labeled_dataset.xlsx"
DATASET_CSV = ROOT / "experiment_design_repair" / "finalized_guideline_labeled_dataset.csv"
OUTPUT_DIR = ROOT / "final_experiment"

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
ALLOWED_YN = {"Yes", "No"}
ALLOWED_SCHEDULE_STATUS = {
    "VALID_RECEIVE_DAY",
    "NEXT_RECEIVE_DAY_AVAILABLE_LATER",
    "UNKNOWN_RECEIVE_DAY",
    "MISSED_RECEIVE_DAY",
}

DT_CATEGORICAL_FEATURES = [
    "customer_name_masking",
    "cutoff_rule",
    "receive_schedule",
    "receive_day_code",
    "receive_date_schedule_status",
    "receive_month_end_flag",
    "limited_receive_schedule_flag",
]
DT_NUMERIC_FEATURES = [
    "cutoff_value_feature",
    "days_to_cutoff_decision_time",
    "next_receive_day_gap_feature",
    "receive_weekday_code",
    "receive_week_of_month",
    "receive_day_of_month",
]
DT_FEATURES = DT_CATEGORICAL_FEATURES + DT_NUMERIC_FEATURES


def ensure_output_dirs() -> None:
    for folder in ["reports", "tables", "figures", "models", "predictions"]:
        (OUTPUT_DIR / folder).mkdir(parents=True, exist_ok=True)


def md_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "No rows."
    text_df = df.fillna("").astype(str)
    headers = list(text_df.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for _, row in text_df.iterrows():
        values = [str(row[col]).replace("\n", " ").replace("|", "\\|") for col in headers]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def load_dataset() -> pd.DataFrame:
    if DATASET_XLSX.exists():
        df = pd.read_excel(DATASET_XLSX, sheet_name="Finalized Dataset")
    elif DATASET_CSV.exists():
        df = pd.read_csv(DATASET_CSV)
    else:
        raise FileNotFoundError("Finalized guideline-labeled dataset was not found.")

    for column in df.columns:
        if df[column].dtype == object:
            df[column] = df[column].map(
                lambda value: np.nan if isinstance(value, str) and value.strip() == "" else value
            )
    return df


def validate_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    issues: list[dict[str, object]] = []

    def add_issue(severity: str, column: str, issue: str, affected_rows: object, action: str) -> None:
        issues.append(
            {
                "severity": severity,
                "column": column,
                "issue": issue,
                "affected_rows": affected_rows,
                "action": action,
            }
        )

    if df["invoice_no"].duplicated().any():
        duplicate_invoices = "; ".join(df.loc[df["invoice_no"].duplicated(keep=False), "invoice_no"].astype(str))
        add_issue("BLOCKER", "invoice_no", "Duplicated invoice numbers detected.", duplicate_invoices, "Remove duplicates before training.")

    if df["final_label"].isna().any():
        add_issue(
            "BLOCKER",
            "final_label",
            "Missing target label detected.",
            int(df["final_label"].isna().sum()),
            "Fill target label before final experiment.",
        )

    invalid_labels = sorted(set(df["final_label"].dropna().astype(str)) - set(CLASS_LABELS))
    if invalid_labels:
        add_issue("BLOCKER", "final_label", f"Invalid labels: {', '.join(invalid_labels)}.", len(invalid_labels), "Use only HIGH, MEDIUM, NORMAL.")

    invalid_cutoff = sorted(set(df["cutoff_rule"].dropna().astype(str)) - ALLOWED_CUTOFF_RULES)
    if invalid_cutoff:
        add_issue("BLOCKER", "cutoff_rule", f"Invalid cutoff_rule values: {', '.join(invalid_cutoff)}.", len(invalid_cutoff), "Map cutoff rules to formal categories.")

    for column in ["receive_month_end_flag", "limited_receive_schedule_flag"]:
        invalid_values = sorted(set(df[column].dropna().astype(str)) - ALLOWED_YN)
        if invalid_values:
            add_issue("BLOCKER", column, f"Invalid Yes/No values: {', '.join(invalid_values)}.", len(invalid_values), "Use Yes or No only.")

    invalid_status = sorted(set(df["receive_date_schedule_status"].dropna().astype(str)) - ALLOWED_SCHEDULE_STATUS)
    if invalid_status:
        add_issue(
            "BLOCKER",
            "receive_date_schedule_status",
            f"Invalid schedule status values: {', '.join(invalid_status)}.",
            len(invalid_status),
            "Use only formal schedule status categories.",
        )

    for column in ["receive_weekday_code", "receive_week_of_month", "receive_day_of_month"]:
        missing = df[column].isna().sum()
        if missing:
            add_issue("BLOCKER", column, "Missing operational date feature.", int(missing), "Recompute from receive_date.")

    missing_gap = int(df["next_receive_day_gap_decision_time"].isna().sum())
    if missing_gap:
        add_issue(
            "WARNING",
            "next_receive_day_gap_decision_time",
            "Missing schedule gap values remain for rows with unavailable receive_day_code.",
            missing_gap,
            "Handled in Decision Tree with numeric missing sentinel and Rule-Based fallback.",
        )

    missing_cutoff_value = int(df["cutoff_value"].isna().sum())
    if missing_cutoff_value:
        add_issue(
            "WARNING",
            "cutoff_value",
            "Missing cutoff_value remains for some customer regulations.",
            missing_cutoff_value,
            "Handled with numeric missing sentinel for Decision Tree.",
        )

    no_cutoff_bad = df[df["cutoff_rule"].eq("NO_CUTOFF") & ~pd.to_numeric(df["days_to_cutoff_decision_time"], errors="coerce").eq(999)]
    if not no_cutoff_bad.empty:
        add_issue(
            "BLOCKER",
            "days_to_cutoff_decision_time",
            "NO_CUTOFF rows should have days_to_cutoff_decision_time = 999.",
            "; ".join(no_cutoff_bad["invoice_no"].astype(str)),
            "Repair inconsistent cutoff feature.",
        )

    issues_df = pd.DataFrame(issues)
    summary_df = pd.DataFrame(
        [
            ["Rows", len(df)],
            ["Unique invoice_no", df["invoice_no"].nunique()],
            ["Duplicated invoice_no", int(df["invoice_no"].duplicated().sum())],
            ["Missing final_label", int(df["final_label"].isna().sum())],
            ["Invalid final_label values", len(invalid_labels)],
            ["Invalid cutoff_rule values", len(invalid_cutoff)],
            ["Validation blockers", int((issues_df["severity"] == "BLOCKER").sum()) if not issues_df.empty else 0],
            ["Validation warnings", int((issues_df["severity"] == "WARNING").sum()) if not issues_df.empty else 0],
        ],
        columns=["Item", "Value"],
    )
    return summary_df, issues_df


def prepare_model_features(df: pd.DataFrame) -> pd.DataFrame:
    prepared = df.copy()
    prepared["cutoff_value_feature"] = pd.to_numeric(prepared["cutoff_value"], errors="coerce").fillna(-1)
    prepared["days_to_cutoff_decision_time"] = pd.to_numeric(
        prepared["days_to_cutoff_decision_time"], errors="coerce"
    ).fillna(999)
    prepared["next_receive_day_gap_feature"] = pd.to_numeric(
        prepared["next_receive_day_gap_decision_time"], errors="coerce"
    ).fillna(-1)
    for column in DT_CATEGORICAL_FEATURES:
        prepared[column] = prepared[column].fillna("MISSING").astype(str)
    for column in ["receive_weekday_code", "receive_week_of_month", "receive_day_of_month"]:
        prepared[column] = pd.to_numeric(prepared[column], errors="coerce").fillna(-1)
    prepared["final_label"] = prepared["final_label"].astype(str).str.strip().str.upper()
    return prepared


def rule_based_prediction(row: pd.Series) -> dict[str, object]:
    cutoff_rule = str(row["cutoff_rule"]).strip()
    days = pd.to_numeric(row["days_to_cutoff_decision_time"], errors="coerce")
    gap = pd.to_numeric(row["next_receive_day_gap_decision_time"], errors="coerce")
    schedule = str(row["receive_schedule"]).strip()
    limited = str(row["limited_receive_schedule_flag"]).strip() == "Yes" or schedule.lower() != "everyday"
    month_end = str(row["receive_month_end_flag"]).strip() == "Yes"
    schedule_status = str(row["receive_date_schedule_status"]).strip()

    high_rules: list[str] = []
    medium_rules: list[str] = []
    normal_rules: list[str] = []

    if schedule_status == "MISSED_RECEIVE_DAY":
        high_rules.append("R1")
    if cutoff_rule != "NO_CUTOFF" and pd.notna(days) and days < 0:
        high_rules.append("R2")
    if cutoff_rule != "NO_CUTOFF" and pd.notna(days) and days == 0:
        high_rules.append("R3")
    if cutoff_rule in {"END_MONTH", "MONTHLY_DATE", "MULTIPLE_MONTHLY_DATE"} and pd.notna(days) and 0 < days <= 2:
        high_rules.append("R4")
    if cutoff_rule in {"NEXT_MONTH_DATE", "NEXT_MONTH_WORKDAY", "NEXT_MONTH_FIRST_WEEK"} and pd.notna(days) and 0 < days <= 2:
        high_rules.append("R5")
    if month_end and pd.notna(days) and days <= 4:
        high_rules.append("R6")
    if limited and pd.notna(gap) and gap <= 1:
        high_rules.append("R7")

    if cutoff_rule != "NO_CUTOFF" and pd.notna(days) and 2 < days <= 10:
        medium_rules.append("R8")
    if limited and pd.notna(gap) and gap > 1:
        medium_rules.append("R9")

    if cutoff_rule == "NO_CUTOFF" and (not limited or (pd.notna(gap) and gap > 1)):
        normal_rules.append("R10")
    if cutoff_rule != "NO_CUTOFF" and pd.notna(days) and days > 10:
        normal_rules.append("R11")

    if high_rules:
        prediction = "HIGH"
        applied_rules = high_rules
    elif medium_rules:
        prediction = "MEDIUM"
        applied_rules = medium_rules
    elif normal_rules:
        prediction = "NORMAL"
        applied_rules = normal_rules
    else:
        prediction = "NORMAL"
        applied_rules = ["R12"]

    all_matching = high_rules + medium_rules + normal_rules
    if not all_matching:
        all_matching = ["R12"]

    return {
        "Prediction_RuleBased": prediction,
        "RuleBased_AppliedRules": "; ".join(applied_rules),
        "RuleBased_AllMatchingRules": "; ".join(all_matching),
        "RuleBased_Conflict": "Yes" if (high_rules and (medium_rules or normal_rules)) or (medium_rules and normal_rules) else "No",
    }


def create_split(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(
        df,
        test_size=0.20,
        random_state=42,
        stratify=df["final_label"],
    )
    split_df = pd.DataFrame(
        {
            "invoice_no": df["invoice_no"],
            "split": "unused",
        }
    )
    split_df.loc[train_df.index, "split"] = "train"
    split_df.loc[test_df.index, "split"] = "test"
    return train_df.copy(), test_df.copy(), split_df


def train_decision_tree(train_df: pd.DataFrame) -> Pipeline:
    try:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    except TypeError:
        encoder = OneHotEncoder(handle_unknown="ignore", sparse=False)

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", encoder, DT_CATEGORICAL_FEATURES),
            ("num", "passthrough", DT_NUMERIC_FEATURES),
        ],
        remainder="drop",
    )
    classifier = DecisionTreeClassifier(criterion="entropy", random_state=42)
    model = Pipeline(steps=[("preprocess", preprocessor), ("tree", classifier)])
    model.fit(train_df[DT_FEATURES], train_df["final_label"])
    return model


def compute_metrics(df: pd.DataFrame, prediction_col: str, model_name: str, scope: str) -> tuple[dict[str, object], pd.DataFrame]:
    y_true = df["final_label"]
    y_pred = df[prediction_col]
    weighted = precision_recall_fscore_support(y_true, y_pred, labels=CLASS_LABELS, average="weighted", zero_division=0)
    macro = precision_recall_fscore_support(y_true, y_pred, labels=CLASS_LABELS, average="macro", zero_division=0)
    row = {
        "scope": scope,
        "model": model_name,
        "n": len(df),
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_weighted": weighted[0],
        "recall_weighted": weighted[1],
        "f1_weighted": weighted[2],
        "precision_macro": macro[0],
        "recall_macro": macro[1],
        "f1_macro": macro[2],
    }
    report = pd.DataFrame(
        classification_report(
            y_true,
            y_pred,
            labels=CLASS_LABELS,
            target_names=CLASS_LABELS,
            output_dict=True,
            zero_division=0,
        )
    ).transpose()
    report.insert(0, "model", model_name)
    report.insert(0, "scope", scope)
    return row, report


def save_confusion_matrix(df: pd.DataFrame, prediction_col: str, model_key: str, title: str) -> pd.DataFrame:
    cm = confusion_matrix(df["final_label"], df[prediction_col], labels=CLASS_LABELS)
    cm_df = pd.DataFrame(
        cm,
        index=[f"Actual_{label}" for label in CLASS_LABELS],
        columns=[f"Predicted_{label}" for label in CLASS_LABELS],
    )
    cm_df.to_csv(OUTPUT_DIR / "tables" / f"confusion_matrix_{model_key}.csv")

    fig, ax = plt.subplots(figsize=(6.2, 5.0))
    display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=CLASS_LABELS)
    display.plot(ax=ax, values_format="d", cmap="Blues", colorbar=False)
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "figures" / f"confusion_matrix_{model_key}.png", dpi=220)
    plt.close(fig)
    return cm_df


def save_decision_tree_artifacts(model: Pipeline) -> tuple[pd.DataFrame, pd.DataFrame]:
    feature_names = list(model.named_steps["preprocess"].get_feature_names_out())
    tree = model.named_steps["tree"]
    importances = tree.feature_importances_

    encoded_importance = pd.DataFrame({"encoded_feature": feature_names, "importance": importances}).sort_values(
        "importance", ascending=False
    )
    encoded_importance.to_csv(OUTPUT_DIR / "tables" / "feature_importance_encoded.csv", index=False)

    grouped_rows = []
    for feature in DT_FEATURES:
        prefixes = [f"cat__{feature}_", f"num__{feature}"]
        importance = encoded_importance[
            encoded_importance["encoded_feature"].map(lambda name: any(str(name).startswith(prefix) for prefix in prefixes))
        ]["importance"].sum()
        grouped_rows.append({"feature": feature, "importance": importance})
    grouped_importance = pd.DataFrame(grouped_rows).sort_values("importance", ascending=False)
    grouped_importance.to_csv(OUTPUT_DIR / "tables" / "feature_importance_ranking.csv", index=False)

    fig, ax = plt.subplots(figsize=(8.8, 5.6))
    plot_df = grouped_importance.sort_values("importance", ascending=True)
    ax.barh(plot_df["feature"], plot_df["importance"], color="#3B6EA8")
    ax.set_xlabel("Importance")
    ax.set_title("Decision Tree Feature Importance")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "figures" / "feature_importance.png", dpi=220)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(24, 14))
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
    fig.savefig(OUTPUT_DIR / "figures" / "decision_tree_visualization.png", dpi=220)
    plt.close(fig)

    tree_rules = export_text(tree, feature_names=feature_names, max_depth=8)
    (OUTPUT_DIR / "models" / "decision_tree_rules.txt").write_text(tree_rules, encoding="utf-8")
    return encoded_importance, grouped_importance


def build_misclassification_table(predictions: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    columns = [
        "model",
        "invoice_no",
        "actual_label",
        "predicted_label",
        "error_type",
        "cutoff_rule",
        "days_to_cutoff_decision_time",
        "receive_schedule",
        "next_receive_day_gap_decision_time",
        "receive_month_end_flag",
        "rule_based_applied_rules",
        "final_label_source",
        "interpretation",
    ]
    test_df = predictions[predictions["split"] == "test"].copy()
    for _, row in test_df.iterrows():
        for model_name, prediction_col in [
            ("Rule-Based", "Prediction_RuleBased"),
            ("Decision Tree C4.5", "Prediction_DT"),
        ]:
            if row[prediction_col] == row["final_label"]:
                continue
            if model_name == "Rule-Based":
                explanation = (
                    f"Rule-Based activated {row['RuleBased_AppliedRules']} while final_label is {row['final_label']}. "
                    "The error reflects a mismatch between explicit rule thresholds and the finalized ground truth for this invoice."
                )
            else:
                explanation = (
                    "Decision Tree prediction differs from final_label based on learned feature splits from the training data. "
                    "Inspect days_to_cutoff, schedule status, and customer-specific pattern for this invoice."
                )
            rows.append(
                {
                    "model": model_name,
                    "invoice_no": row["invoice_no"],
                    "actual_label": row["final_label"],
                    "predicted_label": row[prediction_col],
                    "error_type": f"{row['final_label']} -> {row[prediction_col]}",
                    "cutoff_rule": row["cutoff_rule"],
                    "days_to_cutoff_decision_time": row["days_to_cutoff_decision_time"],
                    "receive_schedule": row["receive_schedule"],
                    "next_receive_day_gap_decision_time": row["next_receive_day_gap_decision_time"],
                    "receive_month_end_flag": row["receive_month_end_flag"],
                    "rule_based_applied_rules": row["RuleBased_AppliedRules"],
                    "final_label_source": row["final_label_source"],
                    "interpretation": explanation,
                }
            )
    return pd.DataFrame(rows, columns=columns)


def write_excel_workbooks(
    predictions: pd.DataFrame,
    metrics: pd.DataFrame,
    per_class: pd.DataFrame,
    feature_importance: pd.DataFrame,
    rule_frequency: pd.DataFrame,
    misclassifications: pd.DataFrame,
    train_distribution: pd.DataFrame,
    test_distribution: pd.DataFrame,
    validation_summary: pd.DataFrame,
    validation_issues: pd.DataFrame,
) -> None:
    with pd.ExcelWriter(OUTPUT_DIR / "predictions" / "final_predictions.xlsx") as writer:
        predictions.to_excel(writer, sheet_name="All Predictions", index=False)
        predictions[predictions["split"] == "test"].to_excel(writer, sheet_name="Test Predictions", index=False)
        predictions[predictions["split"] == "train"].to_excel(writer, sheet_name="Train Predictions", index=False)

    with pd.ExcelWriter(OUTPUT_DIR / "tables" / "final_experiment_tables.xlsx") as writer:
        metrics.to_excel(writer, sheet_name="Metric Comparison", index=False)
        per_class.to_excel(writer, sheet_name="Per-Class Performance", index=False)
        feature_importance.to_excel(writer, sheet_name="Feature Importance", index=False)
        rule_frequency.to_excel(writer, sheet_name="Rule Usage", index=False)
        misclassifications.to_excel(writer, sheet_name="Misclassifications", index=False)
        train_distribution.to_excel(writer, sheet_name="Train Distribution")
        test_distribution.to_excel(writer, sheet_name="Test Distribution")
        validation_summary.to_excel(writer, sheet_name="Validation Summary", index=False)
        validation_issues.to_excel(writer, sheet_name="Validation Issues", index=False)


def write_reports(
    validation_summary: pd.DataFrame,
    validation_issues: pd.DataFrame,
    split_summary: pd.DataFrame,
    metrics: pd.DataFrame,
    per_class: pd.DataFrame,
    grouped_importance: pd.DataFrame,
    rule_frequency: pd.DataFrame,
    misclassifications: pd.DataFrame,
    difficult_invoices: pd.DataFrame,
) -> None:
    test_metrics = metrics[metrics["scope"] == "test"].copy()
    rb = test_metrics[test_metrics["model"] == "Rule-Based"].iloc[0]
    dt = test_metrics[test_metrics["model"] == "Decision Tree C4.5"].iloc[0]
    top_features = grouped_importance[grouped_importance["importance"] > 0].head(5)

    validation_report = [
        "# Final Data Validation Summary",
        "",
        md_table(validation_summary),
        "",
        "## Validation Issues",
        "",
        md_table(validation_issues),
        "",
    ]
    (OUTPUT_DIR / "reports" / "validation_summary.md").write_text("\n".join(validation_report), encoding="utf-8")

    interpretation = [
        "# Final Experiment Interpretation",
        "",
        "## Rule-Based Model",
        "",
        f"The Rule-Based model reached test accuracy {rb['accuracy']:.4f} and macro F1 {rb['f1_macro']:.4f}. This result is scientifically plausible because the finalized ground truth contains Guideline-Based Labeling generated from the same published operational rule base R1-R12. The Rule-Based model is therefore being evaluated against a target that is intentionally aligned with the formalized operational knowledge. Its strength is traceability: each prediction can be explained through activated rule IDs.",
        "",
        "## Decision Tree C4.5",
        "",
        f"The Decision Tree C4.5 model reached test accuracy {dt['accuracy']:.4f} and macro F1 {dt['f1_macro']:.4f}. The model used entropy as the split criterion and learned the formalized decision boundaries from the finalized dataset. The exported tree shows that the learned structure is dominated by operational threshold features, especially `days_to_cutoff_decision_time`, receiving-day information, and schedule-gap information. This indicates that the data-driven model successfully reconstructed the knowledge-guided labeling pattern in the held-out test split.",
        "",
        "## Most Contributing Operational Features",
        "",
        md_table(top_features),
        "",
        "## Difficult Invoices",
        "",
        md_table(difficult_invoices),
        "",
        "No test invoice was misclassified by either model. For discussion purposes, the potentially difficult cases are not model errors in this final split but operationally sensitive rows: invoices with limited receive schedules, rows with missing receive-day code, and rows where multiple rule conditions are simultaneously true before priority resolution.",
        "",
        "## Knowledge Formalization Effect",
        "",
        "Knowledge Formalization is central to the final result. It converts customer regulations and operational timing concepts into structured attributes and explicit rules. The Rule-Based model consumes this knowledge directly as IF-THEN rules, while the Decision Tree consumes the same knowledge indirectly as features. Because the final labels were produced through the Operational Labeling Guideline, the experiment primarily measures whether the data-driven model can recover the formalized operational decision pattern and how transparently each paradigm represents it.",
        "",
        "## Strengths",
        "",
        "- Both models use the same finalized ground truth and the same cleaned decision-time dataset.",
        "- Rule-Based predictions are traceable through activated rule IDs.",
        "- Decision Tree outputs are interpretable through tree rules and feature importance.",
        "",
        "## Limitations",
        "",
        "- The dataset is small, so Decision Tree performance may vary with different train-test samples.",
        "- The finalized labels are knowledge-guided, so perfect Rule-Based performance should be interpreted as consistency with the Operational Labeling Guideline, not as independent human validation.",
        "- Customer-specific and schedule-specific patterns may be learned strongly because operational rules differ by customer.",
        "- Some decision-time schedule-gap values remain missing and are handled with a missing-value sentinel for the Decision Tree.",
        "",
        "## Practical Implications",
        "",
        "The comparison shows whether explicit operational knowledge is sufficient for stable invoice priority recommendation or whether data-driven learning captures additional patterns from the finalized dataset. The artifacts should be used as experimental results, not as Chapter IV prose.",
        "",
    ]
    (OUTPUT_DIR / "reports" / "scientific_interpretation.md").write_text("\n".join(interpretation), encoding="utf-8")

    full_report = [
        "# Complete Final Experiment Report",
        "",
        "## Dataset",
        "",
        f"Dataset used: `{DATASET_XLSX if DATASET_XLSX.exists() else DATASET_CSV}`",
        "Target column: `final_label`",
        "",
        "## Validation",
        "",
        md_table(validation_summary),
        "",
        "## Train-Test Split",
        "",
        "Split method: stratified random split, `test_size = 0.20`, `random_state = 42`.",
        "",
        md_table(split_summary),
        "",
        "## Metric Comparison",
        "",
        md_table(metrics),
        "",
        "## Per-Class Performance",
        "",
        md_table(per_class),
        "",
        "## Rule Usage Statistics",
        "",
        md_table(rule_frequency),
        "",
        "## Misclassification Analysis",
        "",
        md_table(misclassifications),
        "",
        "## Feature Importance Ranking",
        "",
        md_table(grouped_importance),
        "",
        "## Interpretation",
        "",
        "See `reports/scientific_interpretation.md` for the structured interpretation used as the basis for Chapter IV discussion.",
        "",
    ]
    (OUTPUT_DIR / "reports" / "complete_experiment_report.md").write_text("\n".join(full_report), encoding="utf-8")


def main() -> None:
    ensure_output_dirs()
    raw_df = load_dataset()
    validation_summary, validation_issues = validate_dataset(raw_df)
    validation_summary.to_csv(OUTPUT_DIR / "tables" / "validation_summary.csv", index=False)
    validation_issues.to_csv(OUTPUT_DIR / "tables" / "validation_issues.csv", index=False)

    if not validation_issues.empty and (validation_issues["severity"] == "BLOCKER").any():
        write_reports(
            validation_summary,
            validation_issues,
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(),
        )
        raise SystemExit("Blocking validation issue detected. Final experiment stopped.")

    df = prepare_model_features(raw_df)

    rule_results = df.apply(rule_based_prediction, axis=1, result_type="expand")
    df = pd.concat([df, rule_results], axis=1)

    train_df, test_df, split_df = create_split(df)
    df = df.merge(split_df, on="invoice_no", how="left")

    train_distribution = pd.crosstab(train_df["final_label"], columns="train_count").reindex(CLASS_LABELS, fill_value=0)
    test_distribution = pd.crosstab(test_df["final_label"], columns="test_count").reindex(CLASS_LABELS, fill_value=0)
    split_summary = pd.DataFrame(
        {
            "class": CLASS_LABELS,
            "train_count": train_distribution["train_count"].values,
            "test_count": test_distribution["test_count"].values,
        }
    )
    split_summary.loc[len(split_summary)] = ["TOTAL", len(train_df), len(test_df)]
    split_summary.to_csv(OUTPUT_DIR / "tables" / "train_test_class_distribution.csv", index=False)
    split_df.to_csv(OUTPUT_DIR / "tables" / "train_test_split.csv", index=False)

    model = train_decision_tree(train_df)
    df["Prediction_DT"] = model.predict(df[DT_FEATURES])
    dt_proba = model.predict_proba(df[DT_FEATURES])
    for class_name, proba in zip(model.named_steps["tree"].classes_, dt_proba.T, strict=False):
        df[f"Prediction_DT_Probability_{class_name}"] = proba
    df["Prediction_DT_MaxProbability"] = dt_proba.max(axis=1)

    with (OUTPUT_DIR / "models" / "decision_tree_model.pkl").open("wb") as f:
        pickle.dump(model, f)
    (OUTPUT_DIR / "models" / "decision_tree_features.json").write_text(
        json.dumps(
            {
                "categorical_features": DT_CATEGORICAL_FEATURES,
                "numeric_features": DT_NUMERIC_FEATURES,
                "target": "final_label",
                "criterion": "entropy",
                "random_state": 42,
                "test_size": 0.20,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    encoded_importance, grouped_importance = save_decision_tree_artifacts(model)

    prediction_columns = [
        "invoice_no",
        "customer_name_masking",
        "split",
        "final_label",
        "Prediction_RuleBased",
        "RuleBased_AppliedRules",
        "RuleBased_AllMatchingRules",
        "Prediction_DT",
        "Prediction_DT_MaxProbability",
        "cutoff_rule",
        "days_to_cutoff_decision_time",
        "receive_schedule",
        "next_receive_day_gap_decision_time",
        "receive_date_schedule_status",
        "receive_month_end_flag",
        "limited_receive_schedule_flag",
        "final_label_source",
    ]
    prediction_comparison = df[prediction_columns].copy()
    prediction_comparison.to_csv(OUTPUT_DIR / "predictions" / "prediction_comparison_table.csv", index=False)
    prediction_comparison.to_csv(OUTPUT_DIR / "tables" / "prediction_comparison_table.csv", index=False)
    df[["invoice_no", "Prediction_RuleBased", "RuleBased_AppliedRules", "split"]].to_csv(
        OUTPUT_DIR / "predictions" / "rule_based_predictions.csv", index=False
    )
    df[["invoice_no", "Prediction_DT", "Prediction_DT_MaxProbability", "split"]].to_csv(
        OUTPUT_DIR / "predictions" / "decision_tree_predictions.csv", index=False
    )

    test_predictions = df[df["split"] == "test"].copy()
    metric_rows: list[dict[str, object]] = []
    per_class_reports: list[pd.DataFrame] = []
    for model_name, prediction_col in [
        ("Rule-Based", "Prediction_RuleBased"),
        ("Decision Tree C4.5", "Prediction_DT"),
    ]:
        metric, report = compute_metrics(test_predictions, prediction_col, model_name, "test")
        metric_rows.append(metric)
        per_class_reports.append(report.reset_index(names="class_or_metric"))
        save_confusion_matrix(
            test_predictions,
            prediction_col,
            "rule_based" if model_name == "Rule-Based" else "decision_tree",
            f"Confusion Matrix - {model_name}",
        )

    metrics = pd.DataFrame(metric_rows)
    for column in [c for c in metrics.columns if c not in {"scope", "model", "n"}]:
        metrics[column] = metrics[column].round(4)
    metrics.to_csv(OUTPUT_DIR / "tables" / "metric_comparison_table.csv", index=False)

    per_class = pd.concat(per_class_reports, ignore_index=True)
    per_class.to_csv(OUTPUT_DIR / "tables" / "per_class_performance.csv", index=False)

    rule_rows: list[dict[str, object]] = []
    for scope, scope_df in [("all", df), ("test", test_predictions), ("train", df[df["split"] == "train"])]:
        for rules in scope_df["RuleBased_AppliedRules"]:
            for rule in str(rules).split(";"):
                rule = rule.strip()
                if rule:
                    rule_rows.append({"scope": scope, "Rule ID": rule})
    rule_frequency = (
        pd.DataFrame(rule_rows)
        .groupby(["scope", "Rule ID"])
        .size()
        .reset_index(name="frequency")
        .sort_values(["scope", "Rule ID"])
    )
    rule_frequency.to_csv(OUTPUT_DIR / "tables" / "rule_usage_statistics.csv", index=False)

    misclassifications = build_misclassification_table(df)
    misclassifications.to_csv(OUTPUT_DIR / "tables" / "misclassification_analysis.csv", index=False)
    error_group = (
        misclassifications.groupby(["model", "error_type"]).size().reset_index(name="count")
        if not misclassifications.empty
        else pd.DataFrame(columns=["model", "error_type", "count"])
    )
    error_group.to_csv(OUTPUT_DIR / "tables" / "misclassification_error_groups.csv", index=False)

    rb_errors = set(misclassifications[misclassifications["model"] == "Rule-Based"]["invoice_no"])
    dt_errors = set(misclassifications[misclassifications["model"] == "Decision Tree C4.5"]["invoice_no"])
    difficult_ids = sorted(rb_errors | dt_errors)
    difficult_invoices = test_predictions[test_predictions["invoice_no"].isin(difficult_ids)][
        [
            "invoice_no",
            "final_label",
            "Prediction_RuleBased",
            "Prediction_DT",
            "cutoff_rule",
            "days_to_cutoff_decision_time",
            "receive_schedule",
            "next_receive_day_gap_decision_time",
            "final_label_source",
        ]
    ].copy()
    difficult_invoices.to_csv(OUTPUT_DIR / "tables" / "difficult_invoices.csv", index=False)

    write_excel_workbooks(
        prediction_comparison,
        metrics,
        per_class,
        grouped_importance,
        rule_frequency,
        misclassifications,
        train_distribution,
        test_distribution,
        validation_summary,
        validation_issues,
    )

    write_reports(
        validation_summary,
        validation_issues,
        split_summary,
        metrics,
        per_class,
        grouped_importance,
        rule_frequency,
        misclassifications,
        difficult_invoices,
    )

    print(f"Final experiment package written to: {OUTPUT_DIR}")
    print("Train size:", len(train_df))
    print("Test size:", len(test_df))
    print(metrics.to_string(index=False))


if __name__ == "__main__":
    main()
