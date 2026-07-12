# Chapter III Revision Report

## 1. Section-by-Section Revisions

### 3.1 Proposed Method

- Reframed the chapter around the Operational Knowledge Formalization Framework.
- Positioned Rule-Based and Decision Tree C4.5 as components inside the framework, not as the primary contribution.
- Added the conceptual process chain from Knowledge Acquisition to System Integration.
- Inserted LaTeX comments before the current research framework figure explaining exactly how the figure should later be replaced.

### 3.2 Knowledge Acquisition

- Expanded the explanation of knowledge sources: Customer Regulations, Historical Invoice Data, and Expert Operational Knowledge.
- Distinguished explicit knowledge from tacit operational knowledge.
- Clarified why acquisition is necessary before attribute construction, rule construction, or evaluation.

### 3.3 Knowledge Formalization

- Made this the methodological core of Chapter III.
- Split the section into Attribute Formalization and Rule Formalization.
- Explained how operational concepts become operational attributes and dataset structure.
- Explained how the same operational knowledge becomes the Operational Labeling Guideline and Rule Base.

### 3.4 Dataset Construction

- Reframed the dataset as an operational knowledge artifact.
- Added explanation of attribute selection, attribute transformation, decision-time features, and the role of `final_label`.
- Updated feature descriptions to align with the final experiment artifacts, including `days_to_cutoff_decision_time`, `next_receive_day_gap_feature`, and `receive_month_end_flag`.

### 3.5 Guideline-Based Labeling

- Reframed labeling as generation of Guideline-Based Ground Truth.
- Clarified that labels are produced from the Operational Labeling Guideline, not independently observed universal truth.
- Added the relationship between label consistency and knowledge consistency.

### 3.6 Knowledge Representation

- Replaced the separate Rule-Based Model and Decision Tree sections with one Knowledge Representation section.
- Added Rule-Based Representation as explicit representation of the formalized Rule Base.
- Added Decision Tree Reconstruction as statistical reconstruction of the same formalized knowledge.
- Clarified that C4.5 receives operational attributes and Guideline-Based Ground Truth, not the Rule Base itself.

### 3.7 Knowledge Representation Consistency Evaluation

- Replaced Comparative Evaluation with Knowledge Representation Consistency Evaluation.
- Reframed accuracy, precision, recall, and F1-score as indicators of representation consistency against Guideline-Based Ground Truth.
- Added qualitative evaluation dimensions: Rule ID traceability, tree-path mapping, attribute dominance, and validity boundaries.

### 3.8 System Integration

- Replaced System Design framing with System Integration.
- Connected evaluated operational knowledge to Invoice Tracking, POD, Priority Recommendation, and Decision Support.
- Preserved the existing architecture, use case, activity, and ERD figure labels.

## 2. Scientific Rationale

The revision aligns Chapter III with the thesis identity defined in `Research-Positioning-Statement.md`: the research contribution is the Operational Knowledge Formalization Framework. The chapter now explains how operational knowledge is acquired, structured, formalized, represented, reconstructed, and evaluated for consistency.

The methodology no longer reads as a machine-learning pipeline. Decision Tree C4.5 is introduced only after knowledge acquisition, formalization, dataset construction, and guideline-based labeling have been established. This makes C4.5 a reconstruction component rather than the center of the research.

The revision also reduces circularity risk by explicitly stating that Guideline-Based Ground Truth is derived from the Operational Labeling Guideline. This makes the evaluation claim precise: the experiment evaluates consistency between representations of the same formalized operational knowledge.

## 3. Terminology Changes

| Previous wording | Revised wording |
| --- | --- |
| Rule-Based Model | Rule-Based Representation |
| Decision Tree model as data-driven method | Decision Tree Reconstruction |
| Ground Truth | Guideline-Based Ground Truth |
| Comparative Evaluation | Knowledge Representation Consistency Evaluation |
| Prediction/predicted output | Output, reconstruction output, or priority recommendation |
| Dataset for modeling | Operational dataset / operational knowledge artifact |
| Model comparison | Representation consistency evaluation |
| System Design | System Integration |

## 4. Consistency Check Against Research-Positioning-Statement.md

| Requirement | Status | Evidence in Chapter III |
| --- | --- | --- |
| Primary contribution is Operational Knowledge Formalization Framework | Satisfied | Section 3.1 introduces the framework as the chapter foundation. |
| Do not introduce another research paradigm | Satisfied | Chapter III keeps Knowledge Engineering as the central paradigm. |
| Distinguish Attribute Formalization and Rule Formalization | Satisfied | Section 3.3 is split into two dedicated subsections. |
| Treat Rule-Based as explicit knowledge representation | Satisfied | Section 3.6.1 defines Rule-Based Representation as an explicit Rule Base artifact. |
| Treat Decision Tree as knowledge reconstruction | Satisfied | Section 3.6.2 defines C4.5 as Decision Tree Reconstruction. |
| Explain Guideline-Based Ground Truth | Satisfied | Section 3.5 explains label derivation from the Operational Labeling Guideline. |
| Interpret metrics as representation consistency | Satisfied | Section 3.7 explicitly defines the evaluation as consistency against Guideline-Based Ground Truth. |
| Preserve distinction between prediction and recommendation | Satisfied | System-facing outputs are described as priority recommendations. |
| Keep system contribution secondary | Satisfied | System Integration appears after the knowledge framework and evaluation methodology. |
| Do not modify experiments, datasets, figures, or results | Satisfied | No experiment artifact, dataset, result value, or figure file was changed. |

## 5. Experiment Artifact Review

Reviewed the final experiment artifacts under `final_experiment/`, including validation summaries, metric tables, class split table, rule usage statistics, feature importance ranking, confusion matrices, Decision Tree rules, and scientific interpretation report.

Fixed facts preserved in the methodology:

- Final dataset: 105 rows and 105 unique invoice numbers.
- Validation blockers: 0.
- Guideline-Based Ground Truth stored as `final_label`.
- Test split: 21 rows with HIGH, MEDIUM, and NORMAL represented.
- Both representations reached 1.000 agreement metrics in Chapter IV, but Chapter III now frames the evaluation as representation consistency.
- Dominant reconstruction attributes include `days_to_cutoff_decision_time`, `receive_day_code`, `next_receive_day_gap_feature`, and `receive_schedule`.

## 6. Figure Note

The current Chapter III research framework figure still visually reflects the older comparative framing. Following the instruction not to redraw figures, the figure was left intact and LaTeX comments were inserted before it. The comments specify that the later replacement figure should show the two-branch Operational Knowledge Formalization Framework and should replace the visual label "Evaluasi Komparatif" with Knowledge Representation Consistency Evaluation.
