# Chapter IV Final Audit

## Verdict

**The revised evidence is ready; the active Chapter IV is not yet revised.**

The new dataset audit, Rule-Based predictions, Decision Tree predictions, and E1-E4 evaluations are reproducible. `Hasil-dan-Pembahasan.tex` still presents the superseded three-class guideline experiment and cannot be submitted in its current form.

## 1. Evidence Audit

| Area | Status | Evidence |
|---|---|---|
| Dataset cleaning | Passed | 101 rows; 99 unique invoices; 2 duplicates removed |
| Binary target | Passed with caveat | 30 `Urgent`; 69 `Not Urgent`; source field is `expert_label` |
| Leakage control | Passed | Post-decision, identity, and label-derived fields excluded |
| Binary Rule-Based | Passed | Case-level outputs and Rule IDs saved |
| Binary Decision Tree | Passed | Train-only tuning and model artifacts saved |
| E1-E4 | Passed | Shared validation IDs and out-of-fold predictions verified |
| Comparative metrics | Passed | Metrics, confusion matrices, and paired results saved |
| Error analysis | Passed at data level | Disagreement and misclassification cases identified |
| Label provenance document | Open | Administrative source must be documented in the thesis |
| Operational rubric | Open | Qualitative comparison still requires explicit evidence |
| Active Chapter IV | Failed | Legacy methodology and results remain in LaTeX |

## 2. Result Audit

- E1: both methods achieve 100% accuracy on 20 test invoices.
- E2: Decision Tree accuracy is 96.67%; Rule-Based is 93.33%.
- E3: Decision Tree accuracy is 95.96%; Rule-Based is 93.94%.
- E4: Decision Tree accuracy is 97.98%; Rule-Based is 93.94%.
- E4 urgent recall: Decision Tree 96.67%; Rule-Based 80.00%.
- E4 exact McNemar: `p = 0.2891`.

Decision Tree is descriptively stronger in E2-E4, but the paired difference is not statistically significant. A claim of universal superiority would fail the audit.

## 3. Required Chapter Repair

Remove or replace:

- Guideline-Based Ground Truth;
- `HIGH`, `MEDIUM`, and `NORMAL` as result classes;
- legacy perfect confusion matrices;
- Decision Tree reconstruction claims;
- Knowledge Representation Consistency as the main analysis; and
- conclusions derived from the old experiment.

Retain Knowledge Acquisition and Rule Construction only as support for the SOP-derived Rule-Based method.

## 4. Quality Gate

- [x] Both methods evaluated on identical cases.
- [x] E1-E4 reported.
- [x] LOOCV metrics aggregated from held-out predictions.
- [x] False positives and false negatives identified.
- [x] Decision Tree complexity and importance recorded.
- [x] Feature importance kept non-causal.
- [ ] Ground-truth provenance evidenced in the thesis.
- [ ] SOP-to-rule traceability evidenced.
- [ ] Comparative operational rubric completed.
- [ ] Chapter IV rewritten with complete LaTeX tables.
- [ ] Figure placeholders linked to `Figure-Prompts.md`.
- [ ] Thesis compiled and visually checked.

## 5. Final Conclusion

The empirical redesign has passed reproducibility and leakage checks. The remaining work is chapter integration, provenance documentation, qualitative comparison, and final LaTeX validation.
