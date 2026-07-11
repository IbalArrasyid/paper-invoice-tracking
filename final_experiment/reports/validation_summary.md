# Final Data Validation Summary

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

## Validation Issues

| severity | column | issue | affected_rows | action |
| --- | --- | --- | --- | --- |
| WARNING | next_receive_day_gap_decision_time | Missing schedule gap values remain for rows with unavailable receive_day_code. | 3 | Handled in Decision Tree with numeric missing sentinel and Rule-Based fallback. |
| WARNING | cutoff_value | Missing cutoff_value remains for some customer regulations. | 5 | Handled with numeric missing sentinel for Decision Tree. |
