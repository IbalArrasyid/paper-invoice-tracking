# Thesis Revision Status Review

## 1. Verdict

The revised research design and comparative experiment are complete. The thesis is not ready for submission because the active LaTeX chapters still describe the old guideline-based, three-class study.

## 2. Current Scientific Position

- contribution: comparative analysis of Rule-Based and Decision Tree classification;
- target: `Urgent` and `Not Urgent`;
- reference: the supplied historical labels, treated as administrator decisions;
- Rule-Based source: company SOP;
- Knowledge Engineering role: Knowledge Acquisition and Rule Construction;
- evaluation: E1 80:20, E2 70:30, E3 5-fold CV, and E4 LOOCV; and
- deployment context: invoice tracking and POD system.

## 3. Completed Work

| Work | Status |
|---|---|
| Research positioning and revision roadmap | Complete |
| Research framework and figure prompts | Complete |
| Dataset audit and duplicate handling | Complete |
| Leakage-controlled feature set | Complete |
| Binary Rule-Based predictions | Complete |
| Binary Decision Tree pipeline | Complete |
| E1-E4 case-level predictions | Complete |
| Metrics, paired comparison, and error cases | Complete |
| Reproducible scripts and result files | Complete |

## 4. Verified Dataset

`dataset_invoice.xlsx` contains 101 labeled rows and 99 unique invoices after duplicate handling. The cleaned distribution is 30 `Urgent` and 69 `Not Urgent`.

The source field is named `expert_label`, with `HIGH` normalized to `Urgent` and `NORMAL` to `Not Urgent`. The thesis still needs documentary evidence that this field represents administrator decisions. This limitation must not be hidden.

## 5. Main Finding

Decision Tree performs better descriptively in E2-E4. In LOOCV, its accuracy is 97.98% versus 93.94% for Rule-Based, and its urgent recall is 96.67% versus 80.00%. The exact paired test is not significant (`p = 0.2891`), so the conclusion must remain dataset-specific.

Rule-Based produces no false positives in the full evaluation but misses six urgent invoices. Decision Tree produces one false positive and one false negative in LOOCV.

## 6. Remaining Work

1. Document the administrative provenance and timing of the source labels.
2. Add the complete SOP-to-rule traceability and rule-freezing record.
3. Complete the evidence-based operational comparison rubric.
4. Complete provenance and SOP traceability evidence in `Metodologi.tex`.
5. Rewrite `Hasil-dan-Pembahasan.tex` from the revised results.
6. Align Chapters I, II, V, the abstract, title, and system narrative.
7. Compile and visually audit all tables and figure placeholders.

## 7. Submission Risks

- Reusing old three-class results would invalidate the new comparison.
- Calling `expert_label` an administrator label without evidence invites a provenance challenge.
- Claiming Decision Tree superiority would exceed the non-significant paired evidence.
- Treating E1's 100% result as general performance would ignore split sensitivity.

## 8. Readiness Checklist

- [x] Revised scientific position defined.
- [x] Dataset and features audited.
- [x] E1-E4 completed and validated.
- [x] Comparative results and errors documented.
- [ ] Label provenance documented.
- [ ] SOP traceability completed.
- [ ] Active LaTeX chapters rewritten.
- [ ] Full thesis compiled and audited.

## 9. Next Stage

Continue Chapter IV integration using `Chapter-IV-Blueprint.md` and `Comparative-Experiment-Report.md`. Complete the remaining evidence in Chapter III and do not reuse legacy metrics.
