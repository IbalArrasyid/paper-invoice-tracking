# Research Positioning Statement

## 1. Research Identity

This thesis is a comparative classification study in the domain of invoice delivery administration. It evaluates two interpretable methods, Rule-Based classification and Decision Tree classification, against historical decisions made by company administrators.

The operational decision has two classes: `Urgent` and `Not Urgent`. The administrator label is positioned as the independent empirical reference for evaluation. Rule-Based classification is constructed from company Standard Operating Procedures (SOP), while Decision Tree classification is learned from historical invoice data and administrator labels.

Knowledge Engineering remains part of the methodology, but it is not the primary contribution. Its role is limited and explicit: Knowledge Acquisition extracts decision knowledge from the company SOP, and Rule Construction transforms that knowledge into executable IF-THEN rules. The primary scientific contribution is the comparative analysis of the two methods in terms of classification performance, error behavior, interpretability, adaptability, maintainability, computational characteristics, and alignment with operational procedures.

The thesis therefore integrates Machine Learning, Knowledge Engineering, Decision Support Systems, and Information Systems. Machine Learning supplies the Decision Tree method and supervised evaluation logic. Knowledge Engineering supports the construction and validation of the Rule-Based method. The Decision Support System and Information System components provide the application context in which priority recommendations are presented to users.

## 2. Research Problem

The research addresses an operational problem and a methodological problem.

The operational problem is that invoice urgency decisions must consider administrative conditions such as customer regulations, cut-off constraints, receiving schedules, and other recorded invoice characteristics. A decision-support system requires a method that can produce an urgency recommendation while remaining understandable and operationally usable.

The methodological problem is that Rule-Based and Decision Tree classification represent different ways of producing the same binary decision. Rule-Based classification applies knowledge explicitly derived from SOP, whereas Decision Tree classification learns patterns from historical administrator decisions. Their relative strengths and weaknesses cannot be established by comparing them with labels generated from the Rule-Based guideline itself. Such a design would make the reference dependent on one of the evaluated methods and weaken the validity of the comparison.

The revised research therefore uses administrator decisions as ground truth. Both methods must be evaluated on the same invoice cases and against the same independent labels, `Urgent` and `Not Urgent`.

## 3. Scientific Objective

The primary objective is to compare Rule-Based and Decision Tree methods for classifying invoice urgency using company administrator decisions as ground truth.

The specific objectives are:

1. To construct a Rule-Based classifier through Knowledge Acquisition from the company SOP and formal Rule Construction.
2. To train and validate a Decision Tree classifier using historical invoice attributes and administrator labels.
3. To evaluate both methods on identical validation cases using accuracy, precision, recall, F1-score, false positive, and false negative measures.
4. To examine the stability of the comparison through multiple validation scenarios.
5. To analyze differences in error patterns, explainability, adaptability, maintainability, computational cost, ease of updating, and SOP compliance.
6. To determine the appropriate role of each method in an invoice tracking and Proof of Delivery decision-support system.

## 4. Research Questions

The revised research is guided by the following questions:

1. How can company SOP knowledge be acquired and transformed into a Rule-Based classifier for the `Urgent` and `Not Urgent` classes?
2. How does a Decision Tree classifier perform when trained on historical invoice data labeled by company administrators?
3. How do Rule-Based and Decision Tree classifiers compare against administrator ground truth across multiple validation scenarios?
4. What differences appear in their false-positive, false-negative, and invoice-level misclassification patterns?
5. How do the two methods differ in explainability, adaptability, maintainability, scalability, computational cost, ease of updating, and SOP compliance?

If the institutional thesis format requires a statistical hypothesis, the paired prediction comparison may use the following formulation:

- Null hypothesis: there is no statistically detectable difference in the error proportions of Rule-Based and Decision Tree predictions on the same evaluated invoices.
- Alternative hypothesis: there is a statistically detectable difference in the error proportions of Rule-Based and Decision Tree predictions on the same evaluated invoices.

The hypothesis is optional and must not be inserted if the study program does not require hypothesis testing.

## 5. Ground-Truth Position

The administrator label is the ground truth because it is the historical operational decision that both methods attempt to reproduce. It is external to the output of the Rule-Based classifier and is not generated by the Decision Tree.

This position removes the circularity of the previous Guideline-Based Ground Truth design. The company SOP is used to construct Rule-Based logic, not to generate the evaluation labels. Administrator labels are used to train the Decision Tree and to evaluate both methods.

The use of administrator labels does not make the reference infallible. The thesis must still report label completeness, class validity, duplicate handling, and any available information about how the decisions were recorded. If labels were produced by one administrator, the thesis must not claim inter-rater agreement or organizational consensus unless such evidence is available.

The ground-truth classes must remain exactly:

- `Urgent`
- `Not Urgent`

No automatic conversion from `HIGH`, `MEDIUM`, or `NORMAL` is permitted without an explicit, documented mapping approved by the company or thesis supervisor.

## 6. Role of Knowledge Engineering

Knowledge Engineering is retained as a supporting methodology for the Rule-Based branch:

1. Knowledge source identification: identify the company SOP and operational documents used to determine urgency.
2. Knowledge Acquisition: extract relevant conditions, thresholds, exceptions, and decision consequences.
3. Knowledge Structuring: organize the acquired knowledge into decision variables and rule groups.
4. Rule Construction: formulate transparent IF-THEN rules that output `Urgent` or `Not Urgent`.
5. Rule Validation: verify rule wording, precedence, conflict resolution, default handling, and coverage against the documented SOP.
6. Rule-Based Classification: apply the validated rules to invoice cases.

Knowledge Engineering is therefore neither removed nor claimed as the thesis's central framework. The term `Operational Knowledge Formalization Framework` must no longer be presented as the primary contribution, thesis identity, or principal figure title. Knowledge Acquisition and Rule Construction may remain in Chapter II and Chapter III as the scientific basis of the Rule-Based method.

## 7. Role of Rule-Based Classification

Rule-Based classification is the knowledge-driven method. It receives invoice attributes and applies rules derived from the company SOP. Each output must be traceable to the activated rule, including any rule priority or conflict-resolution mechanism.

The rules must be constructed independently of test labels. Administrator labels may be used to evaluate the rules, but the rules must not be repeatedly adjusted to fit test cases. Any revision following operational validation must be documented and completed before final model evaluation.

The Rule-Based analysis must include:

- confusion matrix against administrator ground truth;
- accuracy, precision, recall, and F1-score;
- false-positive and false-negative cases;
- rule activation frequency and rule coverage;
- uncovered cases and default-rule use;
- rule conflicts and conflict resolution;
- traceability to SOP provisions; and
- invoice-level error analysis.

## 8. Role of Decision Tree Classification

Decision Tree is the data-driven supervised method. It learns relationships between invoice attributes and administrator labels using only the training portion of each validation scenario.

All preprocessing steps that learn from data, feature selection decisions based on labels, model parameters, and pruning decisions must be determined without using the final test cases. The final analysis must report the resulting tree depth, number of leaves, pruning configuration, decision paths, and feature importance.

Decision Tree outputs are classifications, not knowledge reconstruction claims. Tree visualization and feature importance support interpretation, but feature importance must not be presented as proof of causality.

## 9. Comparative Experimental Design

Both methods must be evaluated on identical invoice cases. The core scenarios are:

| Experiment | Validation design | Scientific purpose |
|---|---|---|
| E1 | Stratified hold-out 80:20 | Evaluate both methods with a larger training portion for Decision Tree. |
| E2 | Stratified hold-out 70:30 | Examine sensitivity to a smaller Decision Tree training portion and a larger test portion. |
| E3 | Stratified 5-fold cross-validation | Measure performance stability across several train-test partitions. |
| E4 | Leave-One-Out Cross-Validation | Produce out-of-fold predictions while maximizing training data in each Decision Tree iteration. |

The same split or held-out invoice identifiers must be used for both methods in each scenario. Rule-Based does not require model fitting, but its predictions must be restricted to the same validation cases used for Decision Tree evaluation.

For cross-validation and Leave-One-Out Cross-Validation, metrics must be calculated from the aggregated out-of-fold predictions. In particular, per-fold precision, recall, or F1-score must not be averaged from single-observation LOOCV folds.

If a result remains perfect, the robustness procedure must check label leakage, duplicate invoices, features derived from the target decision, accidental use of test labels, and deterministic equivalence between recorded admin decisions and SOP conditions. Additional splits must use documented seeds and must not be selected only because they produce a preferred result.

## 10. Comparative Evaluation Dimensions

The quantitative comparison must include:

- accuracy;
- precision for the `Urgent` class;
- recall for the `Urgent` class;
- F1-score for the `Urgent` class;
- macro-averaged metrics when both classes require balanced interpretation;
- false positives;
- false negatives;
- confusion matrices; and
- stability across validation scenarios.

The qualitative and operational comparison must include clearly defined evidence:

| Dimension | Required evidence |
|---|---|
| Explainability | Rule ID and condition trace for Rule-Based; decision path and threshold trace for Decision Tree. |
| Adaptability | Documented procedure required to accommodate a change in SOP or a change in historical decision patterns. |
| Maintainability | Number and type of rules, parameters, or model artifacts that must be inspected and updated. |
| Scalability | Reasoned or measured behavior when the number of rules, features, or invoice cases increases. |
| Computational cost | Training time where applicable, prediction time, and model or rule artifact size measured in the same environment. |
| Ease of updating | Steps required to revise a rule versus retrain and revalidate a Decision Tree. |
| SOP compliance | Traceable correspondence between Rule-Based conditions and SOP; secondary comparison of Decision Tree paths with SOP concepts. |
| Error pattern | Invoice-level categories explaining where and why each method disagrees with the administrator label. |

These dimensions must not be scored subjectively without a rubric or observable evidence. If a dimension is discussed conceptually rather than measured, the thesis must state that boundary explicitly.

## 11. Research Contributions

### Primary Contribution

The primary contribution is an evidence-based comparative analysis of Rule-Based and Decision Tree classification for invoice urgency using administrator decisions as independent ground truth.

### Supporting Contributions

The supporting contributions are:

1. A documented Knowledge Acquisition and Rule Construction process that transforms company SOP into a Rule-Based classifier.
2. A reproducible experimental design for comparing a deterministic rule method and a supervised Decision Tree on the same invoice cases.
3. An invoice-level error analysis that explains false positives, false negatives, agreements, and disagreements between the two methods.
4. An implementation interpretation for selecting or combining the methods within an invoice tracking and POD system.

The thesis does not claim a new Decision Tree algorithm, a universal urgency model, or a new general-purpose Knowledge Engineering framework.

## 12. Core Methodological Sequence

The method must be narrated in the following order:

1. Data Collection.
2. Administrator Ground-Truth Verification.
3. Data Cleaning.
4. Feature Engineering.
5. Experimental Scenario Construction.
6. Knowledge Acquisition from Company SOP.
7. Rule Construction and Rule Validation.
8. Rule-Based Classification.
9. Decision Tree Training and Pruning.
10. Decision Tree Prediction.
11. Evaluation against Administrator Ground Truth.
12. Comparative Performance Analysis.
13. Error and Misclassification Analysis.
14. Comparative Characteristics Analysis.
15. System Implementation Interpretation.

## 13. Evidence Boundary

The revised experiment uses `dataset_invoice.xlsx`. The source has 101 labeled rows and 99 unique invoices after duplicate handling. The binary distribution is 30 `Urgent` and 69 `Not Urgent` after the authorized normalization `HIGH = Urgent` and `NORMAL = Not Urgent`.

The source field is named `expert_label`. The thesis must provide documentary evidence that it records administrator decisions. Legacy three-class and Guideline-Based results remain superseded and must not be reused.

## 14. Permitted and Prohibited Claims

Permitted claims after evidence is available:

- Rule-Based rules were acquired and constructed from the company SOP.
- Decision Tree was trained using administrator-labeled historical data.
- Both methods were evaluated on identical validation cases.
- One method produced a particular metric or error pattern in a specified validation scenario.
- The methods differ in traceability, updating procedure, or operational behavior when supported by documented evidence.

Prohibited claims:

- Guideline-Based labels are the ground truth of the revised study.
- `HIGH`, `MEDIUM`, and `NORMAL` are the revised target classes.
- Existing perfect metrics remain valid after the change of ground truth.
- Rule-Based rules may be tuned using the final test labels without disclosure.
- Decision Tree feature importance proves causal influence.
- A single hold-out result proves general superiority.
- The findings generalize beyond the studied company and period without external validation.

## 15. Chapter-Level Consistency Rules

1. Chapter I must frame the gap as a lack of independent comparative evidence between SOP-driven Rule-Based classification and admin-label-driven Decision Tree classification.
2. Chapter II must retain Knowledge Acquisition and Rule-Based theory, but it must support rather than dominate the comparative research framing.
3. Chapter III must define administrator labels as ground truth and document data leakage controls, rule independence, pruning, and all validation scenarios.
4. Chapter IV must make Comparative Analysis the central section and include performance, error, stability, and operational-characteristic comparisons.
5. Chapter V must answer the comparative research questions and avoid reusing conclusions from the legacy guideline-based experiment.
6. The website is an implementation context, not the primary scientific contribution.
7. Every reported result must be traceable to the verified administrator-labeled dataset and a documented experimental scenario.

## 16. Defense Position

| Examiner question | Defensible answer |
|---|---|
| Why retain Knowledge Engineering? | It provides the Knowledge Acquisition and Rule Construction process required to derive the Rule-Based classifier from company SOP, but it is no longer claimed as the primary contribution. |
| Why use administrator labels? | They provide a reference independent of both evaluated outputs, avoiding the circularity created when the Rule-Based guideline also generates the ground truth. |
| Why compare these methods? | They represent two operationally relevant approaches: explicit SOP-driven decisions and patterns learned from historical administrator decisions. |
| What if both methods achieve the same performance? | The thesis examines stability across several validation scenarios and compares error cases, traceability, adaptability, maintainability, computational characteristics, and SOP compliance. Equal aggregate metrics do not imply identical behavior. |
| What is the main contribution? | A reproducible and evidence-based comparative analysis of Rule-Based and Decision Tree classification against administrator ground truth in the invoice urgency context. |
| Can the results be generalized? | Only within the studied dataset and organizational context unless future work provides temporal or external validation. |

## 17. Final Constitutional Statement

This thesis compares a Rule-Based classifier constructed through Knowledge Acquisition from company SOP with a Decision Tree classifier trained on historical administrator decisions. Both methods are evaluated against the same binary administrator ground truth, `Urgent` and `Not Urgent`, through multiple validation scenarios. The central contribution is the comparative analysis of performance, stability, error behavior, interpretability, maintainability, adaptability, computational characteristics, and SOP compliance. Knowledge Engineering remains an essential supporting process for Rule Construction, while the invoice tracking and POD system remains the deployment context for the resulting priority recommendation.
