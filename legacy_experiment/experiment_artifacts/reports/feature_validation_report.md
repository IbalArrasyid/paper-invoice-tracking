# Feature Validation Report

## Required Feature Status

| required_feature | source_column | experiment_column | status | source_missing_count | derivation_or_note |
| --- | --- | --- | --- | --- | --- |
| customer | customer_name_masking | customer_name_masking | available_as_alias | 0 | customer is represented by customer_name_masking for privacy; customer_name is retained only for traceability. |
| receive_date | receive_date | receive_date | available | 0 |  |
| cutoff_rule | cutoff_rule | cutoff_rule | available | 0 |  |
| cutoff_value | cutoff_value | cutoff_value | available | 5 |  |
| receive_schedule | receive_schedule | receive_schedule | available | 0 |  |
| receive_day_code | receive_day_code | receive_day_code | available | 3 |  |
| days_to_cutoff | days_to_cutoff | days_to_cutoff | available | 0 |  |
| next_receive_day_gap | next_receive_day_gap | next_receive_day_gap_experiment | derived_in_experiment_copy | 107 | Derived from sent_date and receive_day_code as days to the next valid receiving day, based on the Guidelines sheet. |
| missed_receive_schedule | missed_receive_schedule | missed_receive_schedule_experiment | validated_with_derivation | 0 | Recomputed from sent_date and receive_day_code; disagreements are reported in validation_issues.csv. |
| month_end_flag | month_end_flag | month_end_flag_experiment | derived_in_experiment_copy | 107 | Derived from sent_date day >= 25, based on the Guidelines sheet. |
| expert_label | expert_label | expert_label | available | 0 |  |

## Modeling Notes

- Source datasets were not modified.
- `next_receive_day_gap_experiment` and `month_end_flag_experiment` were created only in the experiment copy because their derivation is defined in the Guidelines sheet.
- `customer` is represented by `customer_name_masking` in the Decision Tree feature matrix.
- `expert_label` contains HIGH and NORMAL only; MEDIUM has no ground-truth examples.
