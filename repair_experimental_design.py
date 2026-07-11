"""
Repair the experimental design before final model evaluation.

This script does not retrain models and does not modify source datasets. It
creates a cleaned, decision-time dataset and review artifacts for expert MEDIUM
label confirmation.
"""

from __future__ import annotations

import calendar
import re
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
SOURCE_FILE = ROOT / "expert_labeling_sheet.xlsx"
SOURCE_SHEET = "Data Labeling"
OUTPUT_DIR = ROOT / "experiment_design_repair"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)


def clean_blanks(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    for col in cleaned.columns:
        if cleaned[col].dtype == object:
            cleaned[col] = cleaned[col].map(
                lambda value: np.nan if isinstance(value, str) and value.strip() == "" else value
            )
    return cleaned


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


def is_workday(day: date) -> bool:
    return day.weekday() < 5


def last_day_of_month(year: int, month: int) -> date:
    return date(year, month, calendar.monthrange(year, month)[1])


def last_workday_of_month(year: int, month: int) -> date:
    day = last_day_of_month(year, month)
    while not is_workday(day):
        day -= timedelta(days=1)
    return day


def add_months(day: date, months: int) -> date:
    month_index = day.month - 1 + months
    year = day.year + month_index // 12
    month = month_index % 12 + 1
    final_day = min(day.day, calendar.monthrange(year, month)[1])
    return date(year, month, final_day)


def safe_date(year: int, month: int, day: int) -> date:
    return date(year, month, min(day, calendar.monthrange(year, month)[1]))


def nth_workday(year: int, month: int, n: int) -> date:
    count = 0
    current = date(year, month, 1)
    while current.month == month:
        if is_workday(current):
            count += 1
            if count == n:
                return current
        current += timedelta(days=1)
    return last_workday_of_month(year, month)


def workday_gap(start: date, end: date) -> int:
    if end == start:
        return 0
    step = 1 if end > start else -1
    current = start
    count = 0
    while current != end:
        current += timedelta(days=step)
        if is_workday(current):
            count += step
    return count


def parse_multiple_monthly_dates(text: object) -> list[int]:
    if pd.isna(text):
        return []
    candidates = [int(match) for match in re.findall(r"\b([0-3]?\d)(?:st|nd|rd|th)?\b", str(text))]
    return sorted({value for value in candidates if 1 <= value <= 31})


def derive_cutoff_date(row: pd.Series) -> tuple[object, str]:
    receive_date = pd.Timestamp(row["receive_date"]).date()
    cutoff_rule = str(row["cutoff_rule"]).strip()
    cutoff_type = row.get("cutoff_type")
    cutoff_value = pd.to_numeric(row.get("cutoff_value"), errors="coerce")

    if cutoff_rule == "NO_CUTOFF":
        return pd.NaT, "NO_CUTOFF; no cutoff date required"

    if cutoff_rule == "END_MONTH":
        return last_workday_of_month(receive_date.year, receive_date.month), "END_MONTH; last workday of receive month"

    if cutoff_rule == "MONTHLY_DATE":
        text = "" if pd.isna(cutoff_type) else str(cutoff_type).lower()
        if pd.isna(cutoff_value) and "working days before end of month" in text:
            match = re.search(r"(\d+)\s+working days before end of month", text)
            if match:
                days_before = int(match.group(1))
                target = last_workday_of_month(receive_date.year, receive_date.month)
                moved = 0
                while moved < days_before:
                    target -= timedelta(days=1)
                    if is_workday(target):
                        moved += 1
                return target, "MONTHLY_DATE; parsed working-days-before-end-of-month rule"
        if pd.isna(cutoff_value):
            listed_dates = parse_multiple_monthly_dates(cutoff_type)
            if listed_dates:
                for cutoff_day in listed_dates:
                    target = safe_date(receive_date.year, receive_date.month, cutoff_day)
                    if target >= receive_date:
                        return target, "MONTHLY_DATE; parsed next listed date from cutoff_type"
                next_month = add_months(receive_date, 1)
                return safe_date(next_month.year, next_month.month, listed_dates[0]), "MONTHLY_DATE; parsed first listed date in next month from cutoff_type"
            return pd.NaT, "MONTHLY_DATE; cutoff_value missing and cutoff_type could not be parsed"
        target = safe_date(receive_date.year, receive_date.month, int(cutoff_value))
        if target < receive_date:
            next_month = add_months(receive_date, 1)
            target = safe_date(next_month.year, next_month.month, int(cutoff_value))
        return target, "MONTHLY_DATE; cutoff date selected from receive_date month or next month"

    if cutoff_rule == "MULTIPLE_MONTHLY_DATE":
        dates = parse_multiple_monthly_dates(cutoff_type)
        if not dates:
            return pd.NaT, "MULTIPLE_MONTHLY_DATE; no dates could be parsed from cutoff_type"
        for cutoff_day in dates:
            target = safe_date(receive_date.year, receive_date.month, cutoff_day)
            if target >= receive_date:
                return target, "MULTIPLE_MONTHLY_DATE; next listed date in receive month"
        next_month = add_months(receive_date, 1)
        return safe_date(next_month.year, next_month.month, dates[0]), "MULTIPLE_MONTHLY_DATE; first listed date in next month"

    if cutoff_rule == "NEXT_MONTH_DATE":
        if pd.isna(cutoff_value):
            return pd.NaT, "NEXT_MONTH_DATE; cutoff_value missing"
        next_month = add_months(receive_date, 1)
        return safe_date(next_month.year, next_month.month, int(cutoff_value)), "NEXT_MONTH_DATE; date in next month"

    if cutoff_rule == "NEXT_MONTH_WORKDAY":
        if pd.isna(cutoff_value):
            return pd.NaT, "NEXT_MONTH_WORKDAY; cutoff_value missing"
        next_month = add_months(receive_date, 1)
        return nth_workday(next_month.year, next_month.month, int(cutoff_value)), "NEXT_MONTH_WORKDAY; nth workday in next month"

    if cutoff_rule == "NEXT_MONTH_FIRST_WEEK":
        next_month = add_months(receive_date, 1)
        return nth_workday(next_month.year, next_month.month, 5), "NEXT_MONTH_FIRST_WEEK; fifth workday in next month"

    return pd.NaT, f"{cutoff_rule}; unsupported cutoff_rule for decision-time derivation"


def next_receive_gap_from_decision_date(receive_date: pd.Timestamp, receive_day_code: object) -> object:
    codes = parse_day_codes(receive_day_code)
    if not codes or pd.isna(receive_date):
        return np.nan
    weekday_code = pd.Timestamp(receive_date).weekday() + 1
    for gap in range(0, 8):
        candidate_code = ((weekday_code - 1 + gap) % 7) + 1
        if candidate_code in codes:
            return gap
    return np.nan


def load_source() -> pd.DataFrame:
    df = pd.read_excel(SOURCE_FILE, sheet_name=SOURCE_SHEET)
    df = clean_blanks(df)
    df = df[df["invoice_no"].notna()].copy()
    df["_source_excel_row"] = df.index + 2
    df["receive_date"] = pd.to_datetime(df["receive_date"], errors="coerce")
    df["sent_date"] = pd.to_datetime(df["sent_date"], errors="coerce")
    return df.reset_index(drop=True)


def remove_duplicates(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    sortable = df.copy()
    sortable["_receive_sort"] = sortable["receive_date"].fillna(pd.Timestamp.max)
    sortable["_sent_sort"] = sortable["sent_date"].fillna(pd.Timestamp.max)
    sortable = sortable.sort_values(["invoice_no", "_receive_sort", "_sent_sort", "_source_excel_row"])
    keep_indices = sortable.groupby("invoice_no", sort=False).head(1).index

    duplicate_groups = df[df["invoice_no"].duplicated(keep=False)].copy()
    representative_by_invoice = df.loc[keep_indices].set_index("invoice_no")["_source_excel_row"].to_dict()
    duplicate_groups["duplicate_action"] = np.where(
        duplicate_groups.index.isin(keep_indices), "kept_representative", "removed_before_split"
    )
    duplicate_groups["representative_source_excel_row"] = duplicate_groups["invoice_no"].map(representative_by_invoice)
    duplicate_groups["duplicate_handling_reason"] = (
        "One representative record kept per invoice_no; earliest receive_date is preferred, then earliest sent_date, then first source row."
    )

    cleaned = df.loc[keep_indices].sort_values("_source_excel_row").copy()
    cleaned = cleaned.drop(columns=["_receive_sort", "_sent_sort"], errors="ignore")
    duplicate_report = duplicate_groups.sort_values(["invoice_no", "_source_excel_row"]).drop(
        columns=["_receive_sort", "_sent_sort"], errors="ignore"
    )
    return cleaned.reset_index(drop=True), duplicate_report


def add_decision_time_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    repaired = df.copy()

    repaired["receive_weekday_code"] = repaired["receive_date"].dt.weekday + 1
    repaired["receive_weekday_name"] = repaired["receive_date"].dt.day_name()
    repaired["receive_day_of_month"] = repaired["receive_date"].dt.day
    repaired["receive_week_of_month"] = ((repaired["receive_day_of_month"] - 1) // 7 + 1).astype("Int64")
    repaired["receive_month_end_flag"] = np.where(repaired["receive_day_of_month"] >= 25, "Yes", "No")
    repaired["limited_receive_schedule_flag"] = np.where(
        repaired["receive_schedule"].astype(str).str.strip().str.lower().eq("everyday"),
        "No",
        "Yes",
    )

    repaired["next_receive_day_gap_decision_time"] = [
        next_receive_gap_from_decision_date(receive_date, code)
        for receive_date, code in zip(repaired["receive_date"], repaired["receive_day_code"], strict=False)
    ]
    repaired["receive_date_schedule_status"] = np.where(
        pd.Series(repaired["next_receive_day_gap_decision_time"]).isna(),
        "UNKNOWN_RECEIVE_DAY",
        np.where(
            pd.Series(repaired["next_receive_day_gap_decision_time"]).eq(0),
            "VALID_RECEIVE_DAY",
            "NEXT_RECEIVE_DAY_AVAILABLE_LATER",
        ),
    )

    cutoff_dates = repaired.apply(derive_cutoff_date, axis=1, result_type="expand")
    cutoff_dates.columns = ["cutoff_date_decision_time", "cutoff_derivation_note"]
    repaired = pd.concat([repaired, cutoff_dates], axis=1)
    repaired["cutoff_date_decision_time"] = pd.to_datetime(repaired["cutoff_date_decision_time"], errors="coerce")

    repaired["days_to_cutoff_source"] = pd.to_numeric(repaired["days_to_cutoff"], errors="coerce")
    repaired["days_to_cutoff_decision_time"] = np.nan
    has_cutoff_date = repaired["cutoff_date_decision_time"].notna()
    no_cutoff = repaired["cutoff_rule"].eq("NO_CUTOFF")
    repaired.loc[no_cutoff, "days_to_cutoff_decision_time"] = 999
    repaired.loc[has_cutoff_date, "days_to_cutoff_decision_time"] = [
        workday_gap(start.date(), end.date())
        for start, end in zip(
            repaired.loc[has_cutoff_date, "receive_date"],
            repaired.loc[has_cutoff_date, "cutoff_date_decision_time"],
            strict=False,
        )
    ]

    derivation_issues = []
    missing_gap = repaired["next_receive_day_gap_decision_time"].isna()
    if missing_gap.any():
        for _, row in repaired.loc[missing_gap].iterrows():
            derivation_issues.append(
                {
                    "feature": "next_receive_day_gap_decision_time",
                    "invoice_no": row["invoice_no"],
                    "source_excel_row": row["_source_excel_row"],
                    "issue": "Cannot derive because receive_day_code is missing or invalid.",
                    "action": "Keep value as missing; exclude rows or impute only after expert/data-owner confirmation.",
                }
            )
    missing_cutoff = repaired["days_to_cutoff_decision_time"].isna()
    if missing_cutoff.any():
        for _, row in repaired.loc[missing_cutoff].iterrows():
            derivation_issues.append(
                {
                    "feature": "days_to_cutoff_decision_time",
                    "invoice_no": row["invoice_no"],
                    "source_excel_row": row["_source_excel_row"],
                    "issue": row["cutoff_derivation_note"],
                    "action": "Do not use source days_to_cutoff for this row without manual cutoff validation.",
                }
            )

    return repaired, pd.DataFrame(derivation_issues)


def medium_candidate_reasons(row: pd.Series) -> list[str]:
    reasons: list[str] = []
    days = pd.to_numeric(row["days_to_cutoff_decision_time"], errors="coerce")
    gap = pd.to_numeric(row["next_receive_day_gap_decision_time"], errors="coerce")

    if pd.notna(days) and row["cutoff_rule"] != "NO_CUTOFF" and 3 <= days <= 10:
        reasons.append("days_to_cutoff_decision_time between 3 and 10")
    if row["limited_receive_schedule_flag"] == "Yes" and (pd.isna(gap) or gap > 1) and (pd.isna(days) or days > 2):
        reasons.append("limited receive schedule, but not immediately due today/tomorrow")
    if pd.notna(days) and row["cutoff_rule"] != "NO_CUTOFF" and 2 < days <= 10 and row["receive_month_end_flag"] == "No":
        reasons.append("approaching cutoff but not immediately urgent and not month-end")
    return reasons


def build_medium_candidates(df: pd.DataFrame) -> pd.DataFrame:
    candidate_rows = []
    for _, row in df.iterrows():
        reasons = medium_candidate_reasons(row)
        if not reasons:
            continue
        candidate_rows.append(
            {
                "invoice_no": row["invoice_no"],
                "source_excel_row": row["_source_excel_row"],
                "customer_name_masking": row["customer_name_masking"],
                "receive_date": row["receive_date"].date() if pd.notna(row["receive_date"]) else "",
                "cutoff_rule": row["cutoff_rule"],
                "cutoff_type": row["cutoff_type"],
                "cutoff_value": row["cutoff_value"],
                "cutoff_date_decision_time": row["cutoff_date_decision_time"].date()
                if pd.notna(row["cutoff_date_decision_time"])
                else "",
                "days_to_cutoff_source": row["days_to_cutoff_source"],
                "days_to_cutoff_decision_time": row["days_to_cutoff_decision_time"],
                "receive_schedule": row["receive_schedule"],
                "receive_day_code": row["receive_day_code"],
                "next_receive_day_gap_decision_time": row["next_receive_day_gap_decision_time"],
                "receive_date_schedule_status": row["receive_date_schedule_status"],
                "current_expert_label": row["expert_label"],
                "current_expert_reason": row["expert_reason"],
                "candidate_reason": "; ".join(reasons),
                "expert_review_label": "",
                "expert_review_note": "",
            }
        )
    return pd.DataFrame(candidate_rows).sort_values(
        ["days_to_cutoff_decision_time", "invoice_no"], na_position="last"
    )


def build_feature_policy() -> tuple[pd.DataFrame, pd.DataFrame]:
    remaining = pd.DataFrame(
        [
            ["customer_name_masking", "Retain", "Masked customer identity; available at decision time."],
            ["cutoff_rule", "Retain", "Customer regulation; available before invoice decision."],
            ["cutoff_value", "Retain", "Customer regulation; use with missing-value review where absent."],
            ["receive_schedule", "Retain", "Customer regulation; available before invoice decision."],
            ["receive_day_code", "Retain", "Customer regulation; needed for schedule gap derivation."],
            ["days_to_cutoff_decision_time", "Retain", "Receive-date/customer-regulation replacement for source days_to_cutoff."],
            ["next_receive_day_gap_decision_time", "Retain with missing review", "Derived from receive_date and receive_day_code only."],
            ["receive_date_schedule_status", "Retain", "Decision-time schedule status derived from receive_date and customer receive days."],
            ["receive_weekday_code", "Retain", "Operational date attribute; avoids raw-date memorization."],
            ["receive_week_of_month", "Retain", "Operational date attribute for early/mid/late month pattern."],
            ["receive_day_of_month", "Retain", "Operational date attribute; interpretable and less specific than full raw date."],
            ["receive_month_end_flag", "Retain", "Decision-time replacement for month_end_flag."],
            ["limited_receive_schedule_flag", "Retain", "Operational simplification of receive_schedule."],
        ],
        columns=["feature", "decision", "rationale"],
    )

    removed = pd.DataFrame(
        [
            ["sent_date", "Remove from training", "Not known if priority must be predicted at invoice receive/decision time; retained only for traceability."],
            ["days_to_cutoff", "Replace", "Guideline defines it from sent_date; replaced by days_to_cutoff_decision_time."],
            ["next_receive_day_gap", "Replace", "Source column is empty and previous derivation used sent_date; replaced by receive-date version."],
            ["missed_receive_schedule", "Replace/remove", "Original meaning depends on send date; replaced by receive_date_schedule_status."],
            ["month_end_flag", "Replace", "Source column is empty and previous derivation used sent_date; replaced by receive_month_end_flag."],
            ["receive_date_feature/raw receive_date", "Remove from training", "Raw dates can let a small tree memorize sample-specific collection days; use weekday/week/month-end attributes instead."],
            ["expert_label", "Target only", "Must never be used as a feature."],
            ["expert_reason", "Exclude from training", "Explanation text is label-derived and would leak expert judgment."],
            ["rule_based_label", "Exclude from training", "Model output/helper column, not an input feature."],
            ["rule_based_reason", "Exclude from training", "Model output/helper explanation, not an input feature."],
        ],
        columns=["feature", "decision", "rationale"],
    )
    return remaining, removed


def write_report(
    cleaned: pd.DataFrame,
    duplicate_report: pd.DataFrame,
    derivation_issues: pd.DataFrame,
    medium_candidates: pd.DataFrame,
    remaining_features: pd.DataFrame,
    removed_features: pd.DataFrame,
) -> None:
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

    removed_duplicates = duplicate_report[duplicate_report["duplicate_action"].eq("removed_before_split")]
    report_lines = [
        "# Experimental Design Repair Report",
        "",
        "## Scope",
        "",
        "This repair stops before model training. It creates a cleaned decision-time dataset and expert-review table for candidate MEDIUM cases.",
        "",
        "## Duplicate Handling",
        "",
        f"- Source labeled rows: 107",
        f"- Cleaned rows after duplicate handling: {len(cleaned)}",
        f"- Removed duplicate rows: {len(removed_duplicates)}",
        "- Rule: keep one representative per invoice number, preferring the earliest receive_date, then earliest sent_date, then first source row.",
        "",
        md_table(
            removed_duplicates[
                [
                    "invoice_no",
                    "_source_excel_row",
                    "receive_date",
                    "sent_date",
                    "expert_label",
                    "expert_reason",
                    "representative_source_excel_row",
                ]
            ]
        ),
        "",
        "## Prediction-Time Definition",
        "",
        "The repaired dataset defines prediction time as `receive_date`. Features that previously depended on `sent_date` are replaced with receive-date/customer-regulation equivalents where possible.",
        "",
        "## Remaining Feature Set for Future Evaluation",
        "",
        md_table(remaining_features),
        "",
        "## Removed or Replaced Features",
        "",
        md_table(removed_features),
        "",
        "## Date Feature Review",
        "",
        "Raw `receive_date` should remain only for traceability and should not be used directly for training. In this small dataset, raw dates can encode the specific sampling period and allow a Decision Tree to memorize date-specific patterns. The repaired feature set uses operational date attributes instead: weekday, week of month, day of month, and month-end flag.",
        "",
        "## Derivation Issues Requiring Review",
        "",
        md_table(derivation_issues),
        "",
        "## Candidate MEDIUM Review Cases",
        "",
        f"- Candidate rows prepared for expert review: {len(medium_candidates)}",
        "- These rows are not relabeled automatically.",
        "- Expert should fill `expert_review_label` and `expert_review_note` in the review table.",
        "",
    ]
    (OUTPUT_DIR / "design_repair_report.md").write_text("\n".join(report_lines), encoding="utf-8")


def main() -> None:
    ensure_output_dir()
    source = load_source()
    cleaned, duplicate_report = remove_duplicates(source)
    repaired, derivation_issues = add_decision_time_features(cleaned)
    medium_candidates = build_medium_candidates(repaired)
    remaining_features, removed_features = build_feature_policy()

    repaired.to_csv(OUTPUT_DIR / "cleaned_decision_time_dataset.csv", index=False)
    duplicate_report.to_csv(OUTPUT_DIR / "duplicate_handling_report.csv", index=False)
    duplicate_report[duplicate_report["duplicate_action"].eq("removed_before_split")].to_csv(
        OUTPUT_DIR / "removed_duplicate_rows.csv", index=False
    )
    derivation_issues.to_csv(OUTPUT_DIR / "decision_time_derivation_issues.csv", index=False)
    medium_candidates.to_csv(OUTPUT_DIR / "candidate_medium_expert_review.csv", index=False)
    remaining_features.to_csv(OUTPUT_DIR / "remaining_feature_set.csv", index=False)
    removed_features.to_csv(OUTPUT_DIR / "removed_or_replaced_features.csv", index=False)

    with pd.ExcelWriter(OUTPUT_DIR / "candidate_medium_expert_review.xlsx") as writer:
        medium_candidates.to_excel(writer, sheet_name="MEDIUM candidates", index=False)
        removed_features.to_excel(writer, sheet_name="Removed features", index=False)
        remaining_features.to_excel(writer, sheet_name="Remaining features", index=False)
        duplicate_report.to_excel(writer, sheet_name="Duplicate handling", index=False)

    write_report(
        repaired,
        duplicate_report,
        derivation_issues,
        medium_candidates,
        remaining_features,
        removed_features,
    )

    print(f"Cleaned decision-time dataset rows: {len(repaired)}")
    print(f"Removed duplicate rows: {len(duplicate_report[duplicate_report['duplicate_action'].eq('removed_before_split')])}")
    print(f"Candidate MEDIUM review rows: {len(medium_candidates)}")
    print(f"Artifacts written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
