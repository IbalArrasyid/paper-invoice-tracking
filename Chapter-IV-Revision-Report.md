# Chapter IV Revision Report

## 1. Subsections Revised

| Chapter IV part | Revision status | Scientific reason |
|---|---|---|
| 4.1 Karakteristik Dataset | Revised | Repositioned the dataset as an operational knowledge artifact produced by Knowledge Acquisition and Knowledge Formalization, not merely as statistical input. |
| 4.2 Representasi Pengetahuan Rule-Based | Revised and retitled | Reframed Rule-Based as explicit operational knowledge representation. Rule traceability and operational transparency now precede metric discussion. |
| 4.3 Rekonstruksi Pengetahuan Decision Tree C4.5 | Revised and retitled | Reframed C4.5 as statistical reconstruction of formalized operational knowledge, with tree structure and feature dominance emphasized before metrics. |
| 4.4 Analisis Representasi Komparatif | Revised and retitled | Changed the comparison from model performance comparison to representation-mechanism comparison. Metrics are now supporting evidence only. |
| 4.5 Knowledge Representation Perspective | Revised, retitled, and expanded | Made this the scientific core of Chapter IV, aligned with the Operational Knowledge Formalization Framework and Knowledge Representation Consistency Evaluation. |
| 4.5.1 Knowledge Compression | Inserted | Added a dedicated explanation of 12 operational rules being reconstructed into seven major Decision Tree paths and grouped into dominant operational knowledge concepts. |
| 4.5.2 Pemetaan Jalur Rekonstruksi terhadap Rule Base | Expanded | Preserved the existing mapping table and expanded its interpretation without adding new mapping rows or invented rule correspondences. |
| 4.5.3 Konsistensi Representasi Pengetahuan | Inserted | Clarified how Rule-Based and C4.5 preserve the same operational meaning against Guideline-Based Ground Truth. |
| 4.6 Diskusi | Revised | Focused discussion on scientific implications and Knowledge Engineering as the primary contribution. |
| 4.7 Threats to Validity | Strengthened | Expanded limitations around Guideline-Based Ground Truth, dataset size, knowledge scope, operational scope, and no external generalization. |

## 2. Paragraphs Removed

- Removed opening prose that treated Chapter IV primarily as an experiment or model-result presentation.
- Removed metric-first Rule-Based explanation.
- Removed metric-first Decision Tree explanation.
- Removed comparative prose that could be read as model-performance competition.
- Removed language that over-centered prediction, model performance, or general classification success.
- Removed discussion phrasing that could imply C4.5 forms operational rules outside the formalized guideline.

No figures, table labels, metrics, datasets, or experiment artifacts were removed.

## 3. Paragraphs Inserted

- Added a Chapter IV opening position in Section 4.1 explaining the dataset as an operational knowledge artifact.
- Added Rule-Based paragraphs emphasizing Rule Base, Operational Labeling Guideline, traceability, transparency, and operational meaning.
- Added Decision Tree paragraphs emphasizing reconstruction, tree paths, feature dominance, and knowledge compression.
- Added comparative-analysis paragraphs explaining knowledge source, representation mechanism, interpretability, maintainability, and operational meaning.
- Added an expanded Knowledge Representation Perspective section.
- Added dedicated paragraphs on Knowledge Compression.
- Added expanded interpretation of DTR1-DTR7 mapping.
- Added strengthened validity paragraphs on Guideline-Based Ground Truth, dataset limitations, operational scope, and external generalization.

## 4. Terminology Changes

| Previous tendency | Revised terminology |
|---|---|
| Ground truth without qualification | Guideline-Based Ground Truth |
| Model performance as primary interpretation | Knowledge Representation Consistency Evaluation |
| Prediction-centered output | Priority recommendation or model output, depending on context |
| Decision Tree learning/discovery | Decision Tree reconstruction |
| Feature importance as causal importance | Feature importance as knowledge dominance or reconstruction attribute dominance |
| Model comparison | Comparative representation analysis |

## 5. Consistency Check Against Research-Positioning-Statement.md

- Chapter IV now treats Knowledge Engineering as the primary contribution.
- Chapter IV centers the Operational Knowledge Formalization Framework.
- Rule-Based is presented as explicit Knowledge Representation.
- Decision Tree C4.5 is presented as Knowledge Reconstruction.
- Evaluation is framed as Knowledge Representation Consistency Evaluation.
- 1,000 metric values are interpreted as consistency with Guideline-Based Ground Truth, not predictive ranking.
- The discussion avoids algorithm-ranking, replacement, and new-rule-formation narratives.
- Feature importance is interpreted as dominance within reconstruction, not causal proof.
- Threats to validity explicitly bound the claims to the studied organization and final dataset.

## 6. Remaining Weaknesses for Manual Review

- The conceptual figure `fig:knowledge_reconstruction` remains a placeholder and still uses a simple linear illustration. It was not modified because the instruction prohibited modifying figures.
- The table `tab:comparison-characteristics` contains some wording that may later benefit from terminology refinement, but its structure was preserved to avoid unnecessary table modification.
- The Rule Mapping table is preserved from the existing Chapter IV. No separate mapping audit report was found under `final_experiment/`; therefore, no new mappings were introduced.
- Full LaTeX compilation was not performed in this pass.
