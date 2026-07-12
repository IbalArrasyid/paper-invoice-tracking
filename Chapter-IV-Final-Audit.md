# Chapter IV Final Scientific Audit

## Executive Summary

Chapter IV now substantially supports the constitutional positioning in `Research-Positioning-Statement.md`. The chapter no longer reads primarily as Machine Learning evaluation. Its dominant logic is Knowledge Engineering: operational knowledge is acquired, formalized, represented explicitly through Rule-Based rules, reconstructed statistically through Decision Tree C4.5, and evaluated as Knowledge Representation Consistency.

The audit identified minor weaknesses after the previous revision: the novelty signal could be more visible inside Chapter IV, the Knowledge Compression discussion needed clearer explanation of abstraction and attribute redundancy, and the Information Systems transition from evaluated knowledge to Invoice Tracking and POD context needed strengthening. These weaknesses were corrected in `Hasil-dan-Pembahasan.tex`.

No experiment artifacts, datasets, figures, metrics, tables, or models were modified.

## Scores

| Dimension | Score | Interpretation |
|---|---:|---|
| Scientific Score | 92/100 | Strong alignment with the constitutional research position; remaining limitations are mostly presentation-level and figure-quality issues. |
| Knowledge Engineering Score | 94/100 | Operational Knowledge Formalization Framework is now explicit and central. |
| Information Systems Score | 86/100 | System embedding is present and improved, but Chapter IV still remains more knowledge-evaluation focused than system-design focused. |
| Decision Support Score | 88/100 | Priority recommendation is clearly positioned as operational decision support, not autonomous prediction. |
| Machine Learning Framing Score | 9/100 | Residual ML-first framing risk is low; metric tables remain only as official consistency evidence. Lower is better for this score. |

## Step 1: Scientific Audit by Subsection

| Subsection | Scientific question answered | Contribution supported | Strengthens Operational Knowledge Formalization Framework? | Returns to ML competition? |
|---|---|---|---|---|
| 4.1 Karakteristik Dataset | What operational knowledge artifact is being evaluated? | Operational Dataset and Guideline-Based Ground Truth. | YES. It explains dataset as formalized operational knowledge. | NO. Statistics are contextual, not dominant. |
| 4.2 Representasi Pengetahuan Rule-Based | How is formalized knowledge explicitly represented? | Rule-Based Representation and rule traceability. | YES. Rule Base is tied to Operational Labeling Guideline. | NO. Metrics appear last as consistency evidence. |
| 4.3 Rekonstruksi Pengetahuan Decision Tree C4.5 | How is the same knowledge statistically reconstructed? | Decision Tree Reconstruction and feature dominance. | YES. C4.5 is framed as reconstruction from formalized attributes. | NO. Metrics are treated as consistency evidence, not ranking evidence. |
| 4.4 Analisis Representasi Komparatif | How do explicit representation and statistical reconstruction differ? | Knowledge Representation Consistency Evaluation. | YES. The comparison is conceptual and representational. | NO. Metrics are explicitly supporting evidence only. |
| 4.5 Knowledge Representation Perspective | What is the core scientific meaning of Chapter IV? | Operational Knowledge Formalization Framework. | YES. This is the central contribution section. | NO. It rejects ranking logic. |
| 4.5.1 Knowledge Compression | Why can 12 rules become seven major tree paths? | Knowledge Compression and abstraction. | YES. It explains simplification, abstraction, dominant concepts, and redundancy. | NO. It is about representation form, not performance. |
| 4.5.2 Pemetaan Jalur Rekonstruksi terhadap Rule Base | Do tree paths preserve rule meaning? | Rule mapping and reconstruction alignment. | YES. It maps DTR paths to formalized rules. | NO. It does not add new algorithmic claims. |
| 4.5.3 Konsistensi Representasi Pengetahuan | Do both representations preserve the same operational meaning? | Knowledge Representation Consistency. | YES. It links outputs to Guideline-Based Ground Truth. | NO. It bounds interpretation to the final dataset. |
| 4.6 Diskusi | What are the scientific and practical implications? | Knowledge Engineering and Decision Support System contribution. | YES. It centers Operational Knowledge Formalization Framework. | NO. It treats metrics as supporting evidence. |
| 4.7 Threats to Validity | What claims are bounded? | Scientific validity and limitation framing. | YES. It protects the framework from overclaiming. | NO. It explicitly avoids prediction-generalization claims. |

## Step 2: Narrative Audit

Potential ML-evaluation signals were reviewed:

| Occurrence | Audit result | Action |
|---|---|---|
| Confusion matrix figures | Official artifacts; acceptable if interpreted as consistency evidence. | Kept and reframed in prose. |
| Metric table with 1,000 values | Official artifact; acceptable only as supporting evidence. | Kept and explicitly bounded. |
| Terms such as accuracy, precision, recall, F1-score | Necessary because official experiment reports contain these metrics. | Interpreted as consistency with Guideline-Based Ground Truth. |
| Prediction column names in official artifacts | Dataset/report terminology; not rewritten because artifacts are official. | Conceptual prose uses representation, reconstruction, consistency, and recommendation. |
| "Model" wording | Acceptable when referring to artifacts, but not as the contribution center. | Contribution center remains Operational Knowledge Formalization Framework. |

No remaining paragraph requires revision for ML-competition framing.

## Step 3: Knowledge Engineering Audit

Required flow:

```text
Knowledge Acquisition
-> Knowledge Formalization
-> Operational Labeling Guideline
-> Rule-Based Representation
-> Decision Tree Reconstruction
-> Knowledge Representation Consistency
-> Invoice Tracking and POD System
```

Audit result:

- Knowledge Acquisition is visible in Sections 4.1, 4.5, and 4.6.
- Knowledge Formalization is visible in Sections 4.1, 4.3, 4.5, and 4.6.
- Operational Labeling Guideline is linked to Guideline-Based Ground Truth.
- Rule-Based Representation is explicitly positioned in Section 4.2.
- Decision Tree Reconstruction is explicitly positioned in Section 4.3.
- Knowledge Representation Consistency is now the interpretive basis of Sections 4.4 and 4.5.3.
- Invoice Tracking and POD System embedding is strengthened in Section 4.6.

Weak transition found and corrected:

- The connection from evaluated knowledge to the Invoice Tracking and POD system was previously present but underdeveloped. A paragraph was added in the discussion to explain system embedding.

## Step 4: Knowledge Compression Audit

The Knowledge Compression discussion now explains why 12 operational rules can be reconstructed into seven major decision paths:

- Some rules have similar operational effects after projection into formal attributes.
- C4.5 abstracts multiple administrative conditions through dominant attributes.
- Dominant operational concepts are cut-off distance, receiving-day information, and receiving-schedule limitation.
- Attribute redundancy explains why some operationally meaningful features receive zero importance in the final tree.

Audit result: satisfactory after revision.

## Step 5: Comparative Perspective Audit

The comparison section no longer treats Rule-Based and Decision Tree as competitors. It compares:

- Explicit Knowledge Representation through Rule Base.
- Statistical Knowledge Reconstruction through C4.5.
- Source of knowledge.
- Transparency.
- Interpretability.
- Maintainability.
- Representation mechanism.
- Operational meaning.

Performance metrics remain only as supporting evidence of consistency against Guideline-Based Ground Truth.

Audit result: satisfactory after revision.

## Step 6: Threats to Validity Audit

Required limitations are present:

| Required limitation | Present? | Location |
|---|---|---|
| Guideline-Based Ground Truth | YES | Validitas Internal and Keterbatasan Guideline-Based Labeling |
| Limited operational scope | YES | Keterbatasan Ruang Lingkup Pengetahuan |
| Limited organizational scope | YES | Validitas Eksternal |
| Knowledge boundedness | YES | Keterbatasan Ruang Lingkup Pengetahuan |
| Absence of external validation | YES | Validitas Eksternal and Guideline-Based Labeling limitation |
| Small dataset | YES | Keterbatasan Dataset |
| Representation consistency rather than prediction | YES | Validitas Internal, Guideline-Based Labeling limitation |

Audit result: strengthened and satisfactory.

## Step 7: Novelty Audit

Before the final targeted revision, Chapter IV implied the contribution but did not state novelty strongly enough inside the core section. A new paragraph was added to Section 4.5 explaining that novelty lies in transforming operational knowledge into two interpretable representations whose consistency can be evaluated.

Audit result: a reader can now identify the thesis novelty from Chapter IV without reading Chapter I.

## Step 8: Conceptual Flow Audit

Desired flow:

```text
Operational Knowledge
-> Knowledge Acquisition
-> Knowledge Formalization
-> Knowledge Representation
-> Knowledge Reconstruction
-> Representation Consistency
-> Decision Support
```

Current Chapter IV follows this flow. It does not follow the weaker pattern:

```text
Dataset
-> Training
-> Accuracy
-> Conclusion
```

Audit result: satisfactory after targeted edits.

## Step 9: Scientific Language Audit

Language scan result:

- Avoided legacy model-ranking vocabulary and classifier-first framing.
- Preferred terms now dominate: consistent, traceable, interpretable, formalized, represented, reconstructed, operationally meaningful, representation consistency.
- Metric language remains only where required by official tables and is interpretively bounded.

Audit result: satisfactory.

## Step 10: Revision Performed

The following targeted revisions were made to `Hasil-dan-Pembahasan.tex`:

| Location | Paragraph modified | Scientific rationale |
|---|---|---|
| Section 4.5 opening | Added novelty paragraph | Makes the Operational Knowledge Formalization Framework identifiable from Chapter IV itself. |
| Section 4.5.1 Knowledge Compression | Added abstraction/redundancy paragraph | Explains knowledge simplification, abstraction, dominant concepts, and attribute redundancy. |
| Section 4.6 Discussion | Added system-embedding paragraph | Connects evaluated knowledge to Invoice Tracking and POD decision-support context. |
| Section 4.7 Threats to Validity | Added `Keterbatasan Ruang Lingkup Pengetahuan` subsection | Makes knowledge boundedness and operational scope explicit. |

No official experiment values were changed.

## Strengths

- Chapter IV now clearly supports the Operational Knowledge Formalization Framework.
- Rule-Based is consistently positioned as explicit representation.
- Decision Tree C4.5 is consistently positioned as statistical reconstruction.
- Knowledge Compression is explained beyond tree-size reduction.
- Metrics are interpreted as consistency evidence, not model ranking.
- Threats to validity are candid and scientifically bounded.

## Weaknesses

- The conceptual reconstruction figure remains a placeholder and still uses a simple linear layout. It should later be replaced with a professionally designed figure, but the artifact was not modified in this audit.
- The comparison table remains serviceable but could eventually be refined further to use fully constitutional terminology in every row.
- The Rule Mapping table is based on existing Chapter IV mappings and exported tree paths; no separate official mapping audit file was found in `final_experiment/`.

## Paragraphs Modified

1. Added one paragraph in Section 4.5 to state novelty explicitly.
2. Added one paragraph in Section 4.5.1 to explain simplification, abstraction, and attribute redundancy.
3. Added one paragraph in Section 4.6 to connect evaluated knowledge to the Invoice Tracking and POD Information System.
4. Added two paragraphs under a new validity subsection, `Keterbatasan Ruang Lingkup Pengetahuan`.

## Scientific Rationale

The revisions were necessary because Chapter IV must convince the reader that the thesis contribution is not Decision Tree performance. The chapter now demonstrates that operational knowledge is transformed through formalization into interpretable artifacts, represented explicitly by Rule-Based rules, reconstructed statistically by C4.5, and evaluated through consistency of operational meaning.

## Remaining Limitations

- External validation on another organization or future operational period remains absent.
- Dataset size remains limited to 105 invoices.
- Guideline-Based Ground Truth remains guideline-derived rather than independently validated.
- Knowledge scope remains bounded to the customer rules, schedules, and operational conditions acquired in the study context.
- The figure placeholder should be redesigned later for final presentation quality.

## Final Recommendation

- [x] Ready for Chapter III Revision
- [ ] Needs Minor Revision
- [ ] Needs Major Revision
