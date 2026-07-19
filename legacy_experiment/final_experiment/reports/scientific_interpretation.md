# Final Experiment Interpretation

## Rule-Based Model

The Rule-Based model reached test accuracy 1.0000 and macro F1 1.0000. This result is scientifically plausible because the finalized ground truth contains Guideline-Based Labeling generated from the same published operational rule base R1-R12. The Rule-Based model is therefore being evaluated against a target that is intentionally aligned with the formalized operational knowledge. Its strength is traceability: each prediction can be explained through activated rule IDs.

## Decision Tree C4.5

The Decision Tree C4.5 model reached test accuracy 1.0000 and macro F1 1.0000. The model used entropy as the split criterion and learned the formalized decision boundaries from the finalized dataset. The exported tree shows that the learned structure is dominated by operational threshold features, especially `days_to_cutoff_decision_time`, receiving-day information, and schedule-gap information. This indicates that the data-driven model successfully reconstructed the knowledge-guided labeling pattern in the held-out test split.

## Most Contributing Operational Features

| feature | importance |
| --- | --- |
| days_to_cutoff_decision_time | 0.48182753089060987 |
| receive_day_code | 0.2983590013195632 |
| next_receive_day_gap_feature | 0.14293016926194543 |
| receive_schedule | 0.07688329852788157 |

## Difficult Invoices

No rows.

No test invoice was misclassified by either model. For discussion purposes, the potentially difficult cases are not model errors in this final split but operationally sensitive rows: invoices with limited receive schedules, rows with missing receive-day code, and rows where multiple rule conditions are simultaneously true before priority resolution.

## Knowledge Formalization Effect

Knowledge Formalization is central to the final result. It converts customer regulations and operational timing concepts into structured attributes and explicit rules. The Rule-Based model consumes this knowledge directly as IF-THEN rules, while the Decision Tree consumes the same knowledge indirectly as features. Because the final labels were produced through the Operational Labeling Guideline, the experiment primarily measures whether the data-driven model can recover the formalized operational decision pattern and how transparently each paradigm represents it.

## Strengths

- Both models use the same finalized ground truth and the same cleaned decision-time dataset.
- Rule-Based predictions are traceable through activated rule IDs.
- Decision Tree outputs are interpretable through tree rules and feature importance.

## Limitations

- The dataset is small, so Decision Tree performance may vary with different train-test samples.
- The finalized labels are knowledge-guided, so perfect Rule-Based performance should be interpreted as consistency with the Operational Labeling Guideline, not as independent human validation.
- Customer-specific and schedule-specific patterns may be learned strongly because operational rules differ by customer.
- Some decision-time schedule-gap values remain missing and are handled with a missing-value sentinel for the Decision Tree.

## Practical Implications

The comparison shows whether explicit operational knowledge is sufficient for stable invoice priority recommendation or whether data-driven learning captures additional patterns from the finalized dataset. The artifacts should be used as experimental results, not as Chapter IV prose.
