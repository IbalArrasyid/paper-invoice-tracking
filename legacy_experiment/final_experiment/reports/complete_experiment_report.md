# Complete Final Experiment Report

## Dataset

Dataset used: `O:\paper-invoice-tracking\experiment_design_repair\finalized_guideline_labeled_dataset.xlsx`
Target column: `final_label`

## Validation

| Item | Value |
| --- | --- |
| Rows | 105 |
| Unique invoice_no | 105 |
| Duplicated invoice_no | 0 |
| Missing final_label | 0 |
| Invalid final_label values | 0 |
| Invalid cutoff_rule values | 0 |
| Validation blockers | 0 |
| Validation warnings | 2 |

## Train-Test Split

Split method: stratified random split, `test_size = 0.20`, `random_state = 42`.

| class | train_count | test_count |
| --- | --- | --- |
| HIGH | 22 | 5 |
| MEDIUM | 26 | 7 |
| NORMAL | 36 | 9 |
| TOTAL | 84 | 21 |

## Metric Comparison

| scope | model | n | accuracy | precision_weighted | recall_weighted | f1_weighted | precision_macro | recall_macro | f1_macro |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| test | Rule-Based | 21 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| test | Decision Tree C4.5 | 21 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

## Per-Class Performance

| class_or_metric | scope | model | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- | --- | --- |
| HIGH | test | Rule-Based | 1.0 | 1.0 | 1.0 | 5.0 |
| MEDIUM | test | Rule-Based | 1.0 | 1.0 | 1.0 | 7.0 |
| NORMAL | test | Rule-Based | 1.0 | 1.0 | 1.0 | 9.0 |
| accuracy | test | Rule-Based | 1.0 | 1.0 | 1.0 | 1.0 |
| macro avg | test | Rule-Based | 1.0 | 1.0 | 1.0 | 21.0 |
| weighted avg | test | Rule-Based | 1.0 | 1.0 | 1.0 | 21.0 |
| HIGH | test | Decision Tree C4.5 | 1.0 | 1.0 | 1.0 | 5.0 |
| MEDIUM | test | Decision Tree C4.5 | 1.0 | 1.0 | 1.0 | 7.0 |
| NORMAL | test | Decision Tree C4.5 | 1.0 | 1.0 | 1.0 | 9.0 |
| accuracy | test | Decision Tree C4.5 | 1.0 | 1.0 | 1.0 | 1.0 |
| macro avg | test | Decision Tree C4.5 | 1.0 | 1.0 | 1.0 | 21.0 |
| weighted avg | test | Decision Tree C4.5 | 1.0 | 1.0 | 1.0 | 21.0 |

## Rule Usage Statistics

| scope | Rule ID | frequency |
| --- | --- | --- |
| all | R10 | 38 |
| all | R11 | 7 |
| all | R2 | 1 |
| all | R3 | 3 |
| all | R4 | 4 |
| all | R6 | 5 |
| all | R7 | 17 |
| all | R8 | 30 |
| all | R9 | 7 |
| test | R10 | 8 |
| test | R11 | 1 |
| test | R4 | 1 |
| test | R6 | 1 |
| test | R7 | 3 |
| test | R8 | 7 |
| train | R10 | 30 |
| train | R11 | 6 |
| train | R2 | 1 |
| train | R3 | 3 |
| train | R4 | 3 |
| train | R6 | 4 |
| train | R7 | 14 |
| train | R8 | 23 |
| train | R9 | 7 |

## Misclassification Analysis

No rows.

## Feature Importance Ranking

| feature | importance |
| --- | --- |
| days_to_cutoff_decision_time | 0.48182753089060987 |
| receive_day_code | 0.2983590013195632 |
| next_receive_day_gap_feature | 0.14293016926194543 |
| receive_schedule | 0.07688329852788157 |
| customer_name_masking | 0.0 |
| receive_date_schedule_status | 0.0 |
| cutoff_rule | 0.0 |
| limited_receive_schedule_flag | 0.0 |
| receive_month_end_flag | 0.0 |
| cutoff_value_feature | 0.0 |
| receive_weekday_code | 0.0 |
| receive_week_of_month | 0.0 |
| receive_day_of_month | 0.0 |

## Interpretation

See `reports/scientific_interpretation.md` for the structured interpretation used as the basis for Chapter IV discussion.
