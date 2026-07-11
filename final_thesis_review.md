# Final Thesis Review Report

## 1. Executive Summary

The thesis has been reviewed from the perspective of a final academic examiner. The main scientific contribution is now consistent across the abstract, introduction, methodology, and results discussion: operational invoice-administration knowledge is acquired, formalized into an Operational Labeling Guideline, represented explicitly through a Rule-Based model, and reconstructed statistically by Decision Tree C4.5.

The most important submission-readiness issues were corrected. Chapter IV is now included in `main.tex`, the active `References.bib` file is populated, citation coverage is complete, and outdated "expert labeling" terminology has been replaced with the finalized guideline-based labeling narrative. The abstract and title metadata were also completed because they were previously empty.

Static LaTeX checks found no duplicate labels, no unresolved references, no missing bibliography keys, and no unused active bibliography entries. Full compilation could not be performed because no LaTeX compiler (`latexmk`, `pdflatex`, `lualatex`, `xelatex`, or `bibtex`) is installed in the current environment.

## 2. Issues Fixed

### Structural Fixes

- Added `\include{Hasil-dan-Pembahasan}` to `main.tex` so Chapter IV is included in the compiled thesis.
- Filled the empty Indonesian title and English title metadata in `main.tex`.
- Updated the approval page wording from proposal language to final thesis language in `Lembar-Persetujuan.tex`.

### Abstract and Contribution Alignment

- Completed `Abstrak-Indo.tex`, which was previously empty except for the heading and keyword label.
- Aligned the abstract with the final contribution: Knowledge Acquisition, Knowledge Formalization, Operational Labeling Guideline, Rule-Based representation, and Decision Tree reconstruction.
- Added appropriate keywords: invoice tracking, Proof of Delivery, Operational Labeling Guideline, Rule-Based System, and Decision Tree C4.5.

### Terminology Consistency

- Replaced obsolete references to `expert labeling`, `label pakar`, and `pakar domain` with:
  - `Operational Labeling Guideline`
  - `Guideline-Based Labeling`
  - operational knowledge / administrative operational knowledge
- Updated Chapter I and Chapter III so the thesis no longer claims that final labels were independently validated by a human expert.
- Preserved the role of operational knowledge acquisition without overstating expert validation.

### Cross-Chapter Consistency

- Aligned research questions, objectives, methodology, and Chapter IV interpretation around the final research design.
- Preserved the comparative framing: the study does not claim Decision Tree C4.5 is superior; it shows that C4.5 reconstructs formalized operational knowledge.
- Updated Chapter II wording so Rule-Based is described as based on formalized operational rules rather than "expert rules."

### Reference Review

- Populated the active `References.bib`, which was previously empty.
- Ensured every active citation key appears in the bibliography.
- Removed unused active bibliography entries by including only references cited in the current thesis.
- Corrected the placeholder `Unknown` author in the POD reference.
- Added missing bibliography entries for:
  - `Rim2020`
  - `nazifah_2023`
  - `Diwandari_Sela_Syahputra_Parama_Septiarini_2023`
- Reference metadata was checked against available publisher or indexing pages, including:
  - [Dharaningtyas and Nizar, 2021](https://www.ssbfnet.com/ojs/index.php/ijrbs/article/view/1091)
  - [Rim and Liu, 2020](https://thesai.org/Publications/ViewPaper?Code=IJACSA&Issue=10&SerialNo=6&Volume=11)
  - [Nazifah and Prianto, 2023](https://garuda.kemdiktisaintek.go.id/documents/detail/3691338)
  - [Diwandari et al., 2023](https://journals.itb.ac.id/index.php/jictra/article/view/18893)

### Figure, Table, and LaTeX Static Review

- Checked active labels and references: no duplicate labels and no unresolved `\ref{}` targets were found.
- Checked active citations and bibliography: no missing citation keys and no unused active bibliography keys were found.
- Verified Chapter IV figure and table references are discussed in surrounding text.
- Confirmed that the conceptual placeholder figure in Chapter IV remains intentionally marked for later professional replacement.

## 3. Remaining Minor Issues

1. `Kesimpulan.tex` does not exist in the project root. If the university format requires Chapter V, it must be added by the author or supervisor before submission.

2. `\PembimbingSatu` and `\NIPPembimbingSatu` are still empty in `main.tex`. These must be filled manually because advisor identity cannot be inferred safely.

3. The conceptual figure in Chapter IV is still a placeholder. It is scientifically useful, but it should be replaced with a professionally designed illustration before final printing.

4. Full LaTeX compilation could not be performed in this environment because no LaTeX toolchain is installed. The thesis should be compiled locally before submission.

5. The bibliography uses `plain` style while a comment in `main.tex` says "harvard style." This is not a scientific issue, but the style should be confirmed against faculty formatting rules.

## 4. Defense Readiness Assessment

### Five Strongest Points

1. The thesis has a clear scientific contribution: transforming operational invoice-administration knowledge into formal decision representations.

2. The comparison between Rule-Based and Decision Tree C4.5 is framed correctly as knowledge-driven representation versus data-driven reconstruction.

3. The final experiment uses the same dataset and same `final_label` ground truth for both models, supporting a fair comparison.

4. Chapter IV now interprets the results scientifically and does not overclaim Decision Tree superiority.

5. The thesis explicitly discusses threats to validity, especially guideline-based labeling, dataset size, and limited generalization.

### Five Weakest Points

1. The dataset is relatively small, so external generalization remains limited.

2. The final labels are guideline-based, not independently validated in the final experiment phase.

3. The perfect metric values may invite examiner questions about circularity, overfitting, or leakage.

4. The thesis still depends heavily on the clarity and completeness of the Operational Labeling Guideline.

5. The system-design contribution is present, but the strongest scientific contribution is the knowledge formalization and reconstruction analysis.

### Likely Defense Questions and Suggested Answers

**Question 1: If both models achieve the same metric values, what is the real contribution of the research?**  
Suggested answer: The contribution is not proving that one model is superior. The contribution is showing that operational knowledge can be formalized into explicit Rule-Based rules and that the same formalized knowledge can be reconstructed by Decision Tree C4.5 from operational data.

**Question 2: Does perfect agreement mean the models are universally accurate?**  
Suggested answer: No. The result indicates consistency with the Operational Labeling Guideline on the finalized dataset. It should not be interpreted as universal superiority or proof that the model will perform identically in other organizations or periods.

**Question 3: Why is Guideline-Based Labeling acceptable as ground truth?**  
Suggested answer: The objective is to compare two representations of the same formalized operational knowledge. The labels are generated consistently from the Operational Labeling Guideline developed through Knowledge Acquisition and Knowledge Formalization, so they are appropriate for evaluating consistency with that formalized knowledge.

**Question 4: Did Decision Tree C4.5 discover new operational knowledge?**  
Suggested answer: No substantial new operational knowledge was found. The tree compressed and reconstructed the existing guideline into fewer decision paths, mainly using `days_to_cutoff_decision_time`, receive-day information, and schedule-gap features.

**Question 5: What is the practical value of the Rule-Based model if Decision Tree can reconstruct the guideline?**  
Suggested answer: The Rule-Based model is transparent, auditable, and easier to maintain when customer regulations change. Decision Tree is useful for analyzing feature dominance and checking whether data patterns align with the formalized operational guideline.

## 5. Suggested Final Checklist before Submission

- Fill in `\PembimbingSatu` and `\NIPPembimbingSatu` in `main.tex`.
- Confirm whether the university requires a Chapter V conclusion file. If required, add `Kesimpulan.tex` and include it in `main.tex`.
- Replace the Chapter IV conceptual placeholder figure with a final designed illustration.
- Compile the thesis locally with LaTeX and BibTeX.
- Check PDF output for overfull tables, figure placement, and page breaks.
- Confirm bibliography style with the faculty template requirements.
- Confirm that the final PDF includes Cover, Approval Page, Abstract, Chapters I-IV, Bibliography, and Appendices.
- Re-read Chapter IV orally once to prepare for defense questions about perfect metrics and guideline-based labeling.
