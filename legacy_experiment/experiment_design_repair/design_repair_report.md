# Experimental Design Repair Report

## Scope

This repair stops before model training. It creates a cleaned decision-time dataset and expert-review table for candidate MEDIUM cases.

## Duplicate Handling

- Source labeled rows: 107
- Cleaned rows after duplicate handling: 105
- Removed duplicate rows: 2
- Rule: keep one representative per invoice number, preferring the earliest receive_date, then earliest sent_date, then first source row.

| invoice_no | _source_excel_row | receive_date | sent_date | expert_label | expert_reason | representative_source_excel_row |
| --- | --- | --- | --- | --- | --- | --- |
| S202605-0609 | 64 | 2026-05-22 | 2026-05-22 | NORMAL | LONG_TIME_TO_CUTOFF | 59 |
| S202605-0634 | 72 | 2026-05-22 | 2026-05-22 | NORMAL | NO_CUTOFF | 62 |

## Prediction-Time Definition

The repaired dataset defines prediction time as `receive_date`. Features that previously depended on `sent_date` are replaced with receive-date/customer-regulation equivalents where possible.

## Remaining Feature Set for Future Evaluation

| feature | decision | rationale |
| --- | --- | --- |
| customer_name_masking | Retain | Masked customer identity; available at decision time. |
| cutoff_rule | Retain | Customer regulation; available before invoice decision. |
| cutoff_value | Retain | Customer regulation; use with missing-value review where absent. |
| receive_schedule | Retain | Customer regulation; available before invoice decision. |
| receive_day_code | Retain | Customer regulation; needed for schedule gap derivation. |
| days_to_cutoff_decision_time | Retain | Receive-date/customer-regulation replacement for source days_to_cutoff. |
| next_receive_day_gap_decision_time | Retain with missing review | Derived from receive_date and receive_day_code only. |
| receive_date_schedule_status | Retain | Decision-time schedule status derived from receive_date and customer receive days. |
| receive_weekday_code | Retain | Operational date attribute; avoids raw-date memorization. |
| receive_week_of_month | Retain | Operational date attribute for early/mid/late month pattern. |
| receive_day_of_month | Retain | Operational date attribute; interpretable and less specific than full raw date. |
| receive_month_end_flag | Retain | Decision-time replacement for month_end_flag. |
| limited_receive_schedule_flag | Retain | Operational simplification of receive_schedule. |

## Removed or Replaced Features

| feature | decision | rationale |
| --- | --- | --- |
| sent_date | Remove from training | Not known if priority must be predicted at invoice receive/decision time; retained only for traceability. |
| days_to_cutoff | Replace | Guideline defines it from sent_date; replaced by days_to_cutoff_decision_time. |
| next_receive_day_gap | Replace | Source column is empty and previous derivation used sent_date; replaced by receive-date version. |
| missed_receive_schedule | Replace/remove | Original meaning depends on send date; replaced by receive_date_schedule_status. |
| month_end_flag | Replace | Source column is empty and previous derivation used sent_date; replaced by receive_month_end_flag. |
| receive_date_feature/raw receive_date | Remove from training | Raw dates can let a small tree memorize sample-specific collection days; use weekday/week/month-end attributes instead. |
| expert_label | Target only | Must never be used as a feature. |
| expert_reason | Exclude from training | Explanation text is label-derived and would leak expert judgment. |
| rule_based_label | Exclude from training | Model output/helper column, not an input feature. |
| rule_based_reason | Exclude from training | Model output/helper explanation, not an input feature. |

## Date Feature Review

Raw `receive_date` should remain only for traceability and should not be used directly for training. In this small dataset, raw dates can encode the specific sampling period and allow a Decision Tree to memorize date-specific patterns. The repaired feature set uses operational date attributes instead: weekday, week of month, day of month, and month-end flag.

## Derivation Issues Requiring Review

| feature | invoice_no | source_excel_row | issue | action |
| --- | --- | --- | --- | --- |
| next_receive_day_gap_decision_time | S202605-0030 | 31 | Cannot derive because receive_day_code is missing or invalid. | Keep value as missing; exclude rows or impute only after expert/data-owner confirmation. |
| next_receive_day_gap_decision_time | S202605-0757 | 60 | Cannot derive because receive_day_code is missing or invalid. | Keep value as missing; exclude rows or impute only after expert/data-owner confirmation. |
| next_receive_day_gap_decision_time | S202605-2098 | 99 | Cannot derive because receive_day_code is missing or invalid. | Keep value as missing; exclude rows or impute only after expert/data-owner confirmation. |

## Candidate MEDIUM Review Cases

- Candidate rows prepared for expert review: 41
- These rows are not relabeled automatically.
- Expert should fill `expert_review_label` and `expert_review_note` in the review table.
