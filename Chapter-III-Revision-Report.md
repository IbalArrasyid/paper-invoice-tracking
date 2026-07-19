# Chapter III Revision Report

## Status

The dataset, experimental protocol, and active `Metodologi.tex` are revised. Finalization still requires label-provenance evidence, SOP-to-rule traceability, and LaTeX compilation.

## 1. Methodological Identity

Chapter III must present a comparative binary-classification study:

- ground truth: the supplied historical label source;
- target: `Urgent` and `Not Urgent`;
- Rule-Based: constructed from company SOP through Knowledge Acquisition and Rule Construction;
- Decision Tree: trained on historical attributes and training-partition labels; and
- evaluation: E1 80:20, E2 70:30, E3 5-fold CV, and E4 LOOCV.

Knowledge Engineering remains a supporting process for Rule-Based development. Comparative Analysis is the primary contribution.

## 2. Verified Dataset

| Item | Result |
|---|---:|
| Source file | `dataset_invoice.xlsx` |
| Source rows | 101 |
| Unique invoices | 99 |
| Removed duplicate rows | 2 |
| Urgent | 30 |
| Not Urgent | 69 |

The source column is `expert_label`. The authorized normalization is `HIGH = Urgent` and `NORMAL = Not Urgent`. Chapter III must document evidence that these labels represent administrator decisions; the workbook alone does not state that provenance explicitly.

## 3. Data Preparation

1. Read the `Data Labeling` sheet without altering the source workbook.
2. Retain one earliest record for each duplicated `invoice_no`.
3. Normalize the binary target.
4. Derive cutoff and schedule features using information available at `receive_date`.
5. Exclude leakage and identity fields.
6. Freeze the cleaned dataset and feature policy.

Excluded predictors: `expert_reason`, `sent_date`, `invoice_no`, customer identity, `Driver`, and the source `days_to_cutoff`. The last field is replaced with a decision-time calculation.

## 4. Rule-Based Method

The Rule Base uses SOP-derived conditions for missed receiving days, overdue or near cutoff, month-end conditions, and limited receiving schedules. It produces `Urgent` when at least one urgency rule is active and `Not Urgent` through the default rule. Every prediction stores its Rule ID.

The Rule Base must not be tuned using validation labels. Chapter III must include the final rule table, precedence, conflict handling, default behavior, and SOP traceability.

## 5. Decision Tree Method

The Decision Tree uses entropy. Categorical features are one-hot encoded; numerical features pass through the pipeline. Candidate values are:

- `max_depth`: 2, 3, 4, or unlimited;
- `min_samples_leaf`: 1, 2, or 4.

Selection uses stratified inner validation on training data only. The final full-data tree is used for interpretation, not performance estimation.

## 6. Experimental Design

| ID | Scenario | Evaluation set |
|---|---|---|
| E1 | Stratified hold-out 80:20 | Shared 20% test invoices |
| E2 | Stratified hold-out 70:30 | Shared 30% test invoices |
| E3 | Stratified 5-fold CV | Aggregated out-of-fold predictions |
| E4 | LOOCV | Aggregated held-out predictions |

Both methods use identical validation invoice IDs. `Urgent` is the positive class. Report accuracy, precision, recall, F1, macro F1, confusion matrices, paired disagreements, and exact McNemar results.

## 7. Reproducibility

- Random seed: 42.
- Pipeline: `run_comparative_experiment.py`.
- Dependencies: `requirements-comparative-experiment.txt`.
- Configuration: `comparative_experiment/experiment_config.json`.
- Case-level predictions: `comparative_experiment/predictions/all_scenario_predictions.csv`.
- Cleaned analysis data: `comparative_experiment/data/cleaned_analysis_dataset.csv`.

## 8. Chapter III Revision Checklist

- [x] Binary target defined.
- [x] Duplicate handling documented.
- [x] Leakage-prone fields excluded.
- [x] Rule-Based and Decision Tree procedures separated.
- [x] E1-E4 executed reproducibly.
- [x] LOOCV metrics aggregated correctly.
- [ ] Label provenance evidence added to the thesis.
- [ ] Complete SOP-to-rule traceability table added.
- [x] `Metodologi.tex` rewritten using the executed protocol.
- [ ] Revised LaTeX compiled and checked.

## 9. Next Action

Complete the label-provenance evidence and SOP-to-rule traceability table, then compile and visually audit Chapter III. Do not restore Guideline-Based Ground Truth, three-class labels, Decision Tree reconstruction, or Knowledge Representation Consistency terminology.
