# Methodological Note: Guideline-Based Labeling

The additional candidate labels in this artifact were not manually assigned or independently validated by a human reviewer.

They were generated through Guideline-Based Labeling using the Operational Labeling Guideline developed during the Knowledge Acquisition and Knowledge Formalization stages described in Chapter III. The procedure applies the published rule base R1-R12 to the repaired decision-time features. Each suggested label is accompanied by the applied rule ID, operational reason, and confidence level.

This means the finalized dataset should be interpreted as a knowledge-guided experimental dataset. The labels are consistent with the operational decision guideline, but they should not be described as the result of a separate manual validation process.

For the final experiment, the target column should be `final_label`. Rows generated through Guideline-Based Labeling can be identified using `final_label_source = Guideline-Based Labeling`.
