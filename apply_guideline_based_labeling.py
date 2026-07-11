"""
Apply Guideline-Based Labeling to candidate MEDIUM invoices.

This script does not train models, split data, or compute evaluation metrics. It
uses only the published operational rule IDs R1-R12 and the repaired
decision-time dataset.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
REPAIR_DIR = ROOT / "experiment_design_repair"

CANDIDATE_INPUT = REPAIR_DIR / "candidate_medium_expert_review.csv"
CLEANED_DATASET = REPAIR_DIR / "cleaned_decision_time_dataset.csv"

GUIDELINE_WORKBOOK = REPAIR_DIR / "candidate_medium_guideline_review.xlsx"
GUIDELINE_CSV = REPAIR_DIR / "candidate_medium_guideline_review.csv"
LABELING_TABLE = REPAIR_DIR / "guideline_based_labeling_table.csv"
FINAL_DATASET_CSV = REPAIR_DIR / "finalized_guideline_labeled_dataset.csv"
FINAL_DATASET_XLSX = REPAIR_DIR / "finalized_guideline_labeled_dataset.xlsx"
CONSISTENCY_REPORT_MD = REPAIR_DIR / "guideline_labeling_consistency_report.md"
CONSISTENCY_REPORT_CSV = REPAIR_DIR / "guideline_labeling_consistency_summary.csv"
RULE_FREQUENCY_CSV = REPAIR_DIR / "guideline_rule_frequency.csv"
LOW_CONFIDENCE_CSV = REPAIR_DIR / "guideline_low_confidence_invoices.csv"
RULE_CONFLICTS_CSV = REPAIR_DIR / "guideline_rule_conflicts.csv"
METHODOLOGICAL_NOTE_MD = REPAIR_DIR / "methodological_note_guideline_based_labeling.md"


MONTHLY_RULES = {"END_MONTH", "MONTHLY_DATE", "MULTIPLE_MONTHLY_DATE"}
NEXT_MONTH_RULES = {"NEXT_MONTH_DATE", "NEXT_MONTH_WORKDAY", "NEXT_MONTH_FIRST_WEEK"}


def clean_text(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def to_number(value: object) -> float:
    return pd.to_numeric(value, errors="coerce")


def is_limited_schedule(row: pd.Series) -> bool:
    if clean_text(row.get("limited_receive_schedule_flag")):
        return clean_text(row.get("limited_receive_schedule_flag")).lower() == "yes"
    return clean_text(row.get("receive_schedule")).lower() != "everyday"


def evaluate_rule_conditions(row: pd.Series) -> dict[str, bool]:
    cutoff_rule = clean_text(row.get("cutoff_rule"))
    days = to_number(row.get("days_to_cutoff_decision_time"))
    gap = to_number(row.get("next_receive_day_gap_decision_time"))
    month_end = clean_text(row.get("receive_month_end_flag")).lower() == "yes"
    limited = is_limited_schedule(row)
    schedule_status = clean_text(row.get("receive_date_schedule_status"))

    has_days = not pd.isna(days)
    has_gap = not pd.isna(gap)

    return {
        "R1": schedule_status == "MISSED_RECEIVE_DAY",
        "R2": cutoff_rule != "NO_CUTOFF" and has_days and days < 0,
        "R3": cutoff_rule != "NO_CUTOFF" and has_days and days == 0,
        "R4": cutoff_rule in MONTHLY_RULES and has_days and 0 < days <= 2,
        "R5": cutoff_rule in NEXT_MONTH_RULES and has_days and 0 < days <= 2,
        "R6": month_end and has_days and days <= 4,
        "R7": limited and has_gap and gap <= 1,
        "R8": cutoff_rule != "NO_CUTOFF" and has_days and 2 < days <= 10,
        "R9": limited and has_gap and gap > 1,
        "R10": cutoff_rule == "NO_CUTOFF" and (not limited or (has_gap and gap > 1)),
        "R11": cutoff_rule != "NO_CUTOFF" and has_days and days > 10,
        "R12": True,
    }


def rule_description(rule_id: str) -> str:
    return {
        "R1": "jadwal penerimaan dokumen telah terlewat",
        "R2": "batas cutoff telah lewat",
        "R3": "tanggal observasi bertepatan dengan cutoff",
        "R4": "cutoff bulanan atau akhir bulan berada dalam 1-2 hari",
        "R5": "cutoff awal bulan berikutnya berada dalam 1-2 hari",
        "R6": "periode akhir bulan dan cutoff berada dalam batas <= 4 hari",
        "R7": "jadwal penerimaan terbatas dan kesempatan penerimaan berikutnya <= 1 hari",
        "R8": "cutoff berada pada rentang pemantauan 3-10 hari dan tidak memenuhi aturan HIGH",
        "R9": "jadwal penerimaan terbatas tetapi masih terdapat kesempatan operasional sebelum mendesak",
        "R10": "tidak ada cutoff dan tidak terdapat risiko jadwal penerimaan",
        "R11": "cutoff masih lebih dari 10 hari",
        "R12": "aturan penutup karena tidak ada kondisi lain yang terpenuhi",
    }[rule_id]


def assign_guideline_label(row: pd.Series) -> dict[str, object]:
    conditions = evaluate_rule_conditions(row)
    high_rules = [rule for rule in ["R1", "R2", "R3", "R4", "R5", "R6", "R7"] if conditions[rule]]
    medium_rules = [rule for rule in ["R8", "R9"] if conditions[rule]]
    normal_rules = [rule for rule in ["R10", "R11"] if conditions[rule]]

    if high_rules:
        suggested_label = "HIGH"
        applied_rules = high_rules
    elif medium_rules:
        suggested_label = "MEDIUM"
        applied_rules = medium_rules
    elif normal_rules:
        suggested_label = "NORMAL"
        applied_rules = normal_rules
    else:
        suggested_label = "NORMAL"
        applied_rules = ["R12"]

    missing_critical = []
    if pd.isna(to_number(row.get("days_to_cutoff_decision_time"))) and clean_text(row.get("cutoff_rule")) != "NO_CUTOFF":
        missing_critical.append("days_to_cutoff_decision_time")
    if is_limited_schedule(row) and pd.isna(to_number(row.get("next_receive_day_gap_decision_time"))):
        missing_critical.append("next_receive_day_gap_decision_time")

    competing_rules: list[str] = []
    if high_rules and medium_rules:
        competing_rules = high_rules + medium_rules
    elif high_rules and normal_rules:
        competing_rules = high_rules + normal_rules
    elif medium_rules and normal_rules:
        competing_rules = medium_rules + normal_rules

    if missing_critical:
        confidence = "Low"
    elif competing_rules:
        confidence = "Medium"
    elif applied_rules == ["R12"]:
        confidence = "Low"
    elif "R9" in applied_rules:
        confidence = "Medium"
    else:
        confidence = "High"

    reason_parts = [f"{rule}: {rule_description(rule)}" for rule in applied_rules]
    if competing_rules:
        reason_parts.append(
            "priority resolution applied because multiple rule conditions were detected: "
            + ", ".join(competing_rules)
        )
    if missing_critical:
        reason_parts.append("low confidence because required decision-time field is missing: " + ", ".join(missing_critical))

    return {
        "suggested_label": suggested_label,
        "applied_rules": "; ".join(applied_rules),
        "operational_reason": ". ".join(reason_parts),
        "confidence": confidence,
        "all_matching_rules": "; ".join(
            [rule for rule in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11"] if conditions[rule]]
        ),
        "potential_conflict": "Yes" if competing_rules else "No",
        "conflict_detail": "; ".join(competing_rules),
    }


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


def build_guideline_table(candidates: pd.DataFrame, cleaned: pd.DataFrame) -> pd.DataFrame:
    candidate_ids = set(candidates["invoice_no"].astype(str))
    candidate_rows = cleaned[cleaned["invoice_no"].astype(str).isin(candidate_ids)].copy()
    results = candidate_rows.apply(assign_guideline_label, axis=1, result_type="expand")
    candidate_rows = pd.concat([candidate_rows, results], axis=1)

    table = pd.DataFrame(
        {
            "Invoice Number": candidate_rows["invoice_no"],
            "Current Label": candidate_rows["expert_label"],
            "Suggested Label": candidate_rows["suggested_label"],
            "Applied Rule(s)": candidate_rows["applied_rules"],
            "Operational Reason": candidate_rows["operational_reason"],
            "Confidence": candidate_rows["confidence"],
            "All Matching Rule Conditions": candidate_rows["all_matching_rules"],
            "Potential Rule Conflict": candidate_rows["potential_conflict"],
            "Conflict Detail": candidate_rows["conflict_detail"],
        }
    )
    return table.sort_values(["Suggested Label", "Invoice Number"]).reset_index(drop=True)


def write_guideline_workbook(guideline_table: pd.DataFrame, candidates: pd.DataFrame) -> None:
    candidate_view = candidates.rename(
        columns={
            "current_expert_label": "current_label",
            "current_expert_reason": "current_reason",
            "expert_review_label": "guideline_based_label",
            "expert_review_note": "guideline_based_note",
        }
    ).copy()
    candidate_view["guideline_based_label"] = ""
    candidate_view["guideline_based_note"] = ""

    merged = candidate_view.merge(
        guideline_table[
            [
                "Invoice Number",
                "Suggested Label",
                "Applied Rule(s)",
                "Operational Reason",
                "Confidence",
                "Potential Rule Conflict",
                "Conflict Detail",
            ]
        ],
        left_on="invoice_no",
        right_on="Invoice Number",
        how="left",
    ).drop(columns=["Invoice Number"])
    merged["guideline_based_label"] = merged["Suggested Label"]
    merged["guideline_based_note"] = merged["Operational Reason"]

    removed_features = pd.read_csv(REPAIR_DIR / "removed_or_replaced_features.csv")
    remaining_features = pd.read_csv(REPAIR_DIR / "remaining_feature_set.csv")
    duplicate_handling = pd.read_csv(REPAIR_DIR / "duplicate_handling_report.csv")

    with pd.ExcelWriter(GUIDELINE_WORKBOOK) as writer:
        merged.to_excel(writer, sheet_name="Guideline-Based Labeling", index=False)
        guideline_table.to_excel(writer, sheet_name="Applied Rules R1-R12", index=False)
        remaining_features.to_excel(writer, sheet_name="Remaining Features", index=False)
        removed_features.to_excel(writer, sheet_name="Removed Features", index=False)
        duplicate_handling.to_excel(writer, sheet_name="Duplicate Handling", index=False)

    merged.to_csv(GUIDELINE_CSV, index=False)


def build_final_dataset(cleaned: pd.DataFrame, guideline_table: pd.DataFrame) -> pd.DataFrame:
    final_df = cleaned.copy()
    final_df = final_df.rename(columns={"expert_label": "initial_label", "expert_reason": "initial_reason"})
    final_df["final_label"] = final_df["initial_label"]
    final_df["final_label_source"] = "Existing labeled dataset"
    final_df["final_applied_rules"] = ""
    final_df["final_operational_reason"] = ""
    final_df["final_label_confidence"] = ""
    final_df["label_changed_by_guideline"] = "No"

    lookup = guideline_table.set_index("Invoice Number").to_dict(orient="index")
    for idx, row in final_df.iterrows():
        invoice_no = row["invoice_no"]
        if invoice_no not in lookup:
            continue
        item = lookup[invoice_no]
        final_df.at[idx, "final_label"] = item["Suggested Label"]
        final_df.at[idx, "final_label_source"] = "Guideline-Based Labeling"
        final_df.at[idx, "final_applied_rules"] = item["Applied Rule(s)"]
        final_df.at[idx, "final_operational_reason"] = item["Operational Reason"]
        final_df.at[idx, "final_label_confidence"] = item["Confidence"]
        final_df.at[idx, "label_changed_by_guideline"] = "Yes" if item["Suggested Label"] != row["initial_label"] else "No"

    return final_df


def write_reports(guideline_table: pd.DataFrame, final_df: pd.DataFrame) -> None:
    reviewed = len(guideline_table)
    changed = guideline_table[guideline_table["Current Label"] != guideline_table["Suggested Label"]].copy()
    changed_to_high = int(((guideline_table["Suggested Label"] == "HIGH") & (guideline_table["Current Label"] != "HIGH")).sum())
    changed_to_medium = int(((guideline_table["Suggested Label"] == "MEDIUM") & (guideline_table["Current Label"] != "MEDIUM")).sum())
    remaining_normal = int(((guideline_table["Current Label"] == "NORMAL") & (guideline_table["Suggested Label"] == "NORMAL")).sum())
    remaining_high = int(((guideline_table["Current Label"] == "HIGH") & (guideline_table["Suggested Label"] == "HIGH")).sum())

    rule_counter: Counter[str] = Counter()
    for rules in guideline_table["Applied Rule(s)"]:
        for rule in str(rules).split(";"):
            rule = rule.strip()
            if rule:
                rule_counter[rule] += 1
    rule_frequency = pd.DataFrame(
        [{"Rule ID": rule, "Frequency": count} for rule, count in sorted(rule_counter.items())]
    )
    rule_frequency.to_csv(RULE_FREQUENCY_CSV, index=False)

    low_confidence = guideline_table[guideline_table["Confidence"] == "Low"].copy()
    low_confidence.to_csv(LOW_CONFIDENCE_CSV, index=False)

    conflicts = guideline_table[guideline_table["Potential Rule Conflict"] == "Yes"].copy()
    conflicts.to_csv(RULE_CONFLICTS_CSV, index=False)

    summary = pd.DataFrame(
        [
            ["Number of invoices reviewed", reviewed],
            ["Number changed to HIGH", changed_to_high],
            ["Number changed to MEDIUM", changed_to_medium],
            ["Number remaining NORMAL", remaining_normal],
            ["Number remaining HIGH", remaining_high],
            ["Low-confidence invoices", len(low_confidence)],
            ["Potential rule conflicts", len(conflicts)],
            ["Final dataset rows", len(final_df)],
            ["Final HIGH labels", int((final_df["final_label"] == "HIGH").sum())],
            ["Final MEDIUM labels", int((final_df["final_label"] == "MEDIUM").sum())],
            ["Final NORMAL labels", int((final_df["final_label"] == "NORMAL").sum())],
        ],
        columns=["Item", "Value"],
    )
    summary.to_csv(CONSISTENCY_REPORT_CSV, index=False)

    report_lines = [
        "# Guideline-Based Labeling Consistency Report",
        "",
        "## Summary",
        "",
        md_table(summary),
        "",
        "## Rule Frequency",
        "",
        md_table(rule_frequency),
        "",
        "## Invoices with Low Confidence",
        "",
        md_table(
            low_confidence[
                [
                    "Invoice Number",
                    "Current Label",
                    "Suggested Label",
                    "Applied Rule(s)",
                    "Operational Reason",
                    "Confidence",
                ]
            ]
        ),
        "",
        "## Potential Conflicts Between Rules",
        "",
        "A conflict is recorded when rule conditions from different priority levels are detected and the published priority order resolves the final label.",
        "",
        md_table(
            conflicts[
                [
                    "Invoice Number",
                    "Current Label",
                    "Suggested Label",
                    "Applied Rule(s)",
                    "All Matching Rule Conditions",
                    "Conflict Detail",
                ]
            ]
        ),
        "",
    ]
    CONSISTENCY_REPORT_MD.write_text("\n".join(report_lines), encoding="utf-8")

    note_lines = [
        "# Methodological Note: Guideline-Based Labeling",
        "",
        "The additional candidate labels in this artifact were not manually assigned or independently validated by a human reviewer.",
        "",
        "They were generated through Guideline-Based Labeling using the Operational Labeling Guideline developed during the Knowledge Acquisition and Knowledge Formalization stages described in Chapter III. The procedure applies the published rule base R1-R12 to the repaired decision-time features. Each suggested label is accompanied by the applied rule ID, operational reason, and confidence level.",
        "",
        "This means the finalized dataset should be interpreted as a knowledge-guided experimental dataset. The labels are consistent with the operational decision guideline, but they should not be described as the result of a separate manual validation process.",
        "",
        "For the final experiment, the target column should be `final_label`. Rows generated through Guideline-Based Labeling can be identified using `final_label_source = Guideline-Based Labeling`.",
        "",
    ]
    METHODOLOGICAL_NOTE_MD.write_text("\n".join(note_lines), encoding="utf-8")


def main() -> None:
    candidates = pd.read_csv(CANDIDATE_INPUT)
    cleaned = pd.read_csv(CLEANED_DATASET)

    guideline_table = build_guideline_table(candidates, cleaned)
    guideline_table.to_csv(LABELING_TABLE, index=False)
    write_guideline_workbook(guideline_table, candidates)

    final_df = build_final_dataset(cleaned, guideline_table)
    final_df.to_csv(FINAL_DATASET_CSV, index=False)
    with pd.ExcelWriter(FINAL_DATASET_XLSX) as writer:
        final_df.to_excel(writer, sheet_name="Finalized Dataset", index=False)
        guideline_table.to_excel(writer, sheet_name="Guideline Labels", index=False)

    write_reports(guideline_table, final_df)

    print(f"Invoices reviewed: {len(guideline_table)}")
    print(f"Finalized dataset rows: {len(final_df)}")
    print(f"Final label counts: {final_df['final_label'].value_counts().to_dict()}")
    print(f"Artifacts written under: {REPAIR_DIR}")


if __name__ == "__main__":
    main()
