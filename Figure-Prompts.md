# Figure Prompts

This file is the registry for figure-generation prompts used by the thesis. Every LaTeX figure placeholder should reference exactly one prompt ID using a comment such as `% Figure Prompt: FP-01`.

Figures must not be generated directly inside the thesis source. Use LaTeX placeholders in chapter files, then use the matching prompt below when the final professional figure is created.

## FP-01

### Figure ID

FP-01

### Figure Title

Operational Knowledge Formalization Framework for Invoice Delivery Priority

### Purpose

This figure should communicate that the thesis contribution is the Operational Knowledge Formalization Framework. It must show that the research starts from operational knowledge, transforms that knowledge through acquisition, structuring, and formalization, produces both attribute-based and rule-based artifacts, evaluates complementary representations for consistency, and embeds the evaluated knowledge into an Invoice Tracking and POD System that produces Priority Recommendation.

The figure must immediately communicate that Rule-Based Representation and Decision Tree Reconstruction are complementary representations of the same formalized operational knowledge, not competing algorithms.

### Visual Layout

Use a vertical top-to-bottom framework with a clear central spine and a two-branch middle section.

Place the main title at the top center: "Operational Knowledge Formalization Framework".

Top center:

- Operational Knowledge.
- Knowledge Acquisition.
- Knowledge Structuring.

Upper middle center:

- Knowledge Formalization as the visually emphasized central transformation box.

Middle left branch:

- Attribute Formalization.
- Operational Dataset.

Middle right branch:

- Rule Formalization.
- Operational Labeling Guideline.
- Rule Base.

Central convergence:

- Guideline-Based Ground Truth, receiving input from Operational Dataset and Operational Labeling Guideline.

Representation layer:

- Rule-Based Representation on the left.
- Decision Tree Reconstruction on the right.

Both representation boxes must be equal in size, equal in visual weight, and aligned horizontally.

Evaluation layer:

- Knowledge Representation Consistency Evaluation centered below the two representation boxes.

Bottom:

- Invoice Tracking and POD System.
- Priority Recommendation.

### Boxes

List every box with exact wording and capitalization:

1. Operational Knowledge Formalization Framework
2. Operational Knowledge
3. Knowledge Acquisition
4. Knowledge Structuring
5. Knowledge Formalization
6. Attribute Formalization
7. Operational Dataset
8. Rule Formalization
9. Operational Labeling Guideline
10. Rule Base
11. Guideline-Based Ground Truth
12. Rule-Based Representation
13. Decision Tree Reconstruction
14. Knowledge Representation Consistency Evaluation
15. Invoice Tracking and POD System
16. Priority Recommendation

### Connections

| Origin | Destination | Meaning |
| --- | --- | --- |
| Operational Knowledge | Knowledge Acquisition | Operational rules, schedules, POD workflow, and staff practice are acquired as knowledge sources. |
| Knowledge Acquisition | Knowledge Structuring | Acquired knowledge is organized into decision-relevant categories. |
| Knowledge Structuring | Knowledge Formalization | Structured knowledge becomes ready for formal transformation. |
| Knowledge Formalization | Attribute Formalization | One formalization branch converts concepts into computable attributes. |
| Knowledge Formalization | Rule Formalization | The other formalization branch converts operational decision logic into explicit rules and labeling procedures. |
| Attribute Formalization | Operational Dataset | Formalized attributes are applied to invoice records. |
| Rule Formalization | Operational Labeling Guideline | Formalized rule logic defines the labeling procedure. |
| Rule Formalization | Rule Base | Formalized rule logic is expressed as IF-THEN operational rules. |
| Operational Dataset | Guideline-Based Ground Truth | Invoice cases receive reference labels. |
| Operational Labeling Guideline | Guideline-Based Ground Truth | The guideline determines how HIGH, MEDIUM, and NORMAL labels are assigned. |
| Rule Base | Rule-Based Representation | Explicit rules are applied as knowledge representation. |
| Operational Dataset | Rule-Based Representation | Invoice facts are matched against the Rule Base. |
| Operational Dataset | Decision Tree Reconstruction | Formalized attributes provide the data for reconstruction. |
| Guideline-Based Ground Truth | Decision Tree Reconstruction | Guideline-based labels provide the reference decisions for reconstruction. |
| Rule-Based Representation | Knowledge Representation Consistency Evaluation | Explicit representation output is evaluated for consistency. |
| Decision Tree Reconstruction | Knowledge Representation Consistency Evaluation | Reconstructed representation output is evaluated for consistency. |
| Guideline-Based Ground Truth | Knowledge Representation Consistency Evaluation | The shared reference label anchors the consistency evaluation. |
| Knowledge Representation Consistency Evaluation | Invoice Tracking and POD System | Evaluated operational knowledge is embedded into the system context. |
| Invoice Tracking and POD System | Priority Recommendation | The system produces the operational decision-support output. |

### Visual Style

IEEE paper style, minimalist, professional, white background, rounded rectangles, thin black arrows, balanced spacing, flat design, no icons, no gradients, no shadows, publication quality.

Use consistent typography with compact academic labels. Make "Operational Knowledge Formalization Framework" the most visible phrase. Avoid any symbol, separator, or layout that implies Rule-Based versus Decision Tree competition.

### Color Recommendation

Use subtle academic colors only if needed:

- Light blue for knowledge acquisition and structuring.
- Light gray for formalization processes.
- Light green for artifacts such as Operational Dataset, Rule Base, and Guideline-Based Ground Truth.
- Light amber for consistency evaluation.
- Very light purple or neutral gray for system integration.

Keep colors low saturation and ensure the figure remains readable in grayscale.

### Image Generation Prompt

Create a professional IEEE-style academic framework figure titled "Operational Knowledge Formalization Framework". Use a clean white background, minimalist flat design, rounded rectangles, thin black arrows, balanced spacing, no icons, no gradients, and no shadows. Arrange the figure vertically from top to bottom. At the top center place "Operational Knowledge", followed by "Knowledge Acquisition", then "Knowledge Structuring". Place "Knowledge Formalization" in the upper middle as the central emphasized transformation box. From "Knowledge Formalization", split into two balanced parallel branches. The left branch contains "Attribute Formalization" followed by "Operational Dataset". The right branch contains "Rule Formalization" followed by two outputs: "Operational Labeling Guideline" and "Rule Base". Place "Guideline-Based Ground Truth" centered below the two branches, receiving arrows from "Operational Dataset" and "Operational Labeling Guideline". Below that, place two equal sibling boxes: "Rule-Based Representation" on the left and "Decision Tree Reconstruction" on the right. "Rule Base" should connect to "Rule-Based Representation"; "Operational Dataset" and "Guideline-Based Ground Truth" should connect to "Decision Tree Reconstruction". Both representation boxes should feed into a centered box labeled "Knowledge Representation Consistency Evaluation"; "Guideline-Based Ground Truth" should also connect to this evaluation box as the shared reference. Below the evaluation box place "Invoice Tracking and POD System", then at the bottom place "Priority Recommendation". The figure must clearly show that Rule-Based Representation and Decision Tree Reconstruction are complementary representations of the same formalized operational knowledge, not competing methods. Use subtle academic colors only: light blue for acquisition and structuring, light gray for formalization, light green for artifacts, light amber for evaluation, and neutral gray for system integration. Ensure all labels are spelled exactly as provided and remain readable in grayscale.

## FP-02

### Figure ID

FP-02

### Figure Title

Knowledge Reconstruction and Representation Consistency

### Purpose

This figure should explain the Chapter IV scientific interpretation: formalized operational knowledge is represented explicitly through the Rule Base and reconstructed statistically through Decision Tree C4.5. The figure must show that both representation outputs are evaluated against the same Guideline-Based Ground Truth to determine representation consistency.

The figure should support the argument that C4.5 reconstructs and compresses formalized operational knowledge without replacing the Rule Base or creating new operational policy.

### Visual Layout

Use a centered, layered academic layout.

Top center:

- Formalized Operational Knowledge.

Second layer:

- Operational Attributes on the left.
- Rule Base R1-R12 on the right.

Third layer:

- Guideline-Based Ground Truth centered between the branches.

Fourth layer:

- Rule-Based Representation on the left.
- Decision Tree Reconstruction on the right.

Fifth layer:

- Knowledge Representation Consistency Evaluation centered below both representations.

Bottom layer:

- Equivalent Operational Meaning.

The left and right representation boxes must be equal in visual weight. Do not place them as opponents. They should converge into the evaluation box.

### Boxes

List every box with exact wording and capitalization:

1. Formalized Operational Knowledge
2. Operational Attributes
3. Rule Base R1-R12
4. Guideline-Based Ground Truth
5. Rule-Based Representation
6. Decision Tree Reconstruction
7. Knowledge Representation Consistency Evaluation
8. Equivalent Operational Meaning

### Connections

| Origin | Destination | Meaning |
| --- | --- | --- |
| Formalized Operational Knowledge | Operational Attributes | Operational concepts are transformed into structured features. |
| Formalized Operational Knowledge | Rule Base R1-R12 | Operational concepts are transformed into explicit IF-THEN rules. |
| Operational Attributes | Guideline-Based Ground Truth | Attributes provide the case-level basis for guideline-based labeling. |
| Rule Base R1-R12 | Rule-Based Representation | Explicit rules are applied as the knowledge-driven representation. |
| Operational Attributes | Decision Tree Reconstruction | Formal attributes are used by C4.5 to reconstruct decision paths. |
| Guideline-Based Ground Truth | Decision Tree Reconstruction | Guideline-derived labels provide the reference decisions for reconstruction. |
| Guideline-Based Ground Truth | Knowledge Representation Consistency Evaluation | The shared reference label anchors the consistency evaluation. |
| Rule-Based Representation | Knowledge Representation Consistency Evaluation | The explicit representation output is evaluated for consistency. |
| Decision Tree Reconstruction | Knowledge Representation Consistency Evaluation | The reconstructed representation output is evaluated for consistency. |
| Knowledge Representation Consistency Evaluation | Equivalent Operational Meaning | Consistency indicates that both representations preserve the same operational meaning within the studied dataset. |

### Visual Style

IEEE paper style, minimalist, professional, white background, rounded rectangles, thin black arrows, balanced spacing, flat design, no icons, no gradients, no shadows, publication quality.

Use compact labels and leave enough whitespace so the relationship between representation, reconstruction, and consistency evaluation is immediately clear.

### Color Recommendation

Use subtle academic colors only if needed:

- Light gray for Formalized Operational Knowledge.
- Light blue for Operational Attributes.
- Light green for Rule Base R1-R12.
- Light yellow for Guideline-Based Ground Truth.
- Light neutral tones for the two representation boxes.
- Light amber for Knowledge Representation Consistency Evaluation.

Ensure the figure remains readable in grayscale.

### Image Generation Prompt

Create a professional IEEE-style academic figure titled "Knowledge Reconstruction and Representation Consistency". Use a clean white background, minimalist flat design, rounded rectangles, thin black arrows, balanced spacing, no icons, no gradients, and no shadows. Arrange the figure in centered layers from top to bottom. At the top center place "Formalized Operational Knowledge". In the second layer place "Operational Attributes" on the left and "Rule Base R1-R12" on the right. Place "Guideline-Based Ground Truth" centered below these two boxes, with an arrow from "Operational Attributes" to "Guideline-Based Ground Truth". Connect "Formalized Operational Knowledge" to both "Operational Attributes" and "Rule Base R1-R12". In the fourth layer, place two equal sibling boxes: "Rule-Based Representation" on the left and "Decision Tree Reconstruction" on the right. Connect "Rule Base R1-R12" to "Rule-Based Representation". Connect "Operational Attributes" and "Guideline-Based Ground Truth" to "Decision Tree Reconstruction". Below both representation boxes, place a centered box labeled "Knowledge Representation Consistency Evaluation". Connect "Rule-Based Representation", "Decision Tree Reconstruction", and "Guideline-Based Ground Truth" to this evaluation box. At the bottom, place "Equivalent Operational Meaning". Connect "Knowledge Representation Consistency Evaluation" to "Equivalent Operational Meaning". The figure must show that Rule-Based Representation and Decision Tree Reconstruction are complementary representations of the same formalized operational knowledge, not competitors. Use subtle academic colors only and ensure all text remains readable in grayscale.
