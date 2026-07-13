# Scientific Thesis Audit

## Executive Summary

The thesis has a strong and defensible scientific core in Chapters III and IV: it now largely presents the work as an `Operational Knowledge Formalization Framework` that transforms operational invoice-priority knowledge into formal attributes, an `Operational Labeling Guideline`, `Guideline-Based Ground Truth`, `Rule-Based Representation`, and `Decision Tree Reconstruction`, then evaluates `Knowledge Representation Consistency`.

However, the manuscript is not yet scientifically consistent as a full thesis. The title, abstract, Chapter I, and much of Chapter II still frame the study as a comparison of methods, algorithms, prediction, classification, and performance. That older framing conflicts with the positioning document, which explicitly states that the contribution is not algorithm superiority or model-performance comparison. A second major structural problem is that `Kesimpulan.tex` exists but is not included in `main.tex`; therefore the thesis, as compiled from `main.tex`, currently ends at Chapter IV plus bibliography and appendix.

The thesis is intellectually close to the intended knowledge-engineering argument, but it is not yet defense-ready because the opening promise, theoretical foundation, and compiled chapter structure do not fully match the final scientific contribution.

## Strengths

1. Chapter III clearly introduces the `Operational Knowledge Formalization Framework` at `Metodologi.tex:5` and explains the knowledge flow through `Knowledge Acquisition`, `Knowledge Structuring`, `Knowledge Formalization`, `Operational Labeling Guideline`, `Guideline-Based Ground Truth`, `Rule-Based Representation`, `Decision Tree Reconstruction`, and `Knowledge Representation Consistency Evaluation` at `Metodologi.tex:7-18`.
2. Chapter III correctly distinguishes `Attribute Formalization` and `Rule Formalization` at `Metodologi.tex:45-81`.
3. Chapter III gives a defensible explanation of `Guideline-Based Ground Truth` as a reference label derived from the guideline, not an independent external truth, at `Metodologi.tex:132-153`.
4. Chapter IV is the strongest chapter scientifically. It interprets metrics as consistency evidence rather than predictive superiority at `Hasil-dan-Pembahasan.tex:92`, `155`, `224`, `275-277`, and `334-336`.
5. Chapter IV explains Decision Tree C4.5 as `Knowledge Reconstruction`, not as a superior classifier, at `Hasil-dan-Pembahasan.tex:96`, `118`, `232`, and `290-294`.
6. The threats-to-validity section is unusually candid and appropriate for this research design, especially regarding guideline-derived labels, dataset size, limited generalization, and organization-specific rules at `Hasil-dan-Pembahasan.tex:300-342`.
7. `Research-Positioning-Statement.md` is clear, mature, and scientifically coherent. It gives the correct defense position at lines `5-13`, `31-46`, `100-106`, `182`, and `198-213`.

## Weaknesses

1. The thesis title in `main.tex:80-82` still presents the study as a comparison of Rule-Based and Decision Tree C4.5 methods, which contradicts the intended primary contribution.
2. Chapter I still states the research question and objective as performance comparison at `Pendahuluan.tex:13`, `21`, and `30`.
3. Chapter II still positions the theoretical foundation around classification, prediction, and performance at `Kajian-Pustaka.tex:6`, `39`, `90`, `122-126`, and `178-206`.
4. The abstract is closer to the target framing, but it still says the study compares two decision paradigms and uses unqualified `ground truth` at `Abstrak-Indo.tex:21-23`.
5. `Kesimpulan.tex` is scientifically aligned in many places, but it is not included in `main.tex`, so Chapter V is absent from the compiled thesis.
6. Two newly integrated final figures are missing as files: `Knowledge Formalization Framework.png` and `KnowledgeReconstruction.png`.
7. Several figure and table labels are unused, especially in Chapter II and the system-design part of Chapter III.

## Major Issues

### 1. Research Positioning Is Still Split Between Two Paradigms

Target positioning from `Research-Positioning-Statement.md:31-46` and `100-106`: the primary contribution is the `Operational Knowledge Formalization Framework`; Rule-Based and Decision Tree are two representation/reconstruction mechanisms, not competing models.

Inconsistent sentences:

| Location | Inconsistency |
|---|---|
| `main.tex:80` | The Indonesian title says `Perbandingan Metode Rule-Based dan Decision Tree C4.5`, which foregrounds method comparison rather than operational knowledge formalization. |
| `main.tex:82` | The English title repeats the same comparison framing. |
| `Abstrak-Indo.tex:21` | States the objective as comparing two priority-decision paradigms rather than proposing/evaluating a knowledge formalization framework. |
| `Pendahuluan.tex:13` | Uses `komparasi model keputusan prioritas`, `Dua metodologi dikomparasikan`, and asks about `mengevaluasi performa`, all of which re-center comparison/performance. |
| `Pendahuluan.tex:21` | Research question asks to `mengevaluasi dan membandingkan performa` Rule-Based and C4.5. |
| `Pendahuluan.tex:30` | Research objective says `evaluasi komparatif performa`, again making performance comparison the stated goal. |
| `Pendahuluan.tex:43` | States the models are being compared and limits the study to two algorithms, reinforcing an algorithm-comparison identity. |
| `Kajian-Pustaka.tex:6` | Literature review says the research gap is solved through `komparasi algoritma prioritas`. |
| `Kajian-Pustaka.tex:39` | Says the study compares C4.5 with knowledge-driven Rule-Based to cover data-driven weakness; this is closer, but still frames the scientific move as comparison. |
| `Kajian-Pustaka.tex:98` | Says Rule-Based needs to be compared with a data-based approach to see how far explicit rules represent historical patterns. This is acceptable only if reframed as representation-consistency evaluation. |
| `Kesimpulan.tex:21` | Says the purpose is `membandingkan representasi eksplisit dan rekonstruksi data-driven`; this is nearly correct, but should explicitly say consistency evaluation rather than comparison. |

Severity: Major. The thesis body now contains the new argument, but the reader is still first taught to expect a model-performance comparison.

### 2. Chapter V Is Not Compiled

`main.tex` includes:

- `Pendahuluan` at `main.tex:141`
- `Kajian-Pustaka` at `main.tex:143`
- `Metodologi` at `main.tex:145`
- `Hasil-dan-Pembahasan` at `main.tex:147`

It does not include `Kesimpulan.tex`. This means the thesis has no compiled conclusion chapter even though `Kesimpulan.tex` exists and is reasonably aligned with the final framework. This is a structural readiness blocker.

Severity: Major.

### 3. Chapter II Does Not Yet Theoretically Support the Final Contribution

Chapter II contains useful material, but its theoretical center is still classification and performance. Missing or underdeveloped foundations:

- `Operational Knowledge Formalization Framework` as a knowledge-engineering contribution.
- `Knowledge Structuring` as a distinct process.
- `Operational Dataset` as a knowledge artifact.
- `Guideline-Based Ground Truth` as a guideline-derived reference label.
- `Rule-Based Representation` as explicit knowledge representation.
- `Decision Tree Reconstruction` as statistical reconstruction rather than prediction.
- `Knowledge Representation Consistency` as the evaluation construct.

Key locations:

- `Kajian-Pustaka.tex:84-90` introduces knowledge acquisition/formalization but does not cite knowledge-engineering literature and still says the goal is `ground truth` and model classification.
- `Kajian-Pustaka.tex:122-126` explains data-driven classification and prediction rather than reconstruction.
- `Kajian-Pustaka.tex:178-206` explains evaluation metrics as predictive performance rather than representation consistency.

Severity: Major.

### 4. Required Figures Are Integrated but Missing from Workspace

The LaTeX includes:

- `Metodologi.tex:11`: `Knowledge Formalization Framework.png`
- `Hasil-dan-Pembahasan.tex:285`: `KnowledgeReconstruction.png`

Both files are currently absent from the project root. This is a compilation and final-manuscript readiness blocker. Scientifically, the surrounding discussion is appropriate, but the figures cannot function as evidence until the final assets exist under the exact filenames.

Severity: Major for compilation/readiness; Minor for narrative logic.

## Minor Issues

1. `Abstrak-Indo.tex:23` uses unqualified `ground truth`; the thesis target vocabulary prefers `Guideline-Based Ground Truth`.
2. `Pendahuluan.tex:42` uses unqualified `ground truth` and `evaluasi model`.
3. `Kajian-Pustaka.tex:90` uses `ground truth` and `model klasifikasi`.
4. `Hasil-dan-Pembahasan.tex:151` uses the section title `Analisis Representasi Komparatif`. The body is careful, but the title still carries comparison language.
5. `Hasil-dan-Pembahasan.tex:185` uses `label akhir berbasis pedoman`; acceptable as dataset description, but conceptually stronger as `Guideline-Based Ground Truth`.
6. `Hasil-dan-Pembahasan.tex:188` says `sebelum prediksi dilakukan`; this is a local leftover prediction term inside an otherwise aligned table.
7. `Kesimpulan.tex:9` says `label akhir` and `data-driven`; acceptable but less precise than `Guideline-Based Ground Truth` and `Decision Tree Reconstruction`.
8. `Kesimpulan.tex:33-35` shifts future work toward broader machine-learning model exploration. This is acceptable as future work, but it risks weakening the knowledge-engineering identity unless tied back to interpretability and representation consistency.
9. Several captions are descriptive rather than interpretive, especially system-design figures in Chapter III and generic theory figures in Chapter II.
10. Some Chapter IV wording repeats the same consistency claim several times; not harmful, but it can be tightened in final revision.

## Chapter-by-Chapter Review

### Front Matter and Abstract

Readiness: Needs Major Revision.

The title in `main.tex:80-82` is the biggest front-matter inconsistency. It tells examiners the thesis is a method comparison, while the actual contribution should be operational knowledge formalization and representation consistency. The abstract partially fixes this by saying the contribution is not universal model superiority at `Abstrak-Indo.tex:23`, but it still opens the method statement as a comparison of two paradigms at `Abstrak-Indo.tex:21` and uses unqualified `ground truth` at `Abstrak-Indo.tex:23`.

### Chapter I: Pendahuluan

Readiness: Needs Major Revision.

Chapter I correctly identifies the operational problem: semi-manual invoice/POD tracking, tacit operational knowledge, customer cut-off rules, and inconsistent priority decisions at `Pendahuluan.tex:5-13`. However, it does not yet clearly state the `Operational Knowledge Formalization Framework` as the primary contribution. The research question and objective still ask about comparing performance, not evaluating representation consistency.

Logical gaps:

- No explicit separation of operational problem, knowledge problem, and system problem.
- `Knowledge Structuring`, `Operational Dataset`, `Guideline-Based Ground Truth`, `Decision Tree Reconstruction`, and `Knowledge Representation Consistency` are not introduced as the final research chain.
- The stated research question at `Pendahuluan.tex:21` does not naturally lead to Chapter III's knowledge-engineering method.

### Chapter II: Kajian Pustaka

Readiness: Needs Major Revision.

Chapter II provides relevant sources for document tracking, POD, Rule-Based, and C4.5. All citation keys used in the audited files exist in `References.bib`. However, the chapter still supports an older classifier-comparison thesis more than the final knowledge-engineering thesis.

Logical gaps:

- The literature review table focuses on whether prior work has compared Rule-Based and C4.5, rather than whether prior work lacks operational knowledge formalization.
- The knowledge-engineering subsection at `Kajian-Pustaka.tex:84-90` is too short and uncited for the thesis's primary contribution.
- The C4.5 subsection at `Kajian-Pustaka.tex:128-154` explains the algorithm but does not connect interpretability to reconstruction analysis.
- The metrics subsection at `Kajian-Pustaka.tex:178-206` defines predictive metrics but does not establish them as agreement/consistency indicators against `Guideline-Based Ground Truth`.

### Chapter III: Metodologi

Readiness: Needs Minor Revision.

Chapter III is largely aligned with the intended contribution. It explicitly introduces the framework, figure, two formalization branches, guideline-based labels, representation, reconstruction, consistency evaluation, and system integration.

Remaining issues:

- `Knowledge Structuring` is introduced at `Metodologi.tex:7` and `16`, but there is no dedicated method section explaining how structuring is performed.
- `Dataset Construction` at `Metodologi.tex:99` is conceptually the `Operational Dataset` stage, but the section title does not use the target term.
- Some table/figure labels are unused: `tab:sumber_pengetahuan`, `tab:formalisasi_pengetahuan`, `tab:fitur_dataset`, `fig:arsitektur_sistem`, `fig:use_case_diagram`, `fig:activity_pod`, and `fig:erd`.
- The Rule Base uses shortened feature names such as `days_to_cutoff`, `next_receive_day_gap`, and `month_end_flag` at `Metodologi.tex:161-238`, while the dataset table uses `days_to_cutoff_decision_time`, `next_receive_day_gap_feature`, and `receive_month_end_flag` at `Metodologi.tex:121-125`. This is explainable but should be harmonized or explicitly mapped.

### Chapter IV: Hasil dan Pembahasan

Readiness: Needs Minor Revision.

Chapter IV is scientifically the strongest chapter. It correctly reads the dataset as an operational knowledge artifact, Rule-Based as explicit representation, C4.5 as reconstruction, metrics as consistency evidence, and limitations as bounded validity.

Remaining issues:

- Section title `Analisis Representasi Komparatif` at `Hasil-dan-Pembahasan.tex:151` still contains comparison language, though the section text is careful.
- Some table language still uses `Model`, `prediksi`, `false positive`, and `false negative` at `Hasil-dan-Pembahasan.tex:165`, `188`, `205`, and `214`. This is acceptable when reporting official metrics, but it should be interpreted immediately as consistency evidence.
- Figure `KnowledgeReconstruction.png` at `Hasil-dan-Pembahasan.tex:285` is missing from the workspace.
- The discussion is now conceptually good, but it may be slightly too compressed; the scientific meaning of `Knowledge Representation Consistency` could be tied explicitly to the preceding path-mapping table.

### Chapter V: Kesimpulan

Readiness: Scientifically mostly aligned, structurally absent.

`Kesimpulan.tex` supports the intended conclusion: operational knowledge is acquired, formalized, represented explicitly, and reconstructed by Decision Tree. It avoids claiming model superiority and includes good limitations.

The critical issue is structural: `Kesimpulan.tex` is not included in `main.tex`. If the thesis is compiled as-is, this chapter does not exist in the final document.

Remaining wording issues:

- `Kesimpulan.tex:7` says `model keputusan`; `representation mechanism` would better match the final framing.
- `Kesimpulan.tex:9` uses `label akhir` and `data-driven` rather than `Guideline-Based Ground Truth` and `Decision Tree Reconstruction`.
- `Kesimpulan.tex:21` says the purpose is comparing representations. It should be framed as evaluating consistency between complementary representations.

## Terminology Consistency Audit

### Target Terms Used Well

The following target terms are used correctly and consistently in Chapters III and IV:

- `Operational Knowledge Formalization Framework`: `Metodologi.tex:5`, `12`, `16`; `Hasil-dan-Pembahasan.tex:224`, `324`, `342`.
- `Knowledge Acquisition`: `Metodologi.tex:7`, `16`, `20-22`; `Hasil-dan-Pembahasan.tex:5`, `228`.
- `Knowledge Structuring`: `Metodologi.tex:7`, `16`.
- `Knowledge Formalization`: `Metodologi.tex:16`, `43-45`; `Hasil-dan-Pembahasan.tex:5`, `228`.
- `Operational Dataset`: `Metodologi.tex:18`.
- `Operational Labeling Guideline`: `Metodologi.tex:18`, `132-134`; `Hasil-dan-Pembahasan.tex:7`, `230`, `334`.
- `Guideline-Based Ground Truth`: `Metodologi.tex:18`, `132`, `153`, `157`, `305`, `321`; `Hasil-dan-Pembahasan.tex:7`, `51`, `83`, `96`, `230`, `275`, `334-336`.
- `Rule-Based Representation`: `Metodologi.tex:18`, `157`, `159-161`; `Hasil-dan-Pembahasan.tex:290`.
- `Decision Tree Reconstruction`: `Metodologi.tex:18`, `295`; `Hasil-dan-Pembahasan.tex:290-292`.
- `Knowledge Representation Consistency Evaluation`: `Metodologi.tex:18`, `303-305`.
- `Priority Recommendation`: appears in English at `Hasil-dan-Pembahasan.tex:292`; Indonesian `rekomendasi prioritas` appears throughout.

### Outdated or Risky Terms to Flag

| Term | Locations |
|---|---|
| `performa` / performance comparison | `Pendahuluan.tex:13`, `21`, `30`, `44`; `Kajian-Pustaka.tex:178-206`; `main.tex:80-82` by implication |
| `komparasi` / comparison framing | `Pendahuluan.tex:13`, `21`, `30`; `Kajian-Pustaka.tex:6`, `18`, `22`, `39`; `Hasil-dan-Pembahasan.tex:151` |
| unqualified `ground truth` | `Abstrak-Indo.tex:23`; `Pendahuluan.tex:42`; `Kajian-Pustaka.tex:90` |
| `model klasifikasi` / classifier framing | `Pendahuluan.tex:11`, `43`, `44`; `Kajian-Pustaka.tex:6`, `37`, `90`, `122-126`, `180` |
| `prediksi` / prediction framing | `Pendahuluan.tex:11`; `Kajian-Pustaka.tex:28`, `30`, `124`, `180`, `182`, `188`, `218`, `222`; `Hasil-dan-Pembahasan.tex:188` |
| `label akhir` as conceptual term | `Kesimpulan.tex:9`, `21`; `Hasil-dan-Pembahasan.tex:185`, `304`, `334` |
| `Machine Learning` as future-work center | `Kesimpulan.tex:33-35` |

## Logical Consistency Audit

Current logical flow:

1. Chapter I opens with a real operational and knowledge problem.
2. Chapter II reviews document tracking, POD, Rule-Based systems, C4.5, and metrics.
3. Chapter III introduces the correct knowledge-engineering method.
4. Chapter IV interprets results under representation consistency.
5. Chapter V exists but is not compiled.

Main logical gaps:

1. Chapter I asks for performance comparison, while Chapter III executes knowledge formalization and representation consistency.
2. Chapter II explains evaluation metrics as predictive-performance tools, while Chapter III/IV interpret metrics as consistency indicators.
3. Chapter II does not prepare the reader for `Guideline-Based Ground Truth`, so Chapter III has to carry too much conceptual load.
4. Chapter III introduces `Knowledge Structuring` but does not give it a separate methodological treatment.
5. Chapter IV is conceptually aligned, but the compiled thesis has no Chapter V unless `main.tex` is updated.

## Contribution Consistency Audit

| Component | Supports Operational Knowledge Formalization Framework? | Assessment |
|---|---|---|
| Title | No | Method-comparison title conflicts with the contribution. |
| Abstract | Partially | Good final contribution sentence, but comparison and unqualified `ground truth` remain. |
| Chapter I | Partially | Operational problem is strong; research question/objective are inconsistent. |
| Chapter II | Partially | Relevant theory exists; emphasis is still prediction/classification. |
| Chapter III | Yes | Strongly aligned. |
| Chapter IV | Yes | Strongly aligned. |
| Chapter V | Mostly yes | Good conclusion, but not included in `main.tex`. |
| Positioning docs | Yes | Clear and should govern final revision. |

## Figure Consistency Audit

Major figure findings:

1. `Knowledge Formalization Framework.png` is included at `Metodologi.tex:11`, captioned at `Metodologi.tex:12`, labeled at `Metodologi.tex:13`, and discussed immediately at `Metodologi.tex:16-18`. Scientifically consistent, but the image file is missing.
2. `KnowledgeReconstruction.png` is included at `Hasil-dan-Pembahasan.tex:285`, captioned at `Hasil-dan-Pembahasan.tex:286`, labeled at `Hasil-dan-Pembahasan.tex:287`, and discussed before/after at `Hasil-dan-Pembahasan.tex:281` and `290-298`. Scientifically consistent, but the image file is missing.
3. Chapter II figures have labels but are not referenced: `fig:siklus_invoice_pod_b2b`, `fig:arsitektur_rule_based`, `fig:struktur_dasar_pohon_keputusan`, and `fig:confusion_matrix_biner`.
4. Chapter III system figures have labels but are not referenced: `fig:arsitektur_sistem`, `fig:use_case_diagram`, `fig:activity_pod`, and `fig:erd`.
5. No duplicate labels or unresolved references were found in the audited files.

Caption quality:

- The two final research figures have appropriate scientific captions.
- Generic theory and system-design figures mostly have descriptive captions, not scientific-purpose captions.

## Table Consistency Audit

Major table findings:

1. No duplicate table labels or unresolved table references were found.
2. Unused table labels: `tab:sumber_pengetahuan`, `tab:formalisasi_pengetahuan`, and `tab:fitur_dataset`.
3. Chapter IV tables are generally well referenced before and/or after appearance.
4. `tab:rule_base_priority` is referenced after the table at `Metodologi.tex:242`, but the table is very long for a normal `table` float and may have page-placement or overflow risk.
5. Table captions are generally clear, but several still use model-comparison language:
   - `Hasil-dan-Pembahasan.tex:159`: `Perbandingan Metrik Evaluasi pada Data Uji`.
   - `Hasil-dan-Pembahasan.tex:177`: `Perbandingan Karakteristik Rule-Based dan Decision Tree C4.5`.

## Citation Consistency Audit

Mechanical check:

- All `\cite{...}` keys used in the audited thesis files exist in `References.bib`.
- No missing bibliography keys were found.

Unsupported or under-supported claims:

1. `Pendahuluan.tex:5-9` contains broad claims about B2B administration, cash-flow impact, semi-manual work, spreadsheet use, tacit knowledge, and POD separation. Some may come from the case context, but they need either a source, observation/interview basis, or explicit statement that they are findings from the object of study.
2. `Kajian-Pustaka.tex:45-47` explains B2B invoice management and cash-flow consequences without citations.
3. `Kajian-Pustaka.tex:86-90` defines knowledge engineering, tacit knowledge, acquisition, and formalization without knowledge-engineering references.
4. `Kajian-Pustaka.tex:94-98` explains Rule-Based systems and inference architecture without citations.
5. `Kajian-Pustaka.tex:124-126` explains supervised learning/data-driven classification without citations.
6. `Kajian-Pustaka.tex:132-154` gives entropy, information gain, split information, and gain ratio formulas; C4.5 is cited at `Kajian-Pustaka.tex:130`, but the formulas would be stronger with direct support.
7. `Kajian-Pustaka.tex:180-206` explains evaluation metrics without citations.

## Writing Consistency Audit

Repetition:

- Chapter IV repeats the claim that metrics are consistency evidence in multiple locations. This is useful for defense but can be compressed slightly.
- Chapter III uses both a framework figure and several small formula-like arrays. The arrays are not wrong, but they can feel repetitive after the main framework figure.

Contradictions:

- Title/Chapter I say the thesis compares performance; Chapters III/IV say the thesis evaluates representation consistency.
- Chapter I says labels are `ground truth`; Chapters III/IV correctly say `Guideline-Based Ground Truth` is not independent external truth.
- Chapter II teaches metrics as predictive performance; Chapter IV interprets them as consistency evidence.

Unnecessary or risky paragraphs:

- `Kajian-Pustaka.tex:178-206` is too generic unless tied to `Knowledge Representation Consistency`.
- `Kesimpulan.tex:33-35` can dilute the contribution by moving future work toward broad ML exploration unless explicitly bounded by interpretability and knowledge representation.

## Defense Readiness: Ten Strong Examiner Questions

1. If the title says this is a comparison of Rule-Based and Decision Tree C4.5, why do Chapters III and IV say the real contribution is the `Operational Knowledge Formalization Framework`?
2. Why is `Guideline-Based Ground Truth` acceptable as an evaluation reference if it is derived from the same operational guideline used to build the Rule Base?
3. Is the Rule-Based result circular, and if so, why is that still scientifically meaningful?
4. What exactly is new in the `Operational Knowledge Formalization Framework` compared with a normal expert-system workflow?
5. Where is `Knowledge Structuring` performed in the methodology, and what artifacts prove that it occurred?
6. Why is Decision Tree C4.5 necessary if Rule-Based already represents the guideline perfectly?
7. Does a 1.000 score on 21 test records prove anything beyond internal consistency?
8. Why are features with zero importance still kept if the Decision Tree does not use them?
9. If customer rules change, which artifact must change first: the Operational Labeling Guideline, the Rule Base, the Operational Dataset, or the Decision Tree?
10. How can this framework be generalized to another company if the dataset, rules, and labels are all organization-specific?

## Overall Readiness Score

72/100

Rationale: Chapters III and IV are strong enough to support the final scientific claim, and Chapter V is mostly aligned. The score is held down by the comparison-oriented title, Chapter I research question/objective, Chapter II theory framing, missing final figure files, and the fact that `Kesimpulan.tex` is not included in `main.tex`.

## Final Recommendation

□ Needs Major Revision
