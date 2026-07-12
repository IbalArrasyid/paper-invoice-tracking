# Research Framework Blueprint

## 1. Scientific Objective of the Figure

The figure must communicate that the thesis contribution is the Operational Knowledge Formalization Framework for invoice delivery priority. Its primary message is that operational knowledge is acquired, structured, formalized into attributes and rules, represented explicitly through Rule-Based Representation, reconstructed statistically through Decision Tree C4.5, evaluated through Knowledge Representation Consistency Evaluation, and embedded into an Invoice Tracking and POD System that produces Priority Recommendation.

The figure must not visually suggest that Rule-Based and Decision Tree are competing methods. They must appear as two complementary representations of the same formalized operational knowledge. A reader should understand within 10 seconds that the central contribution is the knowledge-engineering framework, not an algorithm comparison.

## 2. Conceptual Flow

1. Operational Knowledge is the starting point.
2. Knowledge Acquisition extracts relevant operational concepts from customer regulations, historical invoice data, and expert operational knowledge.
3. Knowledge Structuring organizes the acquired knowledge into decision-relevant categories.
4. Knowledge Formalization converts structured knowledge into formal artifacts.
5. Knowledge Formalization splits into two coordinated branches: Attribute Formalization and Rule Formalization.
6. Attribute Formalization produces Operational Attributes and the Operational Dataset.
7. Rule Formalization produces the Operational Labeling Guideline and Rule Base.
8. Operational Dataset and Operational Labeling Guideline converge to produce Guideline-Based Ground Truth.
9. Rule Base and Operational Dataset support Rule-Based Representation.
10. Operational Dataset and Guideline-Based Ground Truth support Decision Tree Reconstruction.
11. Rule-Based Representation and Decision Tree Reconstruction converge as complementary knowledge representations.
12. Knowledge Representation Consistency Evaluation evaluates whether both representations preserve the same operational meaning against Guideline-Based Ground Truth.
13. Evaluated operational knowledge is embedded into the Invoice Tracking and POD System.
14. The system produces Priority Recommendation as decision support for invoice delivery handling.

## 3. Box Specifications

| Box | Title | Purpose | Inputs | Outputs |
| --- | --- | --- | --- | --- |
| B1 | Operational Knowledge | Establish the domain knowledge source before any modeling step. | Customer regulations, invoice administration routines, receiving schedules, cut-off rules, POD workflow, staff prioritization practice. | Initial operational decision concepts and constraints. |
| B2 | Knowledge Acquisition | Collect and extract operational knowledge from explicit and tacit sources. | Operational Knowledge. | Acquired knowledge about cut-off timing, receiving windows, schedule limitations, month-end conditions, and urgency handling. |
| B3 | Knowledge Structuring | Organize acquired knowledge into categories that can be formalized. | Acquired operational concepts and constraints. | Structured knowledge categories such as cut-off rules, receiving schedule rules, administrative timing, and priority conditions. |
| B4 | Knowledge Formalization | Act as the central transformation stage of the framework. | Structured knowledge categories. | Two coordinated formalization branches: Attribute Formalization and Rule Formalization. |
| B5 | Attribute Formalization | Convert operational concepts into computable attributes. | Structured knowledge categories, invoice records, customer rules. | Operational Attributes such as `days_to_cutoff_decision_time`, `receive_day_code`, `receive_schedule`, and `next_receive_day_gap_feature`. |
| B6 | Rule Formalization | Convert operational decision logic into explicit rule structures and labeling procedure. | Structured knowledge categories and formalized attributes. | Operational Labeling Guideline and Rule Base. |
| B7 | Operational Dataset | Store formalized invoice cases as an operational knowledge artifact. | Historical invoice data and Operational Attributes. | Structured dataset containing operational attributes and the `final_label` field for Guideline-Based Ground Truth. |
| B8 | Operational Labeling Guideline | Define how priority labels are generated from formalized operational conditions. | Rule Formalization, operational attributes, priority conditions. | Labeling procedure for HIGH, MEDIUM, and NORMAL. |
| B9 | Rule Base | Represent formalized operational rules in explicit IF-THEN form. | Rule Formalization and Operational Labeling Guideline. | Rule set R1-R12 used by Rule-Based Representation. |
| B10 | Guideline-Based Ground Truth | Provide the reference decision label generated from the formalized guideline. | Operational Dataset and Operational Labeling Guideline. | Reference priority labels implemented as `final_label`. |
| B11 | Rule-Based Representation | Explicitly represent the formalized operational knowledge through the Rule Base. | Rule Base and Operational Dataset. | Rule-Based output, activated Rule ID evidence, and traceable priority recommendation logic. |
| B12 | Decision Tree Reconstruction | Reconstruct the same formalized operational knowledge from attributes and guideline-based labels. | Operational Dataset and Guideline-Based Ground Truth. | Decision tree paths, feature dominance structure, and reconstruction output. |
| B13 | Complementary Knowledge Representations | Visually show that Rule-Based and Decision Tree are parallel representations of the same knowledge. | Rule-Based Representation and Decision Tree Reconstruction. | Two interpretable representation outputs ready for consistency evaluation. |
| B14 | Knowledge Representation Consistency Evaluation | Evaluate whether both representations preserve the same operational meaning. | Rule-Based output, Decision Tree reconstruction output, Guideline-Based Ground Truth, rule-path mapping, feature importance, consistency metrics. | Consistency interpretation, evaluation report, limitations, and evaluated operational knowledge. |
| B15 | Invoice Tracking and POD System | Embed evaluated operational knowledge into the information-system context. | Evaluated operational knowledge, invoice tracking requirements, POD workflow, system design artifacts. | Integrated decision-support functionality in the invoice tracking and POD workflow. |
| B16 | Priority Recommendation | Show the final operational decision-support output. | Invoice Tracking and POD System with embedded evaluated knowledge. | HIGH, MEDIUM, or NORMAL priority recommendation for invoice delivery handling. |

## 4. Arrow Specifications

| Arrow | Connection | Explanation |
| --- | --- | --- |
| A1 | Operational Knowledge to Knowledge Acquisition | The framework begins from operational knowledge because customer rules, receiving schedules, POD procedures, and staff practices exist before any formal model is built. |
| A2 | Knowledge Acquisition to Knowledge Structuring | Acquired knowledge must be organized before it can be transformed into formal attributes or rules. |
| A3 | Knowledge Structuring to Knowledge Formalization | Structured knowledge provides the categories needed for formal transformation into computable and rule-based artifacts. |
| A4 | Knowledge Formalization to Attribute Formalization | One branch of formalization converts operational concepts into attributes suitable for dataset construction and reconstruction analysis. |
| A5 | Knowledge Formalization to Rule Formalization | The other branch converts operational decision logic into explicit rules and a labeling guideline. |
| A6 | Attribute Formalization to Operational Dataset | Formal attributes are applied to historical invoice records to construct the operational dataset. |
| A7 | Rule Formalization to Operational Labeling Guideline | Formalized decision conditions define the procedure for assigning HIGH, MEDIUM, and NORMAL labels. |
| A8 | Rule Formalization to Rule Base | The same formalized rule logic is expressed as explicit IF-THEN operational rules. |
| A9 | Operational Dataset to Guideline-Based Ground Truth | The dataset provides the invoice cases that receive reference labels. |
| A10 | Operational Labeling Guideline to Guideline-Based Ground Truth | The guideline provides the decision procedure that generates the reference labels. |
| A11 | Rule Base to Rule-Based Representation | Rule-Based Representation applies the explicit rules as the knowledge-driven representation of operational priority logic. |
| A12 | Operational Dataset to Rule-Based Representation | Each invoice case supplies the facts that are matched against the Rule Base. |
| A13 | Operational Dataset to Decision Tree Reconstruction | The dataset supplies formalized attributes from which C4.5 reconstructs decision paths. |
| A14 | Guideline-Based Ground Truth to Decision Tree Reconstruction | Guideline-based labels provide the reference decisions from which C4.5 learns the reconstructed structure. |
| A15 | Rule-Based Representation to Complementary Knowledge Representations | Rule-Based contributes the explicit, traceable representation of formalized operational knowledge. |
| A16 | Decision Tree Reconstruction to Complementary Knowledge Representations | Decision Tree contributes the interpretable statistical reconstruction of the same formalized knowledge. |
| A17 | Complementary Knowledge Representations to Knowledge Representation Consistency Evaluation | The evaluation compares representational consistency, not competitive superiority. |
| A18 | Guideline-Based Ground Truth to Knowledge Representation Consistency Evaluation | Guideline-Based Ground Truth is the shared reference used to interpret accuracy, precision, recall, and F1-score as consistency indicators. |
| A19 | Knowledge Representation Consistency Evaluation to Invoice Tracking and POD System | Only evaluated operational knowledge should be embedded into the information-system workflow. |
| A20 | Invoice Tracking and POD System to Priority Recommendation | The system operationalizes the evaluated knowledge as a HIGH, MEDIUM, or NORMAL recommendation for invoice delivery. |

## 5. Hierarchy of Components

### Core Contribution

- Operational Knowledge Formalization Framework.
- Knowledge Formalization as the central transformation stage.
- Attribute Formalization and Rule Formalization as the two core branches.
- Guideline-Based Ground Truth as the reference label artifact.
- Rule-Based Representation and Decision Tree Reconstruction as complementary representations.
- Knowledge Representation Consistency Evaluation as the validation logic for preserved operational meaning.

### Supporting Process

- Operational Knowledge.
- Knowledge Acquisition.
- Knowledge Structuring.
- Operational Dataset.
- Operational Labeling Guideline.
- Rule Base.

These components support the contribution by providing the knowledge sources, structured categories, formal attributes, explicit rules, and reference labels needed by the framework.

### Evaluation Process

- Rule-Based Representation.
- Decision Tree Reconstruction.
- Complementary Knowledge Representations.
- Knowledge Representation Consistency Evaluation.

This part must be visually shown as convergence, not competition. The evaluation asks whether both representations preserve the same operational meaning.

### Deployment Process

- Invoice Tracking and POD System.
- Priority Recommendation.

These components show the information-system and decision-support context. They are important, but they must appear downstream from the framework rather than as the main scientific contribution.

## 6. Visual Layout Recommendation

### Overall Shape

Use a vertical top-to-bottom framework with one clearly labeled central spine and a two-branch middle section. The central title above the figure should be "Operational Knowledge Formalization Framework" so the contribution is immediately visible.

### Top Area

Place "Operational Knowledge" at the top center. Directly below it, place "Knowledge Acquisition" and then "Knowledge Structuring" in the center. This makes the figure start from domain knowledge rather than from methods or models.

### Upper Middle

Place "Knowledge Formalization" at the center as a larger or visually emphasized box. This box is the conceptual pivot of the figure.

### Middle Branches

From "Knowledge Formalization", split into two parallel branches:

- Left branch: "Attribute Formalization" leading to "Operational Dataset".
- Right branch: "Rule Formalization" leading to "Operational Labeling Guideline" and "Rule Base".

The branches should be balanced visually. Do not make one branch look more important than the other.

### Convergence Point

Place "Guideline-Based Ground Truth" below the two branches and centered between them. It should receive input from both "Operational Dataset" and "Operational Labeling Guideline".

### Representation Layer

Below "Guideline-Based Ground Truth", place two boxes side by side:

- Left: "Rule-Based Representation".
- Right: "Decision Tree Reconstruction".

Use equal size, equal color intensity, and equal vertical alignment. Do not use "vs", "comparison", opposing arrows, scoreboards, or any visual separator that implies competition.

The Rule-Based box should also receive a visible input from "Rule Base". The Decision Tree box should receive visible input from "Operational Dataset" and "Guideline-Based Ground Truth".

### Evaluation Layer

Place "Knowledge Representation Consistency Evaluation" below the two representation boxes and centered. Both representation boxes should feed downward into this evaluation box. Guideline-Based Ground Truth should also connect to this box as the reference for consistency evaluation.

### Bottom Area

Place "Invoice Tracking and POD System" below the evaluation box. Place "Priority Recommendation" at the bottom center as the final applied output.

### Visual Emphasis

The most visually prominent label should be "Operational Knowledge Formalization Framework", followed by "Knowledge Formalization" and "Knowledge Representation Consistency Evaluation". Rule-Based and Decision Tree should be visibly secondary to the framework title and should appear as sibling boxes.

## 7. Caption Recommendations

1. "Operational Knowledge Formalization Framework for Invoice Delivery Priority Recommendation."
2. "Conceptual Framework for Representing, Reconstructing, and Evaluating Operational Invoice-Priority Knowledge."
3. "Transformation of Operational Knowledge into Complementary Rule-Based and Decision Tree Representations for Invoice Tracking and POD Decision Support."

## 8. Chapter III Narrative Paragraph

Figure X illustrates the Operational Knowledge Formalization Framework used in this research. The framework begins with operational knowledge derived from customer regulations, historical invoice data, receiving schedules, cut-off constraints, POD workflow, and expert administrative practice. This knowledge is acquired, structured, and formalized through two coordinated branches: Attribute Formalization, which produces the Operational Dataset, and Rule Formalization, which produces the Operational Labeling Guideline and Rule Base. The Operational Dataset and Operational Labeling Guideline then generate the Guideline-Based Ground Truth, which becomes the reference for two complementary representations of the same formalized knowledge: Rule-Based Representation and Decision Tree Reconstruction. Both representations are evaluated through Knowledge Representation Consistency Evaluation to determine whether they preserve the same operational meaning. The evaluated knowledge is then embedded into the Invoice Tracking and POD System to support Priority Recommendation for invoice delivery handling.

## 9. Consistency Check

| Source | Consistency Status | Verification |
| --- | --- | --- |
| Research-Positioning-Statement.md | Fully consistent | The blueprint centers the Operational Knowledge Formalization Framework and treats Rule-Based as explicit representation and Decision Tree as reconstruction. |
| Research-Positioning-Statement.md | Fully consistent | The blueprint includes Knowledge Acquisition, Knowledge Structuring, Attribute Formalization, Rule Formalization, Operational Labeling Guideline, Knowledge Representation, Knowledge Reconstruction, and Knowledge Representation Consistency Evaluation. |
| Narrative-Revision-Plan.md | Fully consistent | The blueprint follows the shift from machine-learning prediction toward knowledge engineering, representation, reconstruction, and evaluation. |
| Narrative-Revision-Plan.md | Fully consistent | The blueprint prevents Rule-Based and Decision Tree from appearing as an algorithm-superiority contest. |
| Chapter III | Fully consistent | The blueprint matches the revised Chapter III sections: Proposed Method, Knowledge Acquisition, Knowledge Formalization, Dataset Construction, Guideline-Based Labeling, Knowledge Representation, Knowledge Representation Consistency Evaluation, and System Integration. |
| Chapter III | Fully consistent | The blueprint operationalizes the LaTeX comment in Chapter III that the current figure should be replaced by a two-branch formalization framework. |
| Chapter IV | Fully consistent | The blueprint supports Chapter IV's interpretation of the dataset as an operational knowledge artifact and metrics as representation consistency. |
| Chapter IV | Fully consistent | The blueprint supports the Chapter IV analysis that Rule-Based is explicit representation, C4.5 is reconstruction, and feature importance reflects reconstruction attribute dominance. |

## 10. Implementation Checklist

Use this checklist when manually redrawing the final figure.

- [ ] The title or top label clearly says "Operational Knowledge Formalization Framework".
- [ ] The figure begins with "Operational Knowledge", not Rule-Based or Decision Tree.
- [ ] "Knowledge Acquisition" appears before "Knowledge Structuring".
- [ ] "Knowledge Structuring" appears before "Knowledge Formalization".
- [ ] "Knowledge Formalization" is visually central and prominent.
- [ ] "Knowledge Formalization" splits into exactly two coordinated branches: Attribute Formalization and Rule Formalization.
- [ ] Attribute Formalization leads to Operational Dataset.
- [ ] Rule Formalization leads to Operational Labeling Guideline.
- [ ] Rule Formalization also leads to Rule Base.
- [ ] Operational Dataset and Operational Labeling Guideline converge into Guideline-Based Ground Truth.
- [ ] Rule Base feeds Rule-Based Representation.
- [ ] Operational Dataset and Guideline-Based Ground Truth feed Decision Tree Reconstruction.
- [ ] Rule-Based Representation and Decision Tree Reconstruction are shown as equal sibling boxes.
- [ ] No "VS", "comparative evaluation", ranking symbol, trophy symbol, or opposing visual metaphor appears between Rule-Based and Decision Tree.
- [ ] Knowledge Representation Consistency Evaluation is placed below the two representation boxes.
- [ ] Rule-Based Representation feeds Knowledge Representation Consistency Evaluation.
- [ ] Decision Tree Reconstruction feeds Knowledge Representation Consistency Evaluation.
- [ ] Guideline-Based Ground Truth also feeds Knowledge Representation Consistency Evaluation as the shared reference.
- [ ] Knowledge Representation Consistency Evaluation leads to Invoice Tracking and POD System.
- [ ] Invoice Tracking and POD System leads to Priority Recommendation.
- [ ] Priority Recommendation is shown as the applied system output, not as the main scientific contribution.
- [ ] The core framework remains readable within 10 seconds.
- [ ] The visual hierarchy makes the framework more prominent than the individual Rule-Based and Decision Tree components.
- [ ] The figure caption uses the terms "Operational Knowledge", "Formalization", "Representation", "Reconstruction", or "Consistency Evaluation".
- [ ] The figure does not imply predictive superiority, model competition, or universal generalization.
- [ ] The figure does not add new datasets, new experiments, new algorithms, or new evaluation results.
- [ ] The final drawing preserves the same scientific meaning as this blueprint.
