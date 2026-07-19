# Chapter IV Revision Report

## Status

The revised experiment is complete. `Hasil-dan-Pembahasan.tex` still contains legacy evidence and was not modified in this stage.

## 1. Dataset Result

The source contains 101 rows. Duplicate handling leaves 99 unique invoices: 30 `Urgent` and 69 `Not Urgent`. Two duplicate rows were removed. Six data-quality entries were documented during cutoff and schedule-feature derivation.

The source label column is `expert_label`, normalized as `HIGH = Urgent` and `NORMAL = Not Urgent`. The thesis must provide supporting evidence that the field records administrator decisions.

## 2. Comparative Metrics

| Scenario | Method | Accuracy | Precision Urgent | Recall Urgent | F1 Urgent | Macro F1 |
|---|---|---:|---:|---:|---:|---:|
| E1 80:20 | Rule-Based | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| E1 80:20 | Decision Tree | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| E2 70:30 | Rule-Based | 0.9333 | 1.0000 | 0.7778 | 0.8750 | 0.9148 |
| E2 70:30 | Decision Tree | 0.9667 | 1.0000 | 0.8889 | 0.9412 | 0.9590 |
| E3 5-fold | Rule-Based | 0.9394 | 1.0000 | 0.8000 | 0.8889 | 0.9236 |
| E3 5-fold | Decision Tree | 0.9596 | 0.9643 | 0.9000 | 0.9310 | 0.9512 |
| E4 LOOCV | Rule-Based | 0.9394 | 1.0000 | 0.8000 | 0.8889 | 0.9236 |
| E4 LOOCV | Decision Tree | 0.9798 | 0.9667 | 0.9667 | 0.9667 | 0.9761 |

## 3. Comparative Interpretation

Decision Tree performs better descriptively in E2-E4 and detects more `Urgent` invoices. In E4, Rule-Based has 6 false negatives and no false positives; Decision Tree has 1 false negative and 1 false positive.

The paired differences are not statistically significant. Exact McNemar results are `p = 0.7266` for E3 and `p = 0.2891` for E4. The valid claim is that Decision Tree shows a performance advantage on this dataset, not that it is universally superior.

E1 gives 100% accuracy for both methods on 20 test invoices. This result must be presented with E2-E4 and cannot support a standalone conclusion.

## 4. Error Analysis

The six Rule-Based false negatives in full-data evaluation activate the default rule. All involve limited receiving schedules with a next receiving-day gap of 2-5 days. This indicates that the Rule-Based threshold is more conservative than the supplied labels.

The revised Chapter IV should include cases where:

- only Rule-Based is correct;
- only Decision Tree is correct;
- both are wrong; and
- both are correct.

Case-level evidence is stored in `comparative_experiment/tables/misclassification_cases.csv`.

## 5. Decision Tree Interpretation

The final interpretive tree has depth 2 and 4 leaves. Its impurity-based importance is concentrated in:

| Feature | Importance |
|---|---:|
| `limited_receive_schedule_flag` | 56.96% |
| `days_to_cutoff_feature` | 39.78% |
| `cutoff_value_feature` | 3.26% |

Feature importance is descriptive and must not be interpreted causally.

## 6. Required Chapter IV Structure

1. Dataset and ground-truth analysis.
2. Experimental configuration.
3. Rule-Based results.
4. Decision Tree results.
5. Comparative performance and paired analysis.
6. Error and misclassification cases.
7. Comparative operational characteristics.
8. Discussion and threats to validity.

Comparative Analysis must be the chapter's main section. Explainability, maintainability, adaptability, computational cost, and SOP compliance require observable evidence or a stated rubric.

## 7. Validity Boundaries

- The analysis uses 99 unique invoices from one organizational context.
- Class distribution is 69.70% `Not Urgent` and 30.30% `Urgent`.
- The label-provenance document is not present in the workbook.
- E1 is sensitive to its small test set.
- McNemar tests have limited power with few disagreements.
- External or temporal generalization has not been tested.

## 8. Chapter IV Revision Checklist

- [x] E1-E4 completed on shared validation cases.
- [x] Out-of-fold predictions validated.
- [x] Confusion matrices and class metrics generated.
- [x] Paired comparisons generated.
- [x] Rule IDs and error cases preserved.
- [x] Tree depth, leaves, and feature importance recorded.
- [ ] Label provenance evidence added.
- [ ] SOP traceability and rule-freezing record added.
- [ ] Operational-characteristic rubric completed.
- [ ] `Hasil-dan-Pembahasan.tex` rewritten.
- [ ] Revised LaTeX compiled and audited.

## 9. Evidence Location

Use `Comparative-Experiment-Report.md` for the concise result summary and `comparative_experiment` for reproducible tables, predictions, model artifacts, and reports.
