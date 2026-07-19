"""Run the revised Rule-Based versus Decision Tree experiment.

Source: dataset_invoice.xlsx, sheet "Data Labeling".
The source workbook is read only and is never modified.
"""

from __future__ import annotations

import json
import pickle
import time
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import binomtest
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import (
    GridSearchCV,
    LeaveOneOut,
    StratifiedKFold,
    train_test_split,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

from repair_experimental_design import (
    add_decision_time_features,
    clean_blanks,
    remove_duplicates,
)


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "dataset_invoice.xlsx"
OUTPUT = ROOT / "comparative_experiment"
RANDOM_STATE = 42

SOURCE_LABEL = "expert_label"
TARGET = "admin_ground_truth"
LABEL_MAP = {"HIGH": "Urgent", "NORMAL": "Not Urgent"}
LABELS = ["Not Urgent", "Urgent"]

CATEGORICAL_FEATURES = [
    "cutoff_rule",
    "receive_day_code",
    "receive_schedule",
    "receive_date_schedule_status",
    "receive_month_end_flag",
    "limited_receive_schedule_flag",
]
NUMERIC_FEATURES = [
    "cutoff_value_feature",
    "days_to_cutoff_feature",
    "next_receive_day_gap_feature",
    "receive_weekday_code",
    "receive_week_of_month",
    "receive_day_of_month",
]
MODEL_FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES


def json_default(value: object) -> object:
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def markdown_table(frame: pd.DataFrame) -> str:
    """Render a compact Markdown table without an optional tabulate dependency."""
    columns = [str(column) for column in frame.columns]
    rows = [[str(value) for value in row] for row in frame.itertuples(index=False, name=None)]
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def ensure_output_dirs() -> None:
    for folder in ["data", "tables", "predictions", "models", "reports"]:
        (OUTPUT / folder).mkdir(parents=True, exist_ok=True)


def load_and_prepare_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    raw = pd.read_excel(SOURCE, sheet_name="Data Labeling")
    raw = clean_blanks(raw)
    raw = raw[raw["invoice_no"].notna()].copy()
    raw["_source_excel_row"] = raw.index + 2
    raw["receive_date"] = pd.to_datetime(raw["receive_date"], errors="coerce")
    raw["sent_date"] = pd.to_datetime(raw["sent_date"], errors="coerce")

    source_labels = raw[SOURCE_LABEL].astype(str).str.strip().str.upper()
    invalid_labels = sorted(set(source_labels) - set(LABEL_MAP))
    if invalid_labels:
        raise ValueError(f"Unsupported source labels: {invalid_labels}")
    raw[TARGET] = source_labels.map(LABEL_MAP)

    cleaned, duplicate_report = remove_duplicates(raw)

    cutoff_numeric = pd.to_numeric(cleaned["cutoff_value"], errors="coerce")
    invalid_monthly = cleaned["cutoff_rule"].eq("MONTHLY_DATE") & ~cutoff_numeric.between(1, 31)
    cleaning_issues = cleaned.loc[
        invalid_monthly,
        ["invoice_no", "_source_excel_row", "cutoff_type", "cutoff_rule", "cutoff_value"],
    ].copy()
    if not cleaning_issues.empty:
        cleaning_issues["issue"] = "Invalid or missing monthly cutoff day; parsed from cutoff_type."
        cleaned.loc[invalid_monthly, "cutoff_value"] = np.nan

    prepared, derivation_issues = add_decision_time_features(cleaned)

    prepared["cutoff_value_feature"] = pd.to_numeric(
        prepared["cutoff_value"], errors="coerce"
    ).fillna(-1)
    prepared["days_to_cutoff_feature"] = pd.to_numeric(
        prepared["days_to_cutoff_decision_time"], errors="coerce"
    ).fillna(-999)
    prepared["next_receive_day_gap_feature"] = pd.to_numeric(
        prepared["next_receive_day_gap_decision_time"], errors="coerce"
    ).fillna(-1)

    for column in CATEGORICAL_FEATURES:
        prepared[column] = prepared[column].fillna("MISSING").astype(str)
    for column in ["receive_weekday_code", "receive_week_of_month", "receive_day_of_month"]:
        prepared[column] = pd.to_numeric(prepared[column], errors="coerce").fillna(-1)

    if prepared["invoice_no"].duplicated().any():
        raise ValueError("Duplicate invoice_no remains after cleaning.")
    if prepared[TARGET].isna().any():
        raise ValueError("Missing administrator ground-truth label remains.")
    if set(prepared[TARGET]) != set(LABELS):
        raise ValueError("Both target classes must be present.")

    prepared["observation_id"] = prepared["invoice_no"].astype(str)
    prepared = prepared.reset_index(drop=True)
    return raw, prepared, duplicate_report, pd.concat(
        [cleaning_issues, derivation_issues], ignore_index=True, sort=False
    )


def rule_based_prediction(row: pd.Series) -> tuple[str, str]:
    cutoff_rule = str(row["cutoff_rule"]).strip()
    days = pd.to_numeric(row["days_to_cutoff_decision_time"], errors="coerce")
    gap = pd.to_numeric(row["next_receive_day_gap_decision_time"], errors="coerce")
    limited = str(row["limited_receive_schedule_flag"]).strip() == "Yes"
    month_end = str(row["receive_month_end_flag"]).strip() == "Yes"
    schedule_status = str(row["receive_date_schedule_status"]).strip()

    rules: list[str] = []
    if schedule_status == "MISSED_RECEIVE_DAY":
        rules.append("R1")
    if cutoff_rule != "NO_CUTOFF" and pd.notna(days) and days < 0:
        rules.append("R2")
    if cutoff_rule != "NO_CUTOFF" and pd.notna(days) and days == 0:
        rules.append("R3")
    if cutoff_rule in {"END_MONTH", "MONTHLY_DATE", "MULTIPLE_MONTHLY_DATE"} and pd.notna(days) and 0 < days <= 2:
        rules.append("R4")
    if cutoff_rule in {"NEXT_MONTH_DATE", "NEXT_MONTH_WORKDAY", "NEXT_MONTH_FIRST_WEEK"} and pd.notna(days) and 0 < days <= 2:
        rules.append("R5")
    if month_end and pd.notna(days) and days <= 4:
        rules.append("R6")
    if limited and pd.notna(gap) and gap <= 1:
        rules.append("R7")

    if rules:
        return "Urgent", ";".join(rules)
    return "Not Urgent", "R8"


def build_pipeline(random_state: int) -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL_FEATURES),
            ("num", "passthrough", NUMERIC_FEATURES),
        ],
        remainder="drop",
        verbose_feature_names_out=True,
    )
    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            (
                "tree",
                DecisionTreeClassifier(
                    criterion="entropy",
                    random_state=random_state,
                ),
            ),
        ]
    )


def fit_decision_tree(train_df: pd.DataFrame, random_state: int) -> tuple[Pipeline, dict[str, object], float]:
    min_class_count = int(train_df[TARGET].value_counts().min())
    inner_splits = min(5, min_class_count)
    if inner_splits < 2:
        raise ValueError("Training partition does not contain enough cases for inner validation.")

    search = GridSearchCV(
        estimator=build_pipeline(random_state),
        param_grid={
            "tree__max_depth": [2, 3, 4, None],
            "tree__min_samples_leaf": [1, 2, 4],
        },
        scoring="f1_macro",
        cv=StratifiedKFold(n_splits=inner_splits, shuffle=True, random_state=random_state),
        n_jobs=-1,
        refit=True,
    )
    started = time.perf_counter()
    search.fit(train_df[MODEL_FEATURES], train_df[TARGET])
    elapsed = time.perf_counter() - started
    return search.best_estimator_, search.best_params_, elapsed


def feature_importance_rows(model: Pipeline, experiment: str, fold: int) -> list[dict[str, object]]:
    encoded_names = model.named_steps["preprocess"].get_feature_names_out()
    importances = model.named_steps["tree"].feature_importances_
    grouped = Counter()

    for encoded_name, importance in zip(encoded_names, importances, strict=False):
        source_feature = None
        for feature in CATEGORICAL_FEATURES + NUMERIC_FEATURES:
            if encoded_name == f"num__{feature}" or encoded_name.startswith(f"cat__{feature}_"):
                source_feature = feature
                break
        grouped[source_feature or encoded_name] += float(importance)

    return [
        {
            "experiment": experiment,
            "fold": fold,
            "feature": feature,
            "importance": importance,
        }
        for feature, importance in grouped.items()
    ]


def evaluate_predictions(frame: pd.DataFrame, prediction_column: str) -> dict[str, object]:
    y_true = frame[TARGET]
    y_pred = frame[prediction_column]
    matrix = confusion_matrix(y_true, y_pred, labels=LABELS)
    return {
        "n": len(frame),
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_urgent": precision_score(y_true, y_pred, pos_label="Urgent", zero_division=0),
        "recall_urgent": recall_score(y_true, y_pred, pos_label="Urgent", zero_division=0),
        "f1_urgent": f1_score(y_true, y_pred, pos_label="Urgent", zero_division=0),
        "f1_macro": f1_score(y_true, y_pred, average="macro", zero_division=0),
        "true_negative": int(matrix[0, 0]),
        "false_positive": int(matrix[0, 1]),
        "false_negative": int(matrix[1, 0]),
        "true_positive": int(matrix[1, 1]),
    }


def holdout_splits(data: pd.DataFrame) -> list[tuple[str, int, np.ndarray, np.ndarray]]:
    indices = np.arange(len(data))
    output = []
    for experiment, test_size in [("E1_80_20", 0.20), ("E2_70_30", 0.30)]:
        train_idx, test_idx = train_test_split(
            indices,
            test_size=test_size,
            random_state=RANDOM_STATE,
            stratify=data[TARGET],
        )
        output.append((experiment, 1, train_idx, test_idx))
    return output


def outer_splits(data: pd.DataFrame):
    yield from holdout_splits(data)

    five_fold = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    for fold, (train_idx, test_idx) in enumerate(
        five_fold.split(data[MODEL_FEATURES], data[TARGET]), start=1
    ):
        yield "E3_5_Fold_CV", fold, train_idx, test_idx

    loo = LeaveOneOut()
    for fold, (train_idx, test_idx) in enumerate(loo.split(data), start=1):
        yield "E4_LOOCV", fold, train_idx, test_idx


def run_experiments(data: pd.DataFrame) -> dict[str, pd.DataFrame]:
    prediction_rows: list[dict[str, object]] = []
    complexity_rows: list[dict[str, object]] = []
    importance_rows: list[dict[str, object]] = []

    rule_started = time.perf_counter()
    rule_output = data.apply(rule_based_prediction, axis=1, result_type="expand")
    rule_output.columns = ["prediction_rule_based", "rule_ids"]
    data = pd.concat([data, rule_output], axis=1)
    rule_total_seconds = time.perf_counter() - rule_started

    for experiment, fold, train_idx, test_idx in outer_splits(data):
        train_df = data.iloc[train_idx].copy()
        test_df = data.iloc[test_idx].copy()
        model, best_params, train_seconds = fit_decision_tree(
            train_df,
            RANDOM_STATE + fold,
        )

        prediction_started = time.perf_counter()
        decision_predictions = model.predict(test_df[MODEL_FEATURES])
        probabilities = model.predict_proba(test_df[MODEL_FEATURES])
        prediction_seconds = time.perf_counter() - prediction_started
        urgent_class_index = list(model.named_steps["tree"].classes_).index("Urgent")
        transformed = model.named_steps["preprocess"].transform(test_df[MODEL_FEATURES])
        leaf_ids = model.named_steps["tree"].apply(transformed)

        for position, (_, row) in enumerate(test_df.iterrows()):
            prediction_rows.append(
                {
                    "experiment": experiment,
                    "fold": fold,
                    "invoice_no": row["invoice_no"],
                    "source_excel_row": row["_source_excel_row"],
                    TARGET: row[TARGET],
                    "prediction_rule_based": row["prediction_rule_based"],
                    "rule_ids": row["rule_ids"],
                    "prediction_decision_tree": decision_predictions[position],
                    "decision_tree_urgent_probability": probabilities[position, urgent_class_index],
                    "decision_tree_leaf_id": int(leaf_ids[position]),
                }
            )

        tree = model.named_steps["tree"]
        complexity_rows.append(
            {
                "experiment": experiment,
                "fold": fold,
                "train_n": len(train_df),
                "test_n": len(test_df),
                "best_params": json.dumps(best_params, sort_keys=True),
                "tree_depth": tree.get_depth(),
                "tree_leaves": tree.get_n_leaves(),
                "training_seconds": train_seconds,
                "prediction_seconds": prediction_seconds,
            }
        )
        importance_rows.extend(feature_importance_rows(model, experiment, fold))

    predictions = pd.DataFrame(prediction_rows)
    complexity = pd.DataFrame(complexity_rows)
    importance = pd.DataFrame(importance_rows)

    # Preserve completed validation work before downstream reporting begins.
    predictions.to_csv(OUTPUT / "predictions" / "all_scenario_predictions.csv", index=False)
    complexity.to_csv(OUTPUT / "tables" / "decision_tree_complexity.csv", index=False)
    importance.to_csv(OUTPUT / "tables" / "feature_importance_by_model.csv", index=False)

    metric_rows: list[dict[str, object]] = []
    confusion_rows: list[dict[str, object]] = []
    paired_rows: list[dict[str, object]] = []
    fold_metric_rows: list[dict[str, object]] = []

    for experiment, experiment_df in predictions.groupby("experiment", sort=False):
        for method, column in [
            ("Rule-Based", "prediction_rule_based"),
            ("Decision Tree", "prediction_decision_tree"),
        ]:
            metrics = evaluate_predictions(experiment_df, column)
            metric_rows.append({"experiment": experiment, "method": method, **metrics})
            matrix = confusion_matrix(experiment_df[TARGET], experiment_df[column], labels=LABELS)
            for actual_index, actual in enumerate(LABELS):
                for predicted_index, predicted in enumerate(LABELS):
                    confusion_rows.append(
                        {
                            "experiment": experiment,
                            "method": method,
                            "actual": actual,
                            "predicted": predicted,
                            "count": int(matrix[actual_index, predicted_index]),
                        }
                    )

        rb_correct = experiment_df["prediction_rule_based"].eq(experiment_df[TARGET])
        dt_correct = experiment_df["prediction_decision_tree"].eq(experiment_df[TARGET])
        rb_only = int((rb_correct & ~dt_correct).sum())
        dt_only = int((~rb_correct & dt_correct).sum())
        discordant = rb_only + dt_only
        p_value = float(binomtest(rb_only, discordant, 0.5).pvalue) if discordant else 1.0
        paired_rows.append(
            {
                "experiment": experiment,
                "both_correct": int((rb_correct & dt_correct).sum()),
                "rule_based_only_correct": rb_only,
                "decision_tree_only_correct": dt_only,
                "both_wrong": int((~rb_correct & ~dt_correct).sum()),
                "mcnemar_exact_p_value": p_value,
            }
        )

        if experiment == "E3_5_Fold_CV":
            for fold, fold_df in experiment_df.groupby("fold"):
                for method, column in [
                    ("Rule-Based", "prediction_rule_based"),
                    ("Decision Tree", "prediction_decision_tree"),
                ]:
                    fold_metric_rows.append(
                        {
                            "experiment": experiment,
                            "fold": fold,
                            "method": method,
                            **evaluate_predictions(fold_df, column),
                        }
                    )

    data["prediction_rule_based"] = rule_output["prediction_rule_based"]
    data["rule_ids"] = rule_output["rule_ids"]
    rule_usage = (
        data.assign(rule_id=data["rule_ids"].str.split(";"))
        .explode("rule_id")
        .groupby("rule_id")
        .size()
        .reset_index(name="frequency")
        .sort_values("rule_id")
    )
    rule_usage["total_rule_prediction_seconds"] = rule_total_seconds

    errors = predictions[
        predictions["prediction_rule_based"].ne(predictions[TARGET])
        | predictions["prediction_decision_tree"].ne(predictions[TARGET])
        | predictions["prediction_rule_based"].ne(predictions["prediction_decision_tree"])
    ].copy()
    errors["comparison_group"] = np.select(
        [
            errors["prediction_rule_based"].eq(errors[TARGET])
            & errors["prediction_decision_tree"].ne(errors[TARGET]),
            errors["prediction_rule_based"].ne(errors[TARGET])
            & errors["prediction_decision_tree"].eq(errors[TARGET]),
            errors["prediction_rule_based"].ne(errors[TARGET])
            & errors["prediction_decision_tree"].ne(errors[TARGET]),
        ],
        ["Rule-Based only correct", "Decision Tree only correct", "Both wrong"],
        default="Different predictions",
    )

    return {
        "prepared": data,
        "predictions": predictions,
        "metrics": pd.DataFrame(metric_rows),
        "confusion": pd.DataFrame(confusion_rows),
        "paired": pd.DataFrame(paired_rows),
        "fold_metrics": pd.DataFrame(fold_metric_rows),
        "complexity": complexity,
        "importance": importance,
        "rule_usage": rule_usage,
        "errors": errors,
    }


def train_final_interpretive_tree(data: pd.DataFrame) -> tuple[Pipeline, dict[str, object], pd.DataFrame]:
    model, params, training_seconds = fit_decision_tree(data, RANDOM_STATE)
    encoded_names = list(model.named_steps["preprocess"].get_feature_names_out())
    tree = model.named_steps["tree"]
    rules = export_text(tree, feature_names=encoded_names)
    (OUTPUT / "models" / "final_decision_tree_rules.txt").write_text(rules, encoding="utf-8")
    with (OUTPUT / "models" / "final_decision_tree_model.pkl").open("wb") as handle:
        pickle.dump(model, handle)

    importance = pd.DataFrame(feature_importance_rows(model, "FINAL_FULL_DATA", 0))
    metadata = {
        "source": str(SOURCE),
        "target": TARGET,
        "label_mapping": LABEL_MAP,
        "features": MODEL_FEATURES,
        "criterion": "entropy",
        "best_params": params,
        "tree_depth": tree.get_depth(),
        "tree_leaves": tree.get_n_leaves(),
        "training_seconds": training_seconds,
        "note": "Final full-data tree is interpretive and is not used for reported test metrics.",
    }
    (OUTPUT / "models" / "final_model_metadata.json").write_text(
        json.dumps(metadata, indent=2, default=json_default), encoding="utf-8"
    )
    return model, metadata, importance


def feature_policy_table() -> pd.DataFrame:
    rows = [
        ("invoice_no", "Exclude", "Identifier; used only for traceability and duplicate handling."),
        ("customer_name_masking", "Exclude", "High-cardinality identifier may cause memorization."),
        ("receive_date", "Derive only", "Creates decision-time calendar features."),
        ("sent_date", "Exclude", "Post-decision field and leakage risk."),
        ("Driver", "Exclude", "Operational outcome/assignment, not an urgency condition."),
        ("cutoff_type", "Derive only", "Used to calculate the effective cutoff date."),
        ("cutoff_rule", "Include", "Structured customer cutoff category."),
        ("cutoff_value", "Include derived", "Numeric cutoff input available from customer rules."),
        ("receive_day_code", "Include", "Structured customer receiving-day rule."),
        ("receive_schedule", "Include", "Customer receiving schedule."),
        ("days_to_cutoff", "Replace", "Source value uses sent_date; replaced with decision-time value."),
        ("expert_label", "Target source", "Mapped to administrator ground truth."),
        ("expert_reason", "Exclude", "Post-label explanation and direct leakage risk."),
        ("decision-time derived features", "Include", "Computed from receive_date and customer rules."),
    ]
    return pd.DataFrame(rows, columns=["feature", "policy", "reason"])


def save_outputs(
    raw: pd.DataFrame,
    prepared: pd.DataFrame,
    duplicates: pd.DataFrame,
    data_issues: pd.DataFrame,
    results: dict[str, pd.DataFrame],
    final_metadata: dict[str, object],
    final_importance: pd.DataFrame,
) -> None:
    class_distribution = (
        prepared[TARGET].value_counts().reindex(LABELS, fill_value=0).rename_axis("class").reset_index(name="count")
    )
    class_distribution["percentage"] = class_distribution["count"] / len(prepared)
    dataset_summary = pd.DataFrame(
        [
            ("Source rows", len(raw)),
            ("Cleaned unique invoices", len(prepared)),
            ("Removed duplicate rows", len(raw) - len(prepared)),
            ("Missing target labels", int(prepared[TARGET].isna().sum())),
            ("Urgent", int((prepared[TARGET] == "Urgent").sum())),
            ("Not Urgent", int((prepared[TARGET] == "Not Urgent").sum())),
            ("Feature derivation issues", len(data_issues)),
        ],
        columns=["item", "value"],
    )

    prepared.to_csv(OUTPUT / "data" / "cleaned_analysis_dataset.csv", index=False)
    duplicates.to_csv(OUTPUT / "data" / "duplicate_handling.csv", index=False)
    data_issues.to_csv(OUTPUT / "data" / "data_quality_issues.csv", index=False)
    dataset_summary.to_csv(OUTPUT / "tables" / "dataset_summary.csv", index=False)
    class_distribution.to_csv(OUTPUT / "tables" / "class_distribution.csv", index=False)
    feature_policy_table().to_csv(OUTPUT / "tables" / "feature_policy.csv", index=False)

    results["predictions"].to_csv(OUTPUT / "predictions" / "all_scenario_predictions.csv", index=False)
    results["metrics"].to_csv(OUTPUT / "tables" / "metrics_by_scenario.csv", index=False)
    results["confusion"].to_csv(OUTPUT / "tables" / "confusion_matrices.csv", index=False)
    results["paired"].to_csv(OUTPUT / "tables" / "paired_comparison.csv", index=False)
    results["fold_metrics"].to_csv(OUTPUT / "tables" / "five_fold_metrics.csv", index=False)
    results["complexity"].to_csv(OUTPUT / "tables" / "decision_tree_complexity.csv", index=False)
    results["importance"].to_csv(OUTPUT / "tables" / "feature_importance_by_model.csv", index=False)
    final_importance.to_csv(OUTPUT / "tables" / "final_tree_feature_importance.csv", index=False)
    results["rule_usage"].to_csv(OUTPUT / "tables" / "rule_usage.csv", index=False)
    results["errors"].to_csv(OUTPUT / "tables" / "misclassification_cases.csv", index=False)

    config = {
        "source": str(SOURCE),
        "source_sheet": "Data Labeling",
        "source_label": SOURCE_LABEL,
        "label_mapping": LABEL_MAP,
        "deduplication": "One earliest record retained per invoice_no.",
        "random_state": RANDOM_STATE,
        "experiments": ["E1_80_20", "E2_70_30", "E3_5_Fold_CV", "E4_LOOCV"],
        "decision_tree": {
            "criterion": "entropy",
            "inner_validation": "Stratified 5-fold where class counts permit",
            "parameter_grid": {
                "max_depth": [2, 3, 4, None],
                "min_samples_leaf": [1, 2, 4],
            },
        },
    }
    (OUTPUT / "experiment_config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")

    metrics_rounded = results["metrics"].copy()
    metric_columns = [
        "accuracy", "precision_urgent", "recall_urgent", "f1_urgent", "f1_macro"
    ]
    metrics_rounded[metric_columns] = metrics_rounded[metric_columns].round(4)

    dataset_report = [
        "# Dataset Audit",
        "",
        f"- Source rows: {len(raw)}.",
        f"- Unique invoices after deduplication: {len(prepared)}.",
        f"- Class distribution: {dict(zip(class_distribution['class'], class_distribution['count'], strict=False))}.",
        "- Label normalization: HIGH = Urgent; NORMAL = Not Urgent.",
        "- The source field is expert_label; documentary evidence of administrator provenance remains required.",
        "- expert_reason, sent_date, identifiers, and customer ID are excluded from model features.",
        f"- Data-quality or derivation issues: {len(data_issues)}; see data/data_quality_issues.csv.",
        "",
        "The source workbook was not modified.",
    ]
    (OUTPUT / "reports" / "dataset_audit.md").write_text("\n".join(dataset_report), encoding="utf-8")

    summary_lines = [
        "# Comparative Experiment Summary",
        "",
        "Both methods were evaluated on identical validation invoices in each scenario.",
        "Decision Tree parameters were selected using training data only.",
        "LOOCV metrics were calculated from aggregated out-of-fold predictions.",
        "",
        markdown_table(metrics_rounded),
        "",
        "The final full-data Decision Tree is interpretive only and is not used for test metrics.",
        f"Final tree depth: {final_metadata['tree_depth']}; leaves: {final_metadata['tree_leaves']}.",
    ]
    (OUTPUT / "reports" / "experiment_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    method_note = [
        "# Methodological Note",
        "",
        "The source column expert_label is treated as administrator ground truth following the research direction.",
        "The workbook does not independently document that provenance; the thesis must provide supporting evidence.",
        "HIGH is normalized to Urgent and NORMAL to Not Urgent; no record is relabeled using Rule-Based output.",
        "Rule-Based uses only SOP-derived decision-time conditions.",
        "Decision Tree excludes expert_reason, sent_date, invoice identifiers, customer identifiers, and driver assignment.",
        "The cleaned sample is 99 unique invoices, not 105; all thesis text must use the verified count.",
    ]
    (OUTPUT / "reports" / "methodological_note.md").write_text("\n".join(method_note), encoding="utf-8")


def main() -> None:
    ensure_output_dirs()
    raw, prepared, duplicates, data_issues = load_and_prepare_data()
    results = run_experiments(prepared)
    _, final_metadata, final_importance = train_final_interpretive_tree(prepared)
    save_outputs(
        raw,
        prepared,
        duplicates,
        data_issues,
        results,
        final_metadata,
        final_importance,
    )
    print(f"Experiment complete: {OUTPUT}")
    print(results["metrics"].round(4).to_string(index=False))


if __name__ == "__main__":
    main()
