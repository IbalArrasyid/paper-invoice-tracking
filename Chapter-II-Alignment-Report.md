# Chapter II Alignment Report

## Changed Sections

1. Tinjauan Pustaka opening paragraph
   - Reframed the chapter introduction from decision-model classification and algorithm comparison toward document tracking, POD, operational knowledge engineering, knowledge representation, and the Operational Knowledge Formalization Framework.
   - Preserved the existing citation structure and table reference.

2. Post-table research positioning narrative
   - Revised the discussion after Table 2.1 so that prior studies are synthesized as separate streams: document tracking, POD, Decision Tree interpretability, and operational knowledge representation.
   - Replaced the old gap around C4.5 limitations and model comparison with the gap around lack of Operational Knowledge Formalization that bridges Operational Knowledge, explicit Rule-Based representation, and statistical reconstruction in the Invoice Tracking and POD context.

3. Akuisisi dan Formalisasi Pengetahuan
   - Expanded the theoretical role of Knowledge Engineering as the center of Chapter II.
   - Clarified Operational Knowledge, tacit knowledge, explicit knowledge, Knowledge Acquisition, Knowledge Structuring, and Knowledge Formalization.
   - Replaced unqualified ground truth wording with Operational Labeling Guideline and Guideline-Based Ground Truth.

4. Pendekatan Rule-Based System
   - Repositioned Rule-Based as Rule-Based Representation, not as a competing algorithm.
   - Added the scientific rationale for transparency, traceability, auditability, and maintainability.
   - Clarified that Rule-Based is an explicit representation of formalized operational knowledge whose consistency can be checked against data-driven reconstruction.

5. Konsep Dasar Klasifikasi Data-Driven
   - Renamed the subsection to Rekonstruksi Pengetahuan Berbasis Data.
   - Reframed data-driven learning as data-driven knowledge reconstruction from formal operational attributes and Guideline-Based Ground Truth.
   - Removed the old emphasis on prediction and comparison with a knowledge-driven model.

6. Mekanisme Algoritma C4.5
   - Renamed the subsection to Mekanisme Decision Tree C4.5 untuk Rekonstruksi Pengetahuan.
   - Repositioned C4.5 as Decision Tree Reconstruction for reconstructing interpretable operational decision paths.
   - Preserved the entropy, information gain, split information, and gain ratio formulas.

7. Metrik Evaluasi Performa
   - Renamed the subsection to Metrik Evaluasi Konsistensi Representasi.
   - Reinterpreted Accuracy, Precision, Recall, F1-Score, and Confusion Matrix as indicators of Knowledge Representation Consistency against Guideline-Based Ground Truth.
   - Removed wording that framed the metrics as proof of model superiority or general predictive performance.

## Scientific Rationale

The revision aligns Chapter II with the thesis contribution as an Operational Knowledge Formalization Framework. The theoretical flow now supports Chapter III by establishing that operational decisions must first be acquired, structured, formalized, represented, and then evaluated for consistency.

Rule-Based is now presented as explicit knowledge representation. Decision Tree C4.5 is now presented as reconstruction of operational decision paths from formalized attributes. Evaluation metrics are now used to assess representation consistency, not to rank algorithms.

## Terminology Replacements

- Performance evaluation -> representation consistency evaluation.
- Prediction -> priority recommendation, output, or reconstruction, depending on context.
- Ground truth -> Guideline-Based Ground Truth.
- Model comparison -> consistency evaluation between representations.
- Model/classification emphasis -> knowledge representation and knowledge reconstruction emphasis.
- Rule-Based algorithm framing -> Rule-Based Representation.
- Decision Tree prediction framing -> Decision Tree Reconstruction.

## Remaining Issues

- Table 2.1 still contains original table wording such as Metode/Algoritma, komparasi, prediksi, klasifikasi, and dibandingkan. These were intentionally left unchanged because the instruction explicitly prohibited modifying tables.
- The Confusion Matrix figure still contains the conventional labels Prediksi Positif, Prediksi Negatif, and the caption Klasifikasi Biner. These were intentionally left unchanged because the instruction explicitly prohibited modifying figures.
- The surrounding prose now clarifies that those conventional metric labels are interpreted in this thesis as keluaran mekanisme representasi and Knowledge Representation Consistency.

## Files Modified

- Kajian-Pustaka.tex
- Chapter-II-Alignment-Report.md

No experiments, datasets, references, figures, tables, or other chapters were modified.
