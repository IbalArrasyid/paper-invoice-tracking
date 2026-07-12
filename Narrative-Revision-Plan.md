# Narrative Revision Plan

## Scope and Non-Modification Rule

This document is the master revision blueprint for shifting the thesis narrative from a machine-learning prediction paradigm toward a knowledge-engineering paradigm. It is intentionally limited to planning. It must not be treated as a rewritten chapter.

Protected thesis files must not be modified during this blueprint stage:

- `Pendahuluan.tex`
- `Kajian-Pustaka.tex`
- `Metodologi.tex`
- `Hasil-dan-Pembahasan.tex`
- `Kesimpulan.tex`

Additional restrictions:

- Do not modify experiments.
- Do not modify datasets.
- Do not modify figures.
- Do not modify tables.
- Do not rewrite any chapter in this stage.
- Use this document only as the revision map for later editing.

The final thesis narrative must consistently follow this scientific chain:

```text
Knowledge Acquisition
-> Knowledge Formalization
-> Operational Labeling Guideline
-> Operational Reference Model
-> Decision Tree Reconstruction
-> Knowledge Representation Evaluation
```

## Part A: Core Research Message

### True Scientific Contribution

The true scientific contribution of this thesis is not the production of a highly accurate prediction model in the ordinary machine-learning sense. The contribution is the construction, representation, and evaluation of operational knowledge for invoice delivery prioritization. The thesis takes operational knowledge that is originally embedded in customer regulations, administrative routines, invoice cut-off rules, receiving schedules, and staff decision practices, then transforms it into an explicit decision structure that can be examined scientifically.

In the revised paradigm, the research begins with Knowledge Acquisition. This stage identifies the operational concepts that actually control invoice delivery priority, such as proximity to cut-off, limited receiving schedules, missed receiving windows, month-end conditions, and no-cutoff cases. These concepts are then transformed through Knowledge Formalization into structured attributes and operational rules. The formalization stage is crucial because it converts tacit and procedural administrative knowledge into explicit, testable, and machine-readable forms.

The Operational Labeling Guideline is the bridge between knowledge formalization and evaluation. It defines how each invoice receives an operational priority label. Because the label is produced from the formalized guideline, the label should no longer be narrated as a naturally occurring or independently observed "ground truth" in the strongest empirical sense. It is better understood as an Operational Reference Label: a reference decision generated from the formalized operational guideline.

The Rule-Based model then acts as an explicit representation of the operational knowledge. It does not merely "predict" priority; it applies the Operational Reference Model through 12 operational rules. Its value is traceability: each priority recommendation can be explained by the rule or group of rules that fired.

The Decision Tree C4.5 model has a different scientific role. It is not used to prove that a statistical classifier is better than the Rule-Based model. Instead, it is used to test whether the same formalized operational knowledge can be reconstructed from operational attributes and reference labels. In the final experiment, the Decision Tree reconstructs the rule structure into approximately seven decision paths, dominated by `days_to_cutoff_decision_time`, `receive_day_code`, `next_receive_day_gap_feature`, and `receive_schedule`. This demonstrates that the formalized knowledge has a stable structure that can be recovered statistically.

Thus, the thesis contributes a knowledge representation and reconstruction framework for invoice delivery priority. The Rule-Based model represents formalized knowledge explicitly. The Decision Tree reconstructs the same knowledge statistically. The evaluation compares the consistency, interpretability, traceability, and reconstruction behavior of two representations of the same operational knowledge.

### What Is Not the Contribution

The thesis does not prove that Decision Tree C4.5 is superior to Rule-Based reasoning. It also does not prove that either model is universally accurate for all invoice administration contexts. The perfect evaluation metrics in the final experiment must not be framed as general predictive superiority, because the Operational Reference Label is derived from the Operational Labeling Guideline and the Rule-Based model is built from the same formalized knowledge.

The thesis also does not claim that Decision Tree discovers fundamentally new operational rules. The Decision Tree learns from attributes and labels produced by the knowledge formalization process. Its scientific value lies in reconstruction: it compresses and reproduces the operational decision structure without receiving the 12 Rule-Based rules directly.

The final contribution statement should therefore be:

> This thesis demonstrates that formalized operational knowledge for invoice delivery priority can be represented explicitly through a Rule-Based model and reconstructed consistently through Decision Tree C4.5. The comparison evaluates knowledge representation consistency, not algorithmic superiority.

This statement must become the reference point for every chapter.

## Part B: Global Terminology Plan

Do not replace terminology yet. This table defines the target vocabulary for later revision.

| Old terminology | New terminology | Reason for replacement | Affected chapters |
|---|---|---|---|
| Ground Truth | Operational Reference Label | The label is derived from the Operational Labeling Guideline, so it is a reference decision generated from formalized operational knowledge, not an independently observed truth claim. | Chapter I, Chapter III, Chapter IV, Chapter V |
| Final label | Operational Reference Label | Clarifies that `final_label` is the implementation column for the operational reference decision. Keep `final_label` only when referring to dataset column names. | Chapter III, Chapter IV |
| Prediction | Priority Recommendation | The system output is operational guidance for invoice handling, not merely a statistical forecast. | Chapter I, Chapter III, Chapter IV |
| Predicted label | Recommended Priority Label | Avoids reducing the decision to machine prediction; preserves operational decision-support meaning. | Chapter III, Chapter IV |
| Model Comparison | Knowledge Representation Comparison | The scientific object is the comparison of explicit representation and statistical reconstruction of knowledge. | Chapter I, Chapter II, Chapter III, Chapter IV |
| Performance | Representation Consistency | Metrics should show agreement with the Operational Reference Label, not universal predictive performance. | Chapter I, Chapter II, Chapter IV |
| Model performance evaluation | Knowledge representation evaluation | Aligns evaluation with consistency, interpretability, traceability, and reconstruction. | Chapter II, Chapter III, Chapter IV |
| Accuracy | Agreement accuracy with Operational Reference Label | Prevents overclaiming that accuracy equals external correctness. | Chapter II, Chapter IV |
| Classification | Priority categorization | More operational and less prediction-centered. Use "classification" only for algorithmic mechanics. | Chapter I, Chapter II, Chapter III, Chapter IV |
| Rule-Based prediction | Rule-Based priority recommendation | Emphasizes application of explicit operational rules. | Chapter III, Chapter IV |
| Decision Tree prediction | Decision Tree reconstruction output | Emphasizes reconstruction of formalized knowledge. | Chapter III, Chapter IV |
| Decision Tree model | Decision Tree reconstruction model | Clarifies the role of C4.5 in the thesis contribution. | Chapter I, Chapter III, Chapter IV |
| Algorithm superiority | Representation difference | Avoids ranking models as better/worse when the experiment shows equivalent agreement. | Chapter I, Chapter IV, Chapter V |
| Expert labeling | Guideline-Based Labeling | The current research design uses an Operational Labeling Guideline, not independent expert relabeling. | Chapter I, Chapter III, Chapter IV |
| Expert label | Operational Reference Label | Removes the implication of independent human validation when labels are guideline-derived. | Chapter I, Chapter III, Chapter IV |
| Data-driven prediction | Statistical reconstruction of operational knowledge | The Decision Tree learns a structure induced by formalized operational attributes and labels. | Chapter I, Chapter III, Chapter IV |
| Rule-Based model | Explicit Operational Reference Model | Positions Rule-Based as the explicit knowledge representation. | Chapter III, Chapter IV |
| Feature importance | Reconstruction attribute dominance | The feature ranking explains which formalized attributes dominate reconstruction. | Chapter IV |
| Misclassification analysis | Agreement and discrepancy analysis | Allows discussion even when there are zero classification errors. | Chapter IV |
| Comparative evaluation | Knowledge representation evaluation | Reframes evaluation from model contest to representational analysis. | Chapter III, Chapter IV |
| Machine Learning Prediction | Knowledge Reconstruction | Captures the final paradigm transition. | Cover, Abstract, Chapter I, Chapter III, Chapter IV, Chapter V |

Terminology rule for later revision:

- Keep exact dataset column names such as `final_label`, `cutoff_rule`, or `days_to_cutoff_decision_time` when referring to artifacts.
- Use conceptual terms such as Operational Reference Label and Operational Reference Model when explaining scientific meaning.
- If older terms must remain for reader familiarity, introduce them once as secondary wording, for example: "Operational Reference Label, represented in the dataset as `final_label`."

## Part C: Chapter Revision Matrix

| Chapter or component | Current narrative | Target narrative | Paragraphs requiring revision | New paragraphs to insert | Paragraphs to delete | Risk level | Expected scientific outcome |
|---|---|---|---|---|---|---|---|
| Cover and title metadata | Current title frames the thesis as a comparison of Rule-Based and Decision Tree C4.5 for invoice priority determination. This still sounds like a method contest. | Title should foreground representation and reconstruction of operational knowledge. Suggested direction: "Representasi dan Rekonstruksi Pengetahuan Operasional untuk Penentuan Prioritas Pengiriman Invoice Menggunakan Rule-Based dan Decision Tree C4.5". | `main.tex` title metadata and `Cover.tex` inherited title. Do not edit now. | A title rationale note in later revision explaining that Rule-Based and Decision Tree are two representation forms, not competitors for superiority. | None. | High | The first reader signal changes from algorithm comparison to knowledge-engineering contribution. |
| Chapter I: Pendahuluan | Mostly aligned with knowledge acquisition and formalization, but the research question and objective still use "mengevaluasi dan membandingkan performa". | Chapter I should state the research gap as missing operational knowledge formalization and missing evaluation of explicit representation versus statistical reconstruction. | `Pendahuluan.tex:11-13`, `Pendahuluan.tex:19-22`, `Pendahuluan.tex:28-30`, `Pendahuluan.tex:42-44`. | Insert one contribution paragraph after the research gap explaining: tacit operational knowledge -> formalized guideline -> reference label -> two representation forms. | Do not delete paragraphs wholesale. Replace only performance/superiority wording in later revision. | High | Research questions and objectives become consistent with the thesis contribution and prevent defense questions about "which model is better". |
| Chapter II: Kajian Pustaka | Literature review already includes knowledge acquisition/formalization, Rule-Based, C4.5, and metrics. However, the structure still gives substantial space to generic classification performance. | Chapter II should build theoretical support for knowledge engineering, knowledge representation, operational reference labels, and reconstruction. ML theory should support reconstruction, not dominate the chapter. | `Kajian-Pustaka.tex:6`, `Kajian-Pustaka.tex:37-39`, `Kajian-Pustaka.tex:84-90`, `Kajian-Pustaka.tex:122-126`, `Kajian-Pustaka.tex:178-206`. | Insert a conceptual subsection after "Akuisisi dan Formalisasi Pengetahuan" on Operational Reference Model and Knowledge Reconstruction. Add a paragraph before metrics explaining that metrics are used as agreement indicators. | Do not delete the C4.5 or metric formulas. Later revision may shorten purely predictive claims. | Medium | The literature foundation justifies why a perfect metric is interpreted as consistency with formalized knowledge rather than predictive generalization. |
| Chapter III: Metodologi | Strongly aligned with the knowledge pipeline. Still uses `ground truth`, `Comparative Evaluation`, and some prediction-centered wording. | Chapter III should describe a knowledge-engineering method: acquisition, formalization, operational reference labeling, explicit reference model construction, statistical reconstruction, and representation evaluation. | `Metodologi.tex:3-39`, `Metodologi.tex:125-146`, `Metodologi.tex:148-279`, `Metodologi.tex:281-305`. | Insert a paragraph before Rule-Based explaining "Operational Reference Model". Insert a paragraph before Decision Tree explaining that C4.5 receives no Rule Base and reconstructs from reference-labeled data. Insert a paragraph before evaluation defining "representation consistency". | Do not delete the 12-rule table or system design. Do not alter datasets or experiment procedure. | High | Methodology becomes defensible against circularity criticism because it transparently states what is being evaluated. |
| Chapter IV: Hasil dan Pembahasan | Already closest to the target paradigm. It contains dataset characterization, Rule-Based results, Decision Tree results, comparison, reconstruction analysis, discussion, and threats to validity. | Chapter IV must be the intellectual center: the results should be narrated as evidence of explicit representation and statistical reconstruction of operational knowledge. | `Hasil-dan-Pembahasan.tex:3-49`, `51-90`, `92-145`, `147-218`, `220-263`, `304-316`, `318-342`. | Strengthen the opening of each subsection with its role in the knowledge chain. Add one linking paragraph at the beginning of 4.5 stating that this is the main contribution section. | Do not delete result tables, figures, or threats. Later revision may remove any residual phrase implying algorithm superiority. | Very high | Chapter IV becomes a coherent proof of knowledge representation consistency and Decision Tree reconstruction, not a performance leaderboard. |
| Chapter V: Kesimpulan | `Kesimpulan.tex` is not present in the current project root, although the request names it as protected. | Chapter V, if created later, must conclude the knowledge-engineering contribution and avoid claiming Decision Tree superiority. | No active file found. Treat as a planned future chapter, not an editable file in this stage. | Insert four conclusion blocks later: contribution, empirical findings, limitations, future work. | None now. | High | Final conclusion mirrors the core message: formalized operational knowledge can be explicitly represented and statistically reconstructed. |
| Abstract | Current review report says the abstract has been aligned, but it should still be checked against the new terminology. | Abstract should summarize the knowledge pipeline, not a model contest. | `Abstrak-Indo.tex` should be checked later, but it was not part of the protected list. Do not edit now. | Add one sentence later if missing: "Evaluasi menunjukkan konsistensi representasi pengetahuan, bukan keunggulan universal salah satu model." | None. | Medium | The abstract primes examiners to read the thesis under the correct paradigm. |
| Bibliography and references | Current references support document tracking, POD, Rule-Based, C4.5, and operational systems. | No new references are required for this blueprint. Later revision may add knowledge-engineering references only if required by supervisor. | `References.bib` only if later theoretical strengthening is requested. | Optional later addition: knowledge engineering, knowledge representation, expert systems, interpretable decision trees. | None. | Low | Literature support remains stable without disturbing thesis structure. |

## Part D: Chapter IV Blueprint

Chapter IV must not be rewritten in this document. The following blueprint defines how each subsection should function scientifically.

### Section 4.1: Karakteristik Dataset

| Blueprint item | Instruction |
|---|---|
| Purpose of section | Establish the dataset as the operational substrate produced by Knowledge Acquisition, Knowledge Formalization, and Guideline-Based Labeling. |
| Scientific objective | Show that the dataset is not merely raw historical data; it is a structured representation of formalized invoice-priority knowledge. |
| Main message | The final dataset is suitable for knowledge representation evaluation because it contains complete Operational Reference Labels, no duplicate invoice numbers, and operational attributes derived from formalized knowledge. |
| Expected scientific argument | Since the dataset contains 105 unique invoices, valid labels, and operational attributes such as cut-off distance and receiving schedule, it can support an evaluation of whether operational knowledge is consistently represented and reconstructed. |
| Supporting experimental evidence | 105 rows, 105 unique invoice numbers, 0 duplicate invoice numbers, 0 missing `final_label`, 0 invalid labels, 0 invalid `cutoff_rule`, 0 validation blockers, 2 validation warnings. |
| Key figures | None required unless the current chapter already uses a dataset diagram. Do not create new figures in this stage. |
| Key tables | Distribution of final labels; train-test split table; validation summary if added later as a table. |
| Interpretation | Interpret class distribution as coverage of three operational priority states: HIGH, MEDIUM, NORMAL. Interpret stratified split as preserving reference-label representation in train and test subsets. |
| Expected conclusion | The dataset is adequate for evaluating consistency of operational knowledge representation within the bounded research context. |
| Things that MUST NOT be claimed | Do not claim the dataset is large. Do not claim it guarantees external generalization. Do not claim labels are independent human truth. Do not claim the dataset proves universal operational behavior. |

Narrative role in the full Chapter IV:

- 4.1 should answer: "What is being evaluated?"
- The answer must be: a formalized operational reference dataset, not just historical invoice data.

### Section 4.2: Hasil Model Rule-Based

| Blueprint item | Instruction |
|---|---|
| Purpose of section | Present Rule-Based as explicit representation of the Operational Reference Model. |
| Scientific objective | Demonstrate that the 12 operational rules can reproduce the Operational Reference Label consistently because both originate from the same Operational Labeling Guideline. |
| Main message | Rule-Based is valuable because it preserves traceability, auditability, and direct correspondence to operational rules. |
| Expected scientific argument | Perfect agreement is expected and scientifically meaningful as internal consistency, not as independent validation. The Rule-Based model directly applies the formalized knowledge. |
| Supporting experimental evidence | Rule Base contains 12 rules; activated rules in dataset include R2, R3, R4, R6, R7, R8, R9, R10, R11; test accuracy, macro F1, and weighted F1 are 1.000; no test misclassification. |
| Key figures | Rule-Based confusion matrix. |
| Key tables | Rule usage statistics; metric comparison if referenced briefly; Rule Base table from Chapter III should be cross-referenced conceptually, not duplicated. |
| Interpretation | Explain that the Rule-Based result verifies consistency between guideline-derived labels and explicit rule implementation. Emphasize rule IDs as traceable explanation units. |
| Expected conclusion | Rule-Based functions as the explicit operational knowledge representation and provides transparent priority recommendations. |
| Things that MUST NOT be claimed | Do not claim Rule-Based performance proves real-world correctness independently. Do not claim perfect agreement is surprising evidence of algorithmic excellence. Do not claim Rule-Based discovered the rules; the rules were formalized from operational knowledge. |

Writing reminders:

- Use "agreement with Operational Reference Label" rather than "prediction accuracy" whenever explaining scientific meaning.
- When reporting metrics, immediately interpret them as consistency with the guideline.

### Section 4.3: Hasil Decision Tree C4.5

| Blueprint item | Instruction |
|---|---|
| Purpose of section | Present Decision Tree C4.5 as statistical reconstruction of formalized operational knowledge. |
| Scientific objective | Show that C4.5 can reconstruct the same operational decision structure from attributes and reference labels without receiving the 12 rules directly. |
| Main message | Decision Tree C4.5 does not introduce fundamentally new operational knowledge; it reconstructs a compressed decision structure dominated by operational timing and receiving-schedule attributes. |
| Expected scientific argument | The tree root and feature importance show that the learned structure is driven by formalized operational attributes, especially `days_to_cutoff_decision_time`, `receive_day_code`, `next_receive_day_gap_feature`, and `receive_schedule`. |
| Supporting experimental evidence | Test accuracy 1.000; macro F1 1.000; dominant feature importance values: `days_to_cutoff_decision_time` 0.4818, `receive_day_code` 0.2984, `next_receive_day_gap_feature` 0.1429, `receive_schedule` 0.0769; other listed features 0.0000. |
| Key figures | Decision Tree visualization; Decision Tree confusion matrix; feature importance figure. |
| Key tables | Feature importance ranking table. |
| Interpretation | Interpret tree thresholds as statistical reconstruction of operational cut-off and schedule logic. Explain that thresholds such as 3.5 and 10.5 are model boundaries corresponding to formalized urgency concepts, not new business rules by themselves. |
| Expected conclusion | Decision Tree confirms that the formalized operational knowledge has a stable pattern that can be reconstructed from data. |
| Things that MUST NOT be claimed | Do not claim Decision Tree is superior. Do not claim C4.5 discovered new rules. Do not claim feature importance is causal proof. Do not claim zero-importance features are operationally irrelevant in general. |

Writing reminders:

- Distinguish "learned tree path" from "operational rule".
- Explain that zero-importance features may be redundant after `days_to_cutoff_decision_time` captures their information.

### Section 4.4: Analisis Komparatif

| Blueprint item | Instruction |
|---|---|
| Purpose of section | Compare the two knowledge representation forms rather than ranking two algorithms. |
| Scientific objective | Clarify that equal perfect metrics mean both models agree with the Operational Reference Label under the final dataset, but their scientific roles differ. |
| Main message | Rule-Based is explicit, traceable, and maintainable as operational knowledge. Decision Tree is compressed, data-driven, and useful for reconstruction analysis. |
| Expected scientific argument | The same metric values support consistency, while the conceptual comparison explains different representation mechanisms. |
| Supporting experimental evidence | Both models have 1.000 accuracy, 1.000 macro precision, 1.000 macro recall, 1.000 macro F1, and 0 total errors on 21 test records. |
| Key figures | Confusion matrices from 4.2 and 4.3 may be referenced; no new figure required. |
| Key tables | Metric comparison table; comparison-characteristics table; misclassification summary. |
| Interpretation | The metrics show agreement; the model-characteristic table explains epistemic difference: explicit representation versus statistical reconstruction. |
| Expected conclusion | The comparison validates two complementary ways to represent formalized operational knowledge. |
| Things that MUST NOT be claimed | Do not claim one model wins. Do not claim equal metrics mean equal suitability in all deployment contexts. Do not frame the comparison as pure predictive performance. |

Writing reminders:

- The comparative axis should be "representation, traceability, reconstruction, maintainability", not "highest metric".
- Discuss metrics only as one evidence type, not as the main contribution.

### Section 4.5: Analisis Rekonstruksi Pengetahuan

| Blueprint item | Instruction |
|---|---|
| Purpose of section | Serve as the main scientific contribution section of Chapter IV. |
| Scientific objective | Demonstrate how 12 explicit operational rules are reconstructed by Decision Tree into approximately seven decision paths while preserving the same operational decision structure. |
| Main message | The Decision Tree compresses and reconstructs the formalized guideline; it does not replace, invalidate, or outperform the Rule Base. |
| Expected scientific argument | The mapping between Decision Tree paths and Rule-Based rules proves structural alignment between explicit knowledge representation and statistical reconstruction. |
| Supporting experimental evidence | Rule Base R1-R12; Decision Tree paths DTR1-DTR7; dominant attributes; no new operational knowledge outside the Rule Base; identical agreement with Operational Reference Label. |
| Key figures | Conceptual knowledge reconstruction figure. The existing placeholder should later be replaced professionally, but not in this stage. |
| Key tables | Mapping of Decision Tree paths to Rule Base; feature importance ranking; rule usage statistics if needed. |
| Interpretation | Explain reconstruction as a three-part process: representation in Rule Base, compression in Decision Tree paths, and consistency evaluation against the Operational Reference Label. |
| Expected conclusion | Formalized operational knowledge is representable explicitly and reconstructable statistically. This is the thesis contribution. |
| Things that MUST NOT be claimed | Do not claim seven Decision Tree paths are better than 12 rules. Do not claim compressed paths are administratively complete substitutes for documented rules. Do not claim the tree creates new policy. |

Required conceptual sequence in 4.5:

1. Knowledge Acquisition identifies operational decision concepts.
2. Knowledge Formalization turns those concepts into attributes and 12 rules.
3. Operational Labeling Guideline generates the Operational Reference Label.
4. Rule-Based applies the explicit Operational Reference Model.
5. Decision Tree reconstructs the same structure from data.
6. Feature importance shows which formalized attributes dominate reconstruction.
7. Path-to-rule mapping shows structural consistency.
8. The contribution is representation and reconstruction, not superiority.

### Section 4.6: Diskusi

| Blueprint item | Instruction |
|---|---|
| Purpose of section | Synthesize the scientific meaning of the results without repeating tables. |
| Scientific objective | Explain what the findings mean for knowledge engineering, invoice administration, and future decision-support systems. |
| Main message | The thesis shows that operational invoice-priority knowledge can be made explicit, operationalized, and checked through two complementary representations. |
| Expected scientific argument | Rule-Based provides transparent operational control; Decision Tree provides reconstruction evidence and attribute-dominance analysis; both depend on the quality of formalized knowledge. |
| Supporting experimental evidence | Perfect agreement for both models; 12 rules; seven tree paths; dominant features; zero misclassifications; zero validation blockers; small dataset limitation. |
| Key figures | Knowledge reconstruction figure may be referenced. |
| Key tables | Feature importance and mapping tables may be referenced; do not repeat numeric tables in prose unless needed. |
| Interpretation | Tie every interpretation back to the knowledge pipeline. Discuss practical value: auditability, maintainability, and checking whether data-driven paths remain aligned with rules. |
| Expected conclusion | The empirical results support the claim that formalized operational knowledge can be consistently represented and reconstructed within the studied context. |
| Things that MUST NOT be claimed | Do not overstate generalization. Do not claim independent validation. Do not claim the system solves all invoice administration problems. Do not claim Decision Tree should replace operational guidelines. |

Discussion structure for later writing:

- Paragraph 1: restate contribution in knowledge-engineering terms.
- Paragraph 2: interpret Rule-Based as explicit representation.
- Paragraph 3: interpret C4.5 as reconstruction and compression.
- Paragraph 4: explain why perfect metrics are consistency evidence.
- Paragraph 5: explain operational implications.
- Paragraph 6: transition to validity limitations.

### Section 4.7: Threats to Validity

| Blueprint item | Instruction |
|---|---|
| Purpose of section | Protect the thesis from overclaiming and show examiner awareness of research limitations. |
| Scientific objective | State why the results are valid for representation consistency but limited for external predictive generalization. |
| Main message | The study is internally coherent as a knowledge representation and reconstruction evaluation, but results are bounded by guideline-derived labels, dataset size, customer-specific rules, and context-specific features. |
| Expected scientific argument | Because labels are produced from the Operational Labeling Guideline, agreement must be read as consistency with the guideline. This is appropriate for the research objective but not equivalent to independent real-world validation. |
| Supporting experimental evidence | 105 invoices; 21 test invoices; guideline-derived labels; no misclassification; feature dominance concentrated in a few operational attributes. |
| Key figures | None required. |
| Key tables | None required unless a compact validity table is later added. |
| Interpretation | Each validity threat should be linked to how it affects claims. For example, internal validity affects interpretation of perfect Rule-Based agreement; external validity affects generalization beyond the studied organization. |
| Expected conclusion | The findings are credible within the bounded knowledge-engineering objective, while future work should test the framework on new periods, additional customers, and independently reviewed operational cases. |
| Things that MUST NOT be claimed | Do not write limitations as minor formalities. Do not say the threats invalidate the research. Do not hide the guideline-label dependency. |

Threats that must remain explicit:

- Internal validity: label and Rule Base share the same guideline source.
- External validity: organization-specific customer rules limit generalization.
- Construct validity: priority may involve unmodeled factors.
- Dataset limitation: 105 invoices is limited.
- Labeling limitation: Guideline-Based Labeling is appropriate but not independent human validation.
- Future work: new data, broader customers, independent validation, and monitoring after rule changes.

## Part E: Knowledge Reconstruction Analysis Instructions

This part defines exactly how the discussion of knowledge reconstruction should be written later. It is not the discussion itself.

### Fixed Facts and Required Interpretation

| Fixed fact | Why it matters | How it should be interpreted | What should NOT be claimed | How it supports the thesis contribution |
|---|---|---|---|---|
| Operational Rule Base contains 12 operational rules. | Shows that operational knowledge has been formalized into explicit, auditable decision units. | Treat R1-R12 as the explicit Operational Reference Model derived from the Operational Labeling Guideline. | Do not claim the 12 rules are universal for every company. Do not claim they were discovered by the algorithms. | Establishes the explicit knowledge representation against which reconstruction can be interpreted. |
| Decision Tree reconstructs these rules into approximately 7 decision paths. | Shows compression and reconstruction of formalized knowledge. | Interpret seven paths as statistical reconstruction paths that align with groups of operational rules. | Do not claim seven paths are better than 12 rules. Do not claim they should replace the operational guideline. | Demonstrates that the formalized rule structure is learnable from operational attributes and reference labels. |
| Dominant operational attributes are `days_to_cutoff_decision_time`, `receive_day_code`, `receive_schedule`, and also `next_receive_day_gap_feature` in the final artifact. | Identifies the formalized knowledge elements that drive reconstruction. | Interpret dominance as evidence that timing to cut-off and receiving-schedule constraints are central to invoice priority. | Do not claim these features are causal in a general statistical sense. Do not ignore `next_receive_day_gap_feature`, because the final artifact gives it nonzero importance. | Supports the claim that the Decision Tree reconstructs operational logic, not arbitrary correlations. |
| Decision Tree introduces no fundamentally new operational knowledge. | Prevents overclaiming discovery. | Interpret the tree as reconstructing, compressing, and reorganizing knowledge already formalized through the guideline. | Do not say C4.5 discovered a new policy or new customer rule. | Strengthens the paradigm shift from prediction to knowledge reconstruction. |
| Decision Tree reconstructs formalized operational knowledge using statistical learning. | Defines C4.5's proper scientific role. | Explain that C4.5 receives features and labels, not the Rule Base itself, so alignment with the Rule Base is reconstruction evidence. | Do not frame C4.5 as an independent oracle. Do not claim reconstruction equals external validation. | Shows the complementary role of data-driven learning inside a knowledge-engineering framework. |
| Feature importance shows `cutoff_type` or `cutoff_rule`, weekday-related variables, and month-end-related variables have negligible contribution because their information is already represented through `days_to_cutoff`. | Explains why operationally meaningful features can have zero model importance. | Use exact artifact names when writing: `cutoff_rule`, `receive_weekday_code`, `receive_month_end_flag`, `receive_day_of_month`, and similar zero-importance variables. Explain redundancy through `days_to_cutoff_decision_time`. | Do not claim zero importance means these concepts are operationally irrelevant. Do not delete them from the methodology. | Shows that the tree selected a compact representation of the same knowledge rather than rejecting operational concepts. |
| Rule-Based achieves perfect agreement because the Operational Reference Label was derived from the Operational Labeling Guideline. | Prevents circularity criticism by stating the design honestly. | Interpret 1.000 metrics as internal consistency between guideline-derived label and explicit rule implementation. | Do not claim independent predictive validation. Do not present perfect agreement as unexpected algorithmic superiority. | Supports the contribution by proving that the formalized knowledge can be applied consistently as explicit rules. |
| Decision Tree achieves the same agreement because it successfully reconstructs the same operational structure. | Explains why C4.5 also reaches perfect agreement. | Interpret 1.000 metrics as successful reconstruction on the final stratified test split. | Do not claim universal generalization. Do not claim the model will always perform perfectly on future data. | Supports the contribution by showing that the formalized structure is stable enough to be statistically reconstructed in the experiment. |

### Required Writing Logic for Reconstruction Discussion

Use the following sequence when later drafting the reconstruction discussion:

1. Start from the knowledge source, not from the models.
2. State that operational knowledge was acquired from regulations, schedules, cut-off constraints, and administrative practice.
3. Explain that this knowledge was formalized into attributes and 12 operational rules.
4. Explain that the Operational Labeling Guideline generated the Operational Reference Label.
5. Explain that Rule-Based applies this knowledge directly.
6. Explain that Decision Tree receives only the formalized attributes and labels, not the Rule Base.
7. Show that the tree reconstructs the same structure through seven paths.
8. Use feature importance to explain why reconstruction is dominated by cut-off distance and receiving schedule.
9. Explain zero-importance features as redundancy, not irrelevance.
10. Conclude that the scientific contribution is consistent representation and reconstruction of operational knowledge.

### Forbidden Claims in Reconstruction Discussion

The later chapter revision must not claim:

- Decision Tree is superior to Rule-Based.
- Rule-Based is inferior because it has more rules.
- Seven tree paths are a replacement for the 12 operational rules.
- Perfect metrics prove universal real-world accuracy.
- Operational Reference Labels are independent external ground truth.
- Zero-importance features are useless in operations.
- C4.5 discovered new operational policy.
- The result generalizes without testing on future periods or other organizations.

## Part F: Defense Strategy

| Defense argument | Possible examiner question | Recommended answer | Scientific justification |
|---|---|---|---|
| 1. The thesis contribution is knowledge representation and reconstruction, not algorithm superiority. | "If both models have the same metric values, what is the contribution?" | The contribution is showing that operational invoice-priority knowledge can be formalized, represented explicitly through Rule-Based rules, and reconstructed statistically by Decision Tree C4.5. The equal metrics show consistency with the Operational Reference Label, while the scientific value lies in comparing representation forms. | The experiment uses one Operational Labeling Guideline and evaluates two representation mechanisms: direct rule application and data-driven reconstruction. |
| 2. Perfect Rule-Based agreement is expected and valid within the research design. | "Isn't the Rule-Based result circular because the labels come from the guideline?" | It is not an independent validation claim. It is an internal consistency evaluation. Since the label is derived from the Operational Labeling Guideline, the Rule-Based result verifies that the explicit rule implementation consistently represents the formalized guideline. | The research objective is representation consistency, so agreement with the Operational Reference Label is an appropriate measure when interpreted correctly. |
| 3. Decision Tree is used to reconstruct knowledge, not discover new rules. | "Did C4.5 discover anything new?" | It did not introduce fundamentally new operational knowledge. It reconstructed the existing formalized structure into approximately seven decision paths using attributes such as `days_to_cutoff_decision_time`, receiving-day information, and schedule-gap information. | The path-to-rule mapping and feature importance show alignment with the Rule Base and Operational Labeling Guideline. |
| 4. Feature importance supports the knowledge-engineering interpretation. | "Why do some operational features have zero importance?" | Some features are operationally meaningful but redundant inside the learned tree because their information is already summarized by stronger derived attributes, especially `days_to_cutoff_decision_time`. Zero model importance does not mean the concept is irrelevant in operations. | Decision Tree selects the attributes that best split the final dataset. Derived timing features can absorb information from cut-off type, weekday, or month-end indicators. |
| 5. The study is bounded but defensible. | "Can this result be generalized to other companies?" | Not directly without further testing. The result is valid for the studied operational context and final dataset. Future work should test the guideline and reconstruction framework on new periods, more customers, and independent operational review. | The thesis explicitly states threats to validity: small dataset, organization-specific rules, guideline-derived labels, and possible unmodeled operational factors. |

Additional short defense lines:

- "The Operational Reference Label is not claimed as universal truth; it is the formal reference decision produced by the guideline."
- "Rule-Based is best for auditability and rule maintenance; C4.5 is useful for reconstruction analysis and feature dominance."
- "The result should be read as knowledge consistency, not predictive superiority."
- "The tree's simpler structure is compression, not replacement of the operational guideline."
- "The strongest evidence is the alignment between the 12-rule base, seven tree paths, and dominant operational attributes."

## Part G: Safest Execution Order

Do not revise chapters sequentially from Chapter I to Chapter V. That would risk rewriting the introduction before the final scientific contribution is fully stabilized.

Recommended execution order:

| Order | Revision target | Why this comes at this stage | Main risk controlled |
|---|---|---|---|
| 1 | Chapter IV, especially 4.5 Knowledge Reconstruction Analysis | Chapter IV contains the actual evidence and the main scientific contribution. Stabilize the interpretation before changing the framing chapters. | Prevents Chapter I and Chapter III from promising claims that Chapter IV does not support. |
| 2 | Chapter III Methodology | Once Chapter IV's evidence logic is fixed, revise methodology terms so the research design clearly describes operational reference labeling, explicit representation, statistical reconstruction, and representation consistency. | Prevents circularity criticism and clarifies why the experiment is valid. |
| 3 | Chapter I Introduction | After contribution and methodology are stable, revise the research gap, research question, and objective to match the knowledge-engineering paradigm. | Prevents the thesis from opening as an algorithm-superiority study. |
| 4 | Chapter II Literature Review | Adjust theory to support knowledge representation, operational reference models, and reconstruction. Keep ML theory but subordinate it to the knowledge-engineering frame. | Prevents theory chapter from overemphasizing generic classification performance. |
| 5 | Cover, title metadata, and abstract | Update the title and summary after the internal argument is stable. | Prevents title/abstract from promising a framing that later chapters do not consistently deliver. |
| 6 | Chapter V Conclusion, if the file is added later | Write conclusion last so it reflects the stabilized contribution, limitations, and future work. | Prevents conclusion from overstating Decision Tree superiority or universal accuracy. |
| 7 | Global terminology pass | Apply the terminology table across all chapters only after all conceptual edits are complete. | Prevents partial terminology replacement that creates inconsistency. |
| 8 | Final defense-readiness pass | Read Chapter I, III, IV, and V together as one argument. | Catches contradictions in contribution, methodology, result interpretation, and limitations. |

Minimum safe revision sequence:

```text
Chapter IV contribution logic
-> Chapter III method language
-> Chapter I research question and objective
-> Chapter II theoretical support
-> Cover and abstract
-> Chapter V
-> terminology consistency pass
```

## Final Blueprint Checklist

Before any later LaTeX revision is started, confirm that the planned edits satisfy all checklist items:

- The thesis does not claim Decision Tree superiority.
- The thesis does not claim universal model accuracy.
- "Ground truth" is reframed as Operational Reference Label where scientifically appropriate.
- Rule-Based is described as explicit representation of the Operational Reference Model.
- Decision Tree is described as reconstruction of formalized operational knowledge.
- Metrics are interpreted as agreement or representation consistency.
- Feature importance is interpreted as reconstruction attribute dominance.
- Zero-importance features are described as redundant in the learned tree, not operationally meaningless.
- Chapter IV section 4.5 remains the scientific center of the thesis.
- Limitations explicitly mention guideline-derived labels, dataset size, customer-specific rules, and limited generalization.
- Chapter V, if later created, concludes representation and reconstruction rather than prediction superiority.
