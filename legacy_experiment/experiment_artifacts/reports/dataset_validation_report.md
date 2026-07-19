# Dataset Validation Report

Generated from project root: `O:\paper-invoice-tracking`

## Summary

- Dataset files inspected: 3
- Sheets / sources inspected: 14
- Blockers: 0
- Warnings: 20

The canonical experiment dataset is `expert_labeling_sheet.xlsx` sheet `Data Labeling` because it contains 107 non-empty labeled invoice rows. The CSV export contains the same labeled rows but also trailing blank rows and unnamed columns.

## Dataset Inventory

| dataset | sheet | rows | columns | non_empty_rows | all_empty_columns |
| --- | --- | --- | --- | --- | --- |
| expert_labeling_sheet.csv |  | 832 | 28 | 107 | next_receive_day_gap; month_end_flag; weekday_receive; rule_based_label; rule_based_reason; Unnamed: 20; Unnamed: 21; Unnamed: 22; Unnamed: 23; Unnamed: 24; Unnamed: 25; Unnamed: 26; Unnamed: 27 |
| expert_labeling_sheet.xlsx | Data Labeling | 107 | 20 | 107 | next_receive_day_gap; month_end_flag; weekday_receive; rule_based_label; rule_based_reason |
| expert_labeling_sheet.xlsx | masking | 507 | 2 | 507 |  |
| expert_labeling_sheet.xlsx | Guidelines | 95 | 3 | 72 |  |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | LIST_INV_FINAL | 3148 | 12 | 3148 | effective_cutoff_date |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Copy of LIST_INV_FINAL | 3147 | 14 | 3147 |  |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet6 | 503 | 16 | 502 |  |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Customer_master | 510 | 6 | 508 |  |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet5 | 0 | 0 | 0 |  |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet4 | 0 | 0 | 0 |  |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet2 | 4 | 4 | 3 | Unnamed: 0 |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet1 | 857 | 5 | 782 | Unnamed: 0 |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet3 | 22 | 6 | 17 | Unnamed: 0; Unnamed: 1 |
| LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | TEST | 423 | 7 | 419 | Unnamed: 0; Unnamed: 1 |

## Validation Issues

| severity | dataset | sheet | column | issue | affected_rows | recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| WARNING | expert_labeling_sheet.csv |  | invoice_no | CSV contains trailing blank rows. | 725 | Use the non-empty invoice rows or the XLSX Data Labeling sheet as the canonical labeled dataset. |
| WARNING | expert_labeling_sheet.csv |  | Unnamed: 20; Unnamed: 21; Unnamed: 22; Unnamed: 23; Unnamed: 24; Unnamed: 25; Unnamed: 26; Unnamed: 27 | CSV contains unnamed extra columns. | 8 | Ignore unnamed columns during modeling. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | next_receive_day_gap; month_end_flag; weekday_receive; rule_based_label; rule_based_reason | Sheet contains all-empty columns. | 5 | Exclude empty columns unless they are intentionally derived later. |
| INFO | expert_labeling_sheet.xlsx | masking | Unnamed: 1 | Sheet contains unnamed/helper columns. | 1 | Inspect manually before using this sheet as a modeling dataset. |
| INFO | expert_labeling_sheet.xlsx | Guidelines | Unnamed: 1; Unnamed: 2 | Sheet contains unnamed/helper columns. | 2 | Inspect manually before using this sheet as a modeling dataset. |
| WARNING | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | LIST_INV_FINAL | effective_cutoff_date | Sheet contains all-empty columns. | 1 | Exclude empty columns unless they are intentionally derived later. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | LIST_INV_FINAL | Unnamed: 6 | Sheet contains unnamed/helper columns. | 1 | Inspect manually before using this sheet as a modeling dataset. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Copy of LIST_INV_FINAL | Unnamed: 6; Unnamed: 12; Unnamed: 13 | Sheet contains unnamed/helper columns. | 3 | Inspect manually before using this sheet as a modeling dataset. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet6 | Unnamed: 1 | Sheet contains unnamed/helper columns. | 1 | Inspect manually before using this sheet as a modeling dataset. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet5 |  | Sheet is empty or contains no meaningful rows. | 0 | Exclude this sheet from the experiment dataset. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet4 |  | Sheet is empty or contains no meaningful rows. | 0 | Exclude this sheet from the experiment dataset. |
| WARNING | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet2 | Unnamed: 0 | Sheet contains all-empty columns. | 1 | Exclude empty columns unless they are intentionally derived later. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet2 | Unnamed: 0; Unnamed: 1; Unnamed: 2; Unnamed: 3 | Sheet contains unnamed/helper columns. | 4 | Inspect manually before using this sheet as a modeling dataset. |
| WARNING | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet1 | Unnamed: 0 | Sheet contains all-empty columns. | 1 | Exclude empty columns unless they are intentionally derived later. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet1 | Unnamed: 0; Unnamed: 1; Unnamed: 2; Unnamed: 3; Unnamed: 4 | Sheet contains unnamed/helper columns. | 5 | Inspect manually before using this sheet as a modeling dataset. |
| WARNING | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet3 | Unnamed: 0; Unnamed: 1 | Sheet contains all-empty columns. | 2 | Exclude empty columns unless they are intentionally derived later. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | Sheet3 | Unnamed: 0; Unnamed: 1; Unnamed: 2; Unnamed: 3; Unnamed: 4; Unnamed: 5 | Sheet contains unnamed/helper columns. | 6 | Inspect manually before using this sheet as a modeling dataset. |
| WARNING | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | TEST | Unnamed: 0; Unnamed: 1 | Sheet contains all-empty columns. | 2 | Exclude empty columns unless they are intentionally derived later. |
| INFO | LIST INV YANG SUDAH DIKIRIM-2026 (1).xlsx | TEST | Unnamed: 0; Unnamed: 1; Unnamed: 2; Unnamed: 3; Unnamed: 4; Unnamed: 5; Unnamed: 6 | Sheet contains unnamed/helper columns. | 7 | Inspect manually before using this sheet as a modeling dataset. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | next_receive_day_gap | Required or helper column is completely empty in the source labeled dataset. | 107 | Derive in the experiment copy using the definitions in the Guidelines sheet. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | month_end_flag | Required or helper column is completely empty in the source labeled dataset. | 107 | Derive in the experiment copy using the definitions in the Guidelines sheet. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | weekday_receive | Required or helper column is completely empty in the source labeled dataset. | 107 | Exclude from modeling unless a validated derivation is available. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | rule_based_label | Required or helper column is completely empty in the source labeled dataset. | 107 | Exclude from modeling unless a validated derivation is available. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | rule_based_reason | Required or helper column is completely empty in the source labeled dataset. | 107 | Exclude from modeling unless a validated derivation is available. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | all columns | Exact duplicated rows detected. | S202605-0634; S202605-0634 | Review whether repeated invoices represent true repeat observations or accidental duplication. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | invoice_no | Duplicate invoice numbers detected. | S202605-0609; S202605-0634; S202605-0609; S202605-0634 | Confirm whether duplicate invoice numbers are legitimate repeated observations. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | expert_label | Ground truth has no examples for class(es): MEDIUM. | 1 | Report this as an experimental limitation; Decision Tree cannot learn a class absent from training data. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | receive_day_code | Missing or unparsable receive_day_code values detected. | S202605-0030; S202605-0757; S202605-2098 | Derive from customer schedule or payment schedule before relying on schedule-based rules. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | cutoff_value | cutoff_value is missing for date-based cutoff rules. | S202605-1311; S202605-0030; S202605-0757; S202605-2098; S202605-0707 | Review source cutoff descriptions; current Rule-Based rules use days_to_cutoff, but cutoff_value is still required for traceability. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | missed_receive_schedule | Source missed_receive_schedule differs from the derivation based on sent_date and receive_day_code. | S202605-0715; S202605-0721; S202605-0710 | Use the derived experiment field for reproducibility and document the disagreement. |
| WARNING | expert_labeling_sheet.xlsx | Data Labeling | next_receive_day_gap | next_receive_day_gap remains missing after derivation for rows without receive_day_code. | S202605-0030; S202605-0757; S202605-2098 | Review the customer's payment schedule; rules R7 and R9 cannot use schedule gap for these rows. |
