# Research Framework Blueprint

## Framework Identity

**Primary figure message:** Comparative Analysis of Rule-Based and Decision Tree Methods for Invoice Urgency Classification.

**Ground truth:** Company Administrator Decision.

**Target classes:** `Urgent` and `Not Urgent`.

**Supporting Knowledge Engineering role:** Knowledge Acquisition and Rule Construction for the Rule-Based branch.

This document specifies the conceptual structure of the revised research framework. It does not draw the figure. The final figure must be prepared professionally using the corresponding prompt in `Figure-Prompts.md`.

## 1. Scientific Objective of the Figure

The figure must communicate that this thesis performs an independent comparative evaluation of two interpretable classification methods. Rule-Based classification is constructed from company SOP through Knowledge Acquisition and Rule Construction. Decision Tree classification is trained from historical invoice attributes and administrator labels. Both methods are evaluated against the same administrator ground truth and analyzed through multiple validation scenarios, performance metrics, error patterns, and operational characteristics.

Within ten seconds, a reader must understand:

1. The target is binary invoice urgency: `Urgent` or `Not Urgent`.
2. Administrator decisions are the shared ground truth.
3. Rule-Based and Decision Tree are two methods being compared.
4. Knowledge Engineering supports only the Rule-Based construction process.
5. Comparative Analysis is the core scientific contribution.
6. The invoice tracking and POD system is the deployment context.

The figure must not imply that guideline-derived labels are ground truth, that Decision Tree reconstructs Rule-Based knowledge, or that the Operational Knowledge Formalization Framework remains the primary contribution.

## 2. Conceptual Flow

The final figure should present the following sequence step by step:

1. Historical Invoice Data and Company SOP are shown as two distinct input sources.
2. Historical Invoice Data enters Data Collection and Administrator Ground-Truth Verification.
3. Verified invoice data proceeds through Data Cleaning and Feature Engineering.
4. The prepared dataset and verified administrator labels enter Experimental Scenario Construction.
5. Company SOP enters Knowledge Acquisition, Rule Construction, and Rule Validation.
6. The validated Rule Base produces Rule-Based Classification for each required validation case.
7. Training data and administrator labels produce Decision Tree Training and Pruning.
8. The trained Decision Tree produces Decision Tree Prediction for the same validation cases.
9. Rule-Based and Decision Tree outputs are each compared with Administrator Ground Truth.
10. Results from both methods enter Comparative Performance Evaluation.
11. Case-level predictions enter Error and Misclassification Analysis.
12. Method artifacts and procedures enter Comparative Characteristics Analysis.
13. All comparative evidence converges in Comparative Analysis.
14. The comparative conclusion informs Invoice Tracking and POD System Implementation.
15. The system presents an Urgency Recommendation while retaining administrator authority.

The visual flow must show one data-preparation path, one SOP-based Rule-Based branch, one supervised Decision Tree branch, and one shared comparative-analysis convergence.

## 3. Box Specifications

### Box 1: Historical Invoice Data

- **Title:** Historical Invoice Data
- **Purpose:** Provide the empirical invoice cases and predictor attributes used by the revised study.
- **Inputs:** Historical company invoice records.
- **Outputs:** Candidate invoice records for verification and cleaning.

### Box 2: Company SOP

- **Title:** Company SOP
- **Purpose:** Provide the authoritative operational source for constructing Rule-Based urgency logic.
- **Inputs:** Company procedures, documented urgency conditions, thresholds, exceptions, and rule precedence.
- **Outputs:** Source knowledge for Knowledge Acquisition.

### Box 3: Data Collection

- **Title:** Data Collection
- **Purpose:** Select the intended historical invoice cases and collect the attributes and administrator decisions required by the study.
- **Inputs:** Historical Invoice Data.
- **Outputs:** Collected invoice dataset with candidate features and labels.

### Box 4: Administrator Ground-Truth Verification

- **Title:** Administrator Ground-Truth Verification
- **Purpose:** Confirm that each included invoice has an original administrator decision and that labels use only `Urgent` and `Not Urgent`.
- **Inputs:** Collected invoice records and recorded administrator decisions.
- **Outputs:** Verified Administrator Ground Truth and a label-quality audit.

### Box 5: Data Cleaning

- **Title:** Data Cleaning
- **Purpose:** Resolve documented data-quality issues without changing the substantive meaning of administrator decisions.
- **Inputs:** Collected invoice dataset and label-quality audit.
- **Outputs:** Cleaned invoice dataset, duplicate report, missing-value report, and retained-case list.

### Box 6: Feature Engineering

- **Title:** Feature Engineering
- **Purpose:** Transform operational invoice attributes into model-ready predictors available at decision time.
- **Inputs:** Cleaned invoice dataset.
- **Outputs:** Analysis-ready feature matrix and feature-definition table.

### Box 7: Experimental Scenario Construction

- **Title:** Experimental Scenario Construction
- **Purpose:** Create reproducible and shared validation cases for both methods.
- **Inputs:** Feature matrix, Administrator Ground Truth, fixed seeds, and validation specifications.
- **Outputs:** E1 80:20 split, E2 70:30 split, E3 5-fold partitions, E4 LOOCV partitions, and case identifiers.

### Box 8: Knowledge Acquisition

- **Title:** Knowledge Acquisition from SOP
- **Purpose:** Extract explicit urgency conditions, thresholds, exceptions, and precedence from the company SOP.
- **Inputs:** Company SOP.
- **Outputs:** Structured urgency knowledge and source traceability.

### Box 9: Rule Construction

- **Title:** Rule Construction
- **Purpose:** Transform acquired SOP knowledge into executable binary IF-THEN rules.
- **Inputs:** Structured urgency knowledge and model-ready operational attributes.
- **Outputs:** Draft Rule Base with `Urgent` or `Not Urgent` consequences.

### Box 10: Rule Validation

- **Title:** Rule Validation
- **Purpose:** Verify rule wording, SOP traceability, precedence, conflict handling, default behavior, and coverage before final evaluation.
- **Inputs:** Draft Rule Base and SOP traceability records.
- **Outputs:** Frozen and validated Rule Base.

### Box 11: Rule-Based Classification

- **Title:** Rule-Based Classification
- **Purpose:** Apply the frozen Rule Base to each validation invoice and produce a traceable binary classification.
- **Inputs:** Validation-case features and validated Rule Base.
- **Outputs:** Rule-Based prediction, activated Rule ID, and decision explanation.

### Box 12: Decision Tree Training and Pruning

- **Title:** Decision Tree Training and Pruning
- **Purpose:** Learn a supervised binary classifier from each training partition while controlling overfitting.
- **Inputs:** Training-case features, training-case administrator labels, and train-only parameter-selection procedure.
- **Outputs:** Trained and pruned Decision Tree for each experimental iteration.

### Box 13: Decision Tree Prediction

- **Title:** Decision Tree Prediction
- **Purpose:** Generate binary predictions for validation cases not used as final test labels during model fitting.
- **Inputs:** Trained Decision Tree and validation-case features.
- **Outputs:** Decision Tree prediction, decision path, and model interpretation evidence.

### Box 14: Administrator Ground Truth

- **Title:** Administrator Ground Truth
- **Purpose:** Serve as the shared empirical reference for evaluating both methods.
- **Inputs:** Verified historical administrator decisions.
- **Outputs:** Reference label for each evaluated invoice.

### Box 15: Comparative Performance Evaluation

- **Title:** Comparative Performance Evaluation
- **Purpose:** Compare both methods quantitatively on identical validation cases.
- **Inputs:** Rule-Based predictions, Decision Tree predictions, Administrator Ground Truth, and experiment identifiers.
- **Outputs:** Confusion matrices, accuracy, precision, recall, F1-score, false-positive counts, false-negative counts, and scenario-level stability evidence.

### Box 16: Error and Misclassification Analysis

- **Title:** Error and Misclassification Analysis
- **Purpose:** Explain where the methods agree, disagree, or fail and identify operational error patterns.
- **Inputs:** Case-level predictions, ground truth, rule traces, tree paths, and invoice attributes.
- **Outputs:** Error groups, misclassification case studies, and operational interpretations.

### Box 17: Comparative Characteristics Analysis

- **Title:** Comparative Characteristics Analysis
- **Purpose:** Compare non-metric properties using documented evidence rather than unsupported assertions.
- **Inputs:** Rule Base, Decision Tree artifacts, maintenance procedures, runtime measurements where available, and SOP traceability.
- **Outputs:** Comparison of explainability, adaptability, maintainability, scalability, computational cost, ease of updating, and SOP compliance.

### Box 18: Comparative Analysis

- **Title:** Comparative Analysis
- **Purpose:** Integrate performance, stability, error, and operational-characteristic evidence into the thesis's main scientific findings.
- **Inputs:** Comparative Performance Evaluation, Error and Misclassification Analysis, and Comparative Characteristics Analysis.
- **Outputs:** Evidence-based comparative findings, bounded conclusions, and implementation considerations.

### Box 19: Invoice Tracking and POD System

- **Title:** Invoice Tracking and POD System
- **Purpose:** Provide the operational context in which the selected or justified classification approach supports invoice handling.
- **Inputs:** Comparative findings, system requirements, invoice workflow, and POD workflow.
- **Outputs:** System-integrated urgency support and traceable decision information.

### Box 20: Urgency Recommendation

- **Title:** Urgency Recommendation
- **Purpose:** Present `Urgent` or `Not Urgent` as decision support without replacing administrator responsibility.
- **Inputs:** Implemented classification logic and current invoice attributes.
- **Outputs:** User-facing urgency recommendation and explanation.

## 4. Arrow Specifications

| Origin | Destination | Why the connection exists |
|---|---|---|
| Historical Invoice Data | Data Collection | Historical records supply the empirical cases selected for the study. |
| Data Collection | Administrator Ground-Truth Verification | Collected records must be checked for valid and traceable administrator decisions before modeling. |
| Data Collection | Data Cleaning | Collected predictor data must be checked for missingness, duplication, invalid values, and formatting problems. |
| Administrator Ground-Truth Verification | Administrator Ground Truth | Verification produces the final independent reference labels used in evaluation. |
| Administrator Ground-Truth Verification | Data Cleaning | Label-quality findings determine whether cases must be retained, corrected through documented normalization, or excluded. |
| Data Cleaning | Feature Engineering | Only cleaned records should be transformed into model-ready predictors. |
| Feature Engineering | Experimental Scenario Construction | Validation partitions must be constructed from the finalized analysis features and case identifiers. |
| Administrator Ground Truth | Experimental Scenario Construction | Stratification and train-test labels require the verified binary reference. |
| Company SOP | Knowledge Acquisition from SOP | The SOP is the source of explicit operational urgency knowledge. |
| Knowledge Acquisition from SOP | Rule Construction | Acquired conditions and exceptions must be converted into executable rules. |
| Feature Engineering | Rule Construction | Rules require feature definitions that can operationalize SOP conditions. |
| Rule Construction | Rule Validation | Draft rules must be checked before being frozen for evaluation. |
| Rule Validation | Rule-Based Classification | The classifier must apply only the validated and frozen Rule Base. |
| Experimental Scenario Construction | Rule-Based Classification | Rule-Based predictions must be restricted to the same validation invoices used for Decision Tree evaluation. |
| Experimental Scenario Construction | Decision Tree Training and Pruning | Each scenario determines which invoices may be used for training and validation. |
| Administrator Ground Truth | Decision Tree Training and Pruning | Only labels belonging to the training portion may guide supervised learning. |
| Decision Tree Training and Pruning | Decision Tree Prediction | Each trained tree is applied to its corresponding held-out validation cases. |
| Rule-Based Classification | Comparative Performance Evaluation | Rule-Based outputs must be compared with the shared ground truth. |
| Decision Tree Prediction | Comparative Performance Evaluation | Decision Tree outputs must be compared with the same shared ground truth. |
| Administrator Ground Truth | Comparative Performance Evaluation | The admin label anchors all confusion matrices and performance metrics. |
| Rule-Based Classification | Error and Misclassification Analysis | Activated rules help explain correct and incorrect Rule-Based decisions. |
| Decision Tree Prediction | Error and Misclassification Analysis | Decision paths help explain correct and incorrect Decision Tree decisions. |
| Administrator Ground Truth | Error and Misclassification Analysis | Error type is determined by comparison with the reference decision. |
| Rule Validation | Comparative Characteristics Analysis | Rule structure, traceability, conflicts, and update procedure provide Rule-Based evidence. |
| Decision Tree Training and Pruning | Comparative Characteristics Analysis | Tree complexity, training procedure, feature use, and update procedure provide Decision Tree evidence. |
| Comparative Performance Evaluation | Comparative Analysis | Quantitative differences and stability are part of the central comparison. |
| Error and Misclassification Analysis | Comparative Analysis | Aggregate metrics require case-level explanation to become scientifically meaningful. |
| Comparative Characteristics Analysis | Comparative Analysis | Operational differences complement predictive performance evidence. |
| Comparative Analysis | Invoice Tracking and POD System | The deployment decision must follow the completed comparison. |
| Invoice Tracking and POD System | Urgency Recommendation | The system presents the method output as operational decision support. |

## 5. Hierarchy of Components

### Core Contribution

The central and most visually emphasized component is **Comparative Analysis**. It integrates quantitative performance, stability, error behavior, and operational-characteristic evidence. It must be visually more prominent than either individual method.

### Supporting Processes

Supporting processes prepare valid inputs and construct both methods:

- Historical Invoice Data;
- Company SOP;
- Data Collection;
- Administrator Ground-Truth Verification;
- Data Cleaning;
- Feature Engineering;
- Knowledge Acquisition from SOP;
- Rule Construction;
- Rule Validation; and
- Experimental Scenario Construction.

Knowledge Engineering belongs in this supporting layer.

### Modeling Processes

The two modeling branches are:

- Rule-Based Classification; and
- Decision Tree Training, Pruning, and Prediction.

They should have equal visual weight because the framework evaluates both methods fairly.

### Evaluation Processes

The evaluation layer consists of:

- Administrator Ground Truth;
- Comparative Performance Evaluation;
- Error and Misclassification Analysis; and
- Comparative Characteristics Analysis.

This layer must clearly show that both outputs use the same reference cases and labels.

### Deployment Processes

The deployment layer consists of:

- Invoice Tracking and POD System; and
- Urgency Recommendation.

Deployment should appear after the scientific comparison and should not dominate the framework.

## 6. Visual Layout Recommendation

### Top

Place the figure title at the top center: **Comparative Research Framework for Invoice Urgency Classification**.

Below the title, place two source boxes at equal height:

- Historical Invoice Data on the upper left.
- Company SOP on the upper right.

### Upper Middle

Under Historical Invoice Data, arrange Data Collection, Administrator Ground-Truth Verification, Data Cleaning, and Feature Engineering in a compact vertical sequence.

Under Company SOP, arrange Knowledge Acquisition from SOP, Rule Construction, and Rule Validation in a compact vertical sequence.

Administrator Ground Truth should appear near the center rather than buried in one branch. It must be visually identifiable as the shared reference for both methods.

### Middle

Place Experimental Scenario Construction centrally above the two modeling branches.

Create two equal-width sibling branches:

- Left branch: Rule-Based Classification.
- Right branch: Decision Tree Training and Pruning, followed by Decision Tree Prediction.

Use equal box sizes and balanced spacing. Do not visually suggest that one method is the default or winner.

### Lower Middle

Place three analysis boxes in one balanced row:

- Comparative Performance Evaluation on the left.
- Error and Misclassification Analysis in the center.
- Comparative Characteristics Analysis on the right.

Connect both method outputs and Administrator Ground Truth to the relevant analysis boxes.

### Center Emphasis

Place Comparative Analysis centered below the three analysis boxes. It should be the most prominent box through a slightly stronger border or subtle academic fill, not through decorative styling.

### Bottom

Place Invoice Tracking and POD System below Comparative Analysis. Place Urgency Recommendation at the bottom center.

The bottom layer must remain visually secondary to the comparative-analysis layer.

## 7. Caption Recommendations

1. **Comparative research framework for evaluating Rule-Based and Decision Tree methods for invoice urgency classification using administrator decisions as ground truth.**

2. **Methodological framework for the comparative evaluation of SOP-driven Rule-Based classification and data-driven Decision Tree classification in invoice urgency assessment.**

3. **Research framework integrating administrator-labeled historical data, SOP-based rule construction, multiple validation scenarios, and comparative analysis for invoice urgency classification.**

## 8. Chapter III Narrative

The research framework begins with two independent sources: historical invoice data containing administrator decisions and the company SOP containing explicit operational procedures. Historical data are collected, verified to ensure that the ground-truth labels consist of `Urgent` and `Not Urgent`, cleaned, and transformed into decision-time features. In parallel, Knowledge Acquisition is conducted on the company SOP to construct and validate a frozen Rule Base. Four experimental scenarios define identical validation cases for the Rule-Based and Decision Tree methods. The Rule-Based method applies the validated rules, while the Decision Tree is trained and pruned using only the training portion of each scenario before generating held-out predictions. Both outputs are evaluated against the same administrator ground truth through performance metrics, error and misclassification analysis, and comparison of operational characteristics. The integrated Comparative Analysis forms the central scientific contribution and provides the evidence used to interpret implementation within the invoice tracking and POD system.

## 9. Consistency Check

| Reference | Consistency status | Required interpretation |
|---|---|---|
| `Research-Positioning-Statement.md` | Consistent | Comparative Analysis is primary; administrator labels are ground truth; Knowledge Engineering supports Rule-Based construction. |
| `Narrative-Revision-Plan.md` | Consistent | The flow includes the data-readiness gate, four experiments, error analysis, and Chapter IV as the scientific center. |
| Current Chapter III (`Metodologi.tex`) | Not yet consistent | It still describes the legacy method and must be rewritten from the verified E1-E4 protocol. |
| Current Chapter IV (`Hasil-dan-Pembahasan.tex`) | Not yet consistent | It reports legacy three-class results and must be replaced with the completed comparative evidence. |
| Chapter I and Abstract | Not yet consistent | They still contain the old framework and labels and must later be revised against completed comparative evidence. |
| Chapter V | Not yet consistent | Legacy conclusions must be replaced with answers to the comparative research questions. |

The framework is consistent with the revised planning documents and completed experiment. The active LaTeX thesis remains inconsistent until Chapters III and IV are rewritten.

## 10. Manual Redraw Checklist

- [ ] Use the exact figure title: `Comparative Research Framework for Invoice Urgency Classification`.
- [ ] Show Historical Invoice Data and Company SOP as distinct sources.
- [ ] Show Administrator Ground-Truth Verification before modeling.
- [ ] Use exactly `Administrator Ground Truth` for the shared reference box.
- [ ] Show only `Urgent` and `Not Urgent` as target classes where classes are displayed.
- [ ] Keep Knowledge Acquisition from SOP, Rule Construction, and Rule Validation in the Rule-Based branch.
- [ ] Do not use Operational Knowledge Formalization Framework as the title or central contribution.
- [ ] Do not include Guideline-Based Ground Truth or Operational Labeling Guideline as a label source.
- [ ] Show Experimental Scenario Construction before the two method outputs.
- [ ] Present Rule-Based and Decision Tree branches with equal visual weight.
- [ ] Connect both methods to the same validation cases.
- [ ] Connect Administrator Ground Truth to Decision Tree training only through training partitions.
- [ ] Connect Administrator Ground Truth to the shared evaluation layer.
- [ ] Include Comparative Performance Evaluation.
- [ ] Include Error and Misclassification Analysis.
- [ ] Include Comparative Characteristics Analysis.
- [ ] Make Comparative Analysis the most visually prominent scientific box.
- [ ] Place Invoice Tracking and POD System after Comparative Analysis.
- [ ] Place Urgency Recommendation at the bottom.
- [ ] Avoid wording that claims one method is superior before results are available.
- [ ] Use professional academic typography and sufficient spacing for grayscale printing.
- [ ] Use no icons, gradients, shadows, decorative illustrations, or unnecessary colors.
- [ ] Verify every arrow against the arrow specification in Section 4.
- [ ] Verify that the figure can be understood within ten seconds without reading the chapter text.

## Final Scientific Meaning

The final figure must communicate an independent and reproducible comparative study. The SOP-based Rule-Based method and the admin-label-trained Decision Tree method are evaluated fairly against the same administrator decisions. Knowledge Engineering remains visible because it explains how the Rule-Based classifier is built, but Comparative Analysis is unmistakably the thesis's central contribution.
