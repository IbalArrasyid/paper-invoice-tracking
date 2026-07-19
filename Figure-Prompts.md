# Figure Prompts

## Figure Policy

This file stores the professional design specifications for thesis figures. It does not contain generated figures or diagram code. Every future LaTeX placeholder must reference one prompt ID using a comment such as `% Figure Prompt: FP-01`.

The revised study uses company administrator decisions as ground truth and compares Rule-Based and Decision Tree classification for the binary classes `Urgent` and `Not Urgent`. No prompt may reuse Guideline-Based Ground Truth, `HIGH`, `MEDIUM`, `NORMAL`, Decision Tree Reconstruction, Knowledge Representation Consistency Evaluation, or Operational Knowledge Formalization Framework as the primary contribution.

---

## FP-01

### Figure ID

FP-01

### Figure Title

Comparative Research Framework for Invoice Urgency Classification

### Purpose

Communicate the complete revised methodology at a glance. The figure must show that historical administrator decisions provide the independent ground truth, company SOP provides knowledge for Rule-Based construction, Decision Tree learns from training partitions of the historical data, and both methods are evaluated on the same validation invoices. Comparative Analysis must appear as the primary scientific contribution, while the invoice tracking and POD system must appear as a downstream implementation context.

### Visual Layout

Use a portrait-oriented or moderately tall academic layout.

At the top, place two source boxes at equal height:

- Historical Invoice Data on the left.
- Company SOP on the right.

Under Historical Invoice Data, place Data Collection, Administrator Ground-Truth Verification, Data Cleaning, and Feature Engineering in a vertical sequence. Place Administrator Ground Truth near the visual center as a prominent shared-reference box.

Under Company SOP, place Knowledge Acquisition from SOP, Rule Construction, and Rule Validation in a vertical sequence.

Place Experimental Scenario Construction centrally above the modeling layer.

In the middle, create two equal branches:

- Left: Rule-Based Classification.
- Right: Decision Tree Training and Pruning, followed by Decision Tree Prediction.

In the lower middle, place three boxes in one balanced row:

- Comparative Performance Evaluation on the left.
- Error and Misclassification Analysis in the center.
- Comparative Characteristics Analysis on the right.

Place Comparative Analysis centered below these boxes and emphasize it with a slightly stronger border or subtle fill. At the bottom, place Invoice Tracking and POD System, followed by Urgency Recommendation.

The arrangement must not imply a winner. Rule-Based and Decision Tree must have equal size and visual weight.

### Boxes

Use the following exact wording, capitalization, and conceptual order:

1. Comparative Research Framework for Invoice Urgency Classification
2. Historical Invoice Data
3. Company SOP
4. Data Collection
5. Administrator Ground-Truth Verification
6. Data Cleaning
7. Feature Engineering
8. Administrator Ground Truth
9. Experimental Scenario Construction
10. Knowledge Acquisition from SOP
11. Rule Construction
12. Rule Validation
13. Rule-Based Classification
14. Decision Tree Training and Pruning
15. Decision Tree Prediction
16. Comparative Performance Evaluation
17. Error and Misclassification Analysis
18. Comparative Characteristics Analysis
19. Comparative Analysis
20. Invoice Tracking and POD System
21. Urgency Recommendation

Where space permits, add a small non-box annotation next to Administrator Ground Truth: `Urgent / Not Urgent`.

### Connections

| Origin | Destination | Meaning |
|---|---|---|
| Historical Invoice Data | Data Collection | Historical records provide the empirical study cases. |
| Data Collection | Administrator Ground-Truth Verification | Collected decisions must be verified before use as ground truth. |
| Data Collection | Data Cleaning | Collected invoice attributes require quality control. |
| Administrator Ground-Truth Verification | Administrator Ground Truth | Verification produces the shared binary reference. |
| Administrator Ground-Truth Verification | Data Cleaning | Label-quality findings affect the retained analysis cases. |
| Data Cleaning | Feature Engineering | Cleaned attributes are transformed into model-ready predictors. |
| Feature Engineering | Experimental Scenario Construction | Prepared features are partitioned reproducibly for evaluation. |
| Administrator Ground Truth | Experimental Scenario Construction | Labels support stratification and training-test assignment. |
| Company SOP | Knowledge Acquisition from SOP | The SOP supplies explicit urgency knowledge. |
| Knowledge Acquisition from SOP | Rule Construction | Acquired knowledge is translated into binary IF-THEN rules. |
| Feature Engineering | Rule Construction | Formal features operationalize the SOP conditions. |
| Rule Construction | Rule Validation | Draft rules must be checked and frozen. |
| Rule Validation | Rule-Based Classification | The classifier applies the validated Rule Base. |
| Experimental Scenario Construction | Rule-Based Classification | Rule-Based uses the same validation invoice IDs as Decision Tree. |
| Experimental Scenario Construction | Decision Tree Training and Pruning | Each scenario defines Decision Tree training and validation partitions. |
| Administrator Ground Truth | Decision Tree Training and Pruning | Only training-partition admin labels guide supervised learning. |
| Decision Tree Training and Pruning | Decision Tree Prediction | The trained model predicts held-out validation invoices. |
| Rule-Based Classification | Comparative Performance Evaluation | Rule-Based predictions are evaluated quantitatively. |
| Decision Tree Prediction | Comparative Performance Evaluation | Decision Tree predictions are evaluated quantitatively. |
| Administrator Ground Truth | Comparative Performance Evaluation | Both methods use the same independent reference. |
| Rule-Based Classification | Error and Misclassification Analysis | Rule traces explain case-level outcomes. |
| Decision Tree Prediction | Error and Misclassification Analysis | Tree paths explain case-level outcomes. |
| Administrator Ground Truth | Error and Misclassification Analysis | The reference identifies false positives and false negatives. |
| Rule Validation | Comparative Characteristics Analysis | Rule structure provides evidence on traceability and maintenance. |
| Decision Tree Training and Pruning | Comparative Characteristics Analysis | Model artifacts provide evidence on complexity and updating. |
| Comparative Performance Evaluation | Comparative Analysis | Quantitative results support the central comparison. |
| Error and Misclassification Analysis | Comparative Analysis | Case-level evidence explains aggregate results. |
| Comparative Characteristics Analysis | Comparative Analysis | Operational properties complete the comparison. |
| Comparative Analysis | Invoice Tracking and POD System | Implementation follows the scientific findings. |
| Invoice Tracking and POD System | Urgency Recommendation | The system presents decision support to users. |

### Visual Style

IEEE paper style, minimalist, professional, white background, rounded rectangles with a small corner radius, thin black arrows, balanced spacing, flat design, no icons, no gradients, no shadows, no illustrations, and publication quality. Use one consistent sans-serif font. Keep every label readable at one-column or thesis-page scale. Use solid arrows only and avoid crossing connectors. Ensure strong grayscale legibility.

### Color Recommendation

Color is optional. If used, apply subtle academic colors only:

- light gray-blue for data-preparation boxes;
- very light green for SOP, Knowledge Acquisition, Rule Construction, and Rule Validation;
- neutral light gray for both method boxes;
- pale amber for Administrator Ground Truth and evaluation boxes;
- restrained light blue for Comparative Analysis; and
- white or very light gray for deployment boxes.

Do not use color to imply that either method is superior.

### Image Generation Prompt

Create a publication-quality IEEE-style academic methodology figure titled "Comparative Research Framework for Invoice Urgency Classification". Use a clean white background, minimalist flat design, small-radius rounded rectangles, thin black directional arrows, balanced spacing, one consistent sans-serif font, no icons, no gradients, no shadows, and no decorative illustrations. Ensure all labels remain readable in grayscale and at thesis-page scale. At the top place two equal source boxes: "Historical Invoice Data" on the left and "Company SOP" on the right. Under "Historical Invoice Data", arrange "Data Collection", "Administrator Ground-Truth Verification", "Data Cleaning", and "Feature Engineering" in a clear vertical flow. Place a prominent shared-reference box labeled "Administrator Ground Truth" near the center with a small annotation "Urgent / Not Urgent". Under "Company SOP", arrange "Knowledge Acquisition from SOP", "Rule Construction", and "Rule Validation" vertically. Place "Experimental Scenario Construction" centrally above the modeling layer. In the middle create two equal-width, equal-weight branches: "Rule-Based Classification" on the left, and "Decision Tree Training and Pruning" followed by "Decision Tree Prediction" on the right. Connect the same experimental validation cases to both branches. Connect only training-partition administrator labels to Decision Tree training. In the lower middle place three balanced boxes in one row: "Comparative Performance Evaluation", "Error and Misclassification Analysis", and "Comparative Characteristics Analysis". Connect Rule-Based output, Decision Tree output, and Administrator Ground Truth to the appropriate evaluation boxes. Below these, place a centered and visually emphasized box labeled "Comparative Analysis". At the bottom place "Invoice Tracking and POD System", followed by "Urgency Recommendation". The visual hierarchy must make Comparative Analysis the primary scientific contribution, Knowledge Acquisition and Rule Construction supporting processes for Rule-Based, and the system a downstream deployment context. Do not include Guideline-Based Ground Truth, HIGH, MEDIUM, NORMAL, Decision Tree Reconstruction, Knowledge Representation Consistency Evaluation, Operational Knowledge Formalization Framework, or any visual cue that declares a winner.

---

## FP-02

### Figure ID

FP-02

### Figure Title

Experimental Design and Comparative Analysis Structure

### Purpose

Communicate how the same administrator-labeled invoice cases are used to evaluate Rule-Based and Decision Tree across four validation scenarios. The figure should make reproducibility, paired evaluation, aggregated out-of-fold predictions, and the depth of the Chapter IV comparative analysis immediately visible.

### Visual Layout

Use a landscape-oriented academic layout with four horizontal layers.

At the top center, place Verified Administrator-Labeled Dataset. Directly below it, place four equal scenario boxes in one row:

- E1: Stratified Hold-Out 80:20
- E2: Stratified Hold-Out 70:30
- E3: Stratified 5-Fold Cross-Validation
- E4: Leave-One-Out Cross-Validation

Below the scenario row, place two large equal boxes:

- Rule-Based Predictions on the left.
- Decision Tree Predictions on the right.

Place Administrator Ground Truth as a centered shared-reference box between or directly below the prediction boxes. The visual connection must show that each scenario produces predictions for the same validation invoice IDs from both methods.

In the next layer, place three equal analysis boxes:

- Performance and Stability
- Error and Misclassification Patterns
- Operational Characteristics

At the bottom center, place Comparative Findings for Chapter IV.

### Boxes

Use the following exact wording and capitalization:

1. Experimental Design and Comparative Analysis Structure
2. Verified Administrator-Labeled Dataset
3. E1: Stratified Hold-Out 80:20
4. E2: Stratified Hold-Out 70:30
5. E3: Stratified 5-Fold Cross-Validation
6. E4: Leave-One-Out Cross-Validation
7. Rule-Based Predictions
8. Decision Tree Predictions
9. Administrator Ground Truth
10. Performance and Stability
11. Error and Misclassification Patterns
12. Operational Characteristics
13. Comparative Findings for Chapter IV

Add two short non-box notes:

- `Same Validation Invoice IDs`
- `Urgent / Not Urgent`

### Connections

| Origin | Destination | Meaning |
|---|---|---|
| Verified Administrator-Labeled Dataset | E1: Stratified Hold-Out 80:20 | Create the first reproducible validation scenario. |
| Verified Administrator-Labeled Dataset | E2: Stratified Hold-Out 70:30 | Create the second reproducible validation scenario. |
| Verified Administrator-Labeled Dataset | E3: Stratified 5-Fold Cross-Validation | Create out-of-fold predictions across five folds. |
| Verified Administrator-Labeled Dataset | E4: Leave-One-Out Cross-Validation | Create one held-out prediction for every invoice. |
| Each experiment box | Rule-Based Predictions | Apply the frozen Rule Base to the scenario's validation invoices. |
| Each experiment box | Decision Tree Predictions | Train on the scenario's training invoices and predict its validation invoices. |
| Administrator Ground Truth | Performance and Stability | Anchor metrics and scenario-level comparison. |
| Rule-Based Predictions | Performance and Stability | Supply Rule-Based performance evidence. |
| Decision Tree Predictions | Performance and Stability | Supply Decision Tree performance evidence. |
| Rule-Based Predictions | Error and Misclassification Patterns | Supply rule-trace evidence for case analysis. |
| Decision Tree Predictions | Error and Misclassification Patterns | Supply decision-path evidence for case analysis. |
| Administrator Ground Truth | Error and Misclassification Patterns | Identify false positives, false negatives, and correctness groups. |
| Rule-Based Predictions | Operational Characteristics | Support explainability and rule-maintenance analysis. |
| Decision Tree Predictions | Operational Characteristics | Support model-complexity and retraining analysis. |
| Performance and Stability | Comparative Findings for Chapter IV | Quantitative evidence supports the final comparison. |
| Error and Misclassification Patterns | Comparative Findings for Chapter IV | Case-level evidence explains differences. |
| Operational Characteristics | Comparative Findings for Chapter IV | Operational evidence complements metrics. |

### Visual Style

IEEE paper style, minimalist, professional, white background, small-radius rounded rectangles, thin black arrows, balanced spacing, flat design, no icons, no gradients, no shadows, and publication quality. Keep the four experiment boxes equal in size. Keep Rule-Based and Decision Tree boxes equal in size. Use simple orthogonal connectors without crossings where possible.

### Color Recommendation

Use color only if necessary:

- light gray-blue for the verified dataset;
- four subtle neutral tints for E1-E4 while preserving grayscale differences through borders and labels;
- identical neutral gray for both method boxes;
- pale amber for Administrator Ground Truth;
- very light green for the three analysis boxes; and
- restrained light blue for Comparative Findings for Chapter IV.

### Image Generation Prompt

Create a publication-quality IEEE-style academic figure titled "Experimental Design and Comparative Analysis Structure". Use a landscape layout, clean white background, minimalist flat design, small-radius rounded rectangles, thin black arrows, balanced spacing, one consistent sans-serif font, no icons, no gradients, no shadows, and no decorative elements. At the top center place "Verified Administrator-Labeled Dataset". Below it place four equal scenario boxes in one row: "E1: Stratified Hold-Out 80:20", "E2: Stratified Hold-Out 70:30", "E3: Stratified 5-Fold Cross-Validation", and "E4: Leave-One-Out Cross-Validation". Connect the dataset to all four scenarios. Below the scenario row place two large equal boxes: "Rule-Based Predictions" on the left and "Decision Tree Predictions" on the right. Connect every scenario to both prediction boxes and add a small note "Same Validation Invoice IDs" between the two methods. Place a centered shared-reference box labeled "Administrator Ground Truth" with the annotation "Urgent / Not Urgent". Below the predictions and reference, place three equal boxes in one row: "Performance and Stability", "Error and Misclassification Patterns", and "Operational Characteristics". Connect both method outputs and Administrator Ground Truth to the relevant analysis boxes. At the bottom center place "Comparative Findings for Chapter IV" and connect all three analysis boxes to it. Show that E3 and E4 use aggregated out-of-fold predictions through a small unobtrusive annotation, not an extra process box. Keep the visual weight of Rule-Based and Decision Tree identical and do not declare a winner. Ensure the figure remains legible in grayscale and at thesis-page scale. Do not include HIGH, MEDIUM, NORMAL, Guideline-Based Ground Truth, Decision Tree Reconstruction, Knowledge Representation Consistency Evaluation, or Operational Knowledge Formalization Framework.
