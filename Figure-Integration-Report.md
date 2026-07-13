# Figure Integration Report

## 1. Inserted Figure Locations

1. `Knowledge Formalization Framework.png`
   - File: `Metodologi.tex`
   - Location: Chapter III, Section `\textit{Proposed Method}`
   - Inserted at the beginning of the section after the opening framework paragraph.
   - Replaced the previous TikZ research-framework placeholder and removed the old placeholder label `fig:kerangka_penelitian`.

2. `KnowledgeReconstruction.png`
   - File: `Hasil-dan-Pembahasan.tex`
   - Location: Chapter IV, Section `Diskusi`
   - Inserted at the opening of the discussion section.
   - Replaced the previous boxed placeholder for the knowledge reconstruction concept.

## 2. Updated Captions

1. `\caption{Operational Knowledge Formalization Framework.}`
   - Label: `fig:knowledge_formalization_framework`

2. `\caption{Conceptual Illustration of Knowledge Reconstruction and Representation Consistency.}`
   - Label: `fig:knowledge_reconstruction`

## 3. Updated Surrounding Paragraphs

### Chapter III, Proposed Method

`Gambar~\ref{fig:knowledge_formalization_framework} memperlihatkan alur pengetahuan dalam \textit{Operational Knowledge Formalization Framework}. Alur tersebut dimulai dari \textit{Operational Knowledge} yang diperoleh melalui \textit{Knowledge Acquisition}, kemudian disusun melalui \textit{Knowledge Structuring} agar konsep operasional seperti batas \textit{cutoff}, jadwal penerimaan, dan kondisi prioritas memiliki posisi yang jelas dalam kerangka keputusan. Setelah itu, \textit{Knowledge Formalization} memisahkan pengetahuan ke dalam dua jalur yang saling melengkapi, yaitu \textit{Attribute Formalization} dan \textit{Rule Formalization}.`

`Melalui \textit{Attribute Formalization}, pengetahuan operasional diubah menjadi atribut dan \textit{Operational Dataset} yang dapat digunakan untuk rekonstruksi. Melalui \textit{Rule Formalization}, pengetahuan yang sama diubah menjadi \textit{Operational Labeling Guideline} yang menghasilkan \textit{Guideline-Based Ground Truth} serta \textit{Rule-Based Representation}. Kedua jalur tersebut kemudian bertemu pada \textit{Decision Tree Reconstruction} dan \textit{Knowledge Representation Consistency Evaluation} untuk menilai apakah makna operasional tetap setara dalam dua bentuk representasi. Hasil evaluasi tersebut menjadi dasar konseptual bagi \textit{Invoice Tracking and POD System}, sehingga rekomendasi prioritas ditempatkan sebagai bagian dari alur kerja operasional, bukan sebagai keluaran model yang berdiri sendiri.`

### Chapter IV, Discussion

`Gambar~\ref{fig:knowledge_reconstruction} memperlihatkan bahwa kontribusi penelitian tidak berhenti pada keluaran numerik, tetapi pada hubungan antara \textit{explicit operational knowledge}, \textit{Rule-Based Representation}, \textit{Decision Tree Reconstruction}, dan \textit{Guideline-Based Ground Truth}. Pengetahuan operasional yang telah diformalkan berperan sebagai sumber makna bersama. Dari sumber tersebut, Rule-Based menyatakan pengetahuan secara eksplisit melalui aturan, sedangkan Decision Tree merekonstruksi pola keputusan dari atribut operasional dan label referensi berbasis pedoman.`

`Kedua bentuk tersebut bersifat \textit{complementary representations}. Rule-Based menjaga keterbacaan administratif karena setiap \textit{Priority Recommendation} dapat ditelusuri ke kondisi operasional yang diformalkan. Decision Tree Reconstruction memberikan sudut pandang rekonstruktif karena struktur pohon memperlihatkan bagaimana atribut seperti jarak terhadap \textit{cutoff} dan jadwal penerimaan cukup untuk membentuk kembali makna keputusan yang sama. Dengan demikian, C4.5 tidak diposisikan sebagai pengganti pedoman, melainkan sebagai mekanisme untuk memeriksa apakah struktur pengetahuan dapat direkonstruksi dari data yang telah diberi \textit{Guideline-Based Ground Truth}.`

`Makna utama dari gambar tersebut adalah \textit{representation consistency}. Konsistensi tidak hanya berarti kesamaan keluaran, tetapi juga kesetaraan makna operasional antara representasi eksplisit dan rekonstruksi data-driven. Apabila dua representasi menghasilkan keputusan yang sama terhadap pedoman yang sama dan masih dapat dijelaskan melalui konsep operasional yang sama, maka keduanya mempertahankan \textit{equivalent operational meaning}.`

`Implikasi ilmiahnya adalah bahwa Knowledge Engineering menjadi pusat penelitian. Tanpa akuisisi, strukturisasi, dan formalisasi pengetahuan, atribut operasional hanya menjadi variabel data yang terpisah dari konteks administrasi. Setelah diformalkan, atribut dan aturan tersebut menjadi artefak pengetahuan yang dapat direpresentasikan, direkonstruksi, dan dievaluasi konsistensinya.`

`Implikasi praktisnya adalah bahwa hasil evaluasi dapat ditempatkan kembali dalam sistem pelacakan \textit{invoice} dan POD. Rekomendasi prioritas tidak berdiri sebagai label teknis semata, tetapi sebagai bagian dari alur informasi operasional yang mendukung pelacakan dokumen, penyimpanan POD, riwayat pengiriman, dan pengambilan keputusan administratif. Dengan demikian, gambar tersebut menegaskan bahwa nilai ilmiah penelitian terletak pada kemampuan mempertahankan makna pengetahuan operasional ketika pengetahuan tersebut bergerak dari pedoman eksplisit menuju rekonstruksi dan konteks sistem informasi.`

## 4. Cross-Reference Verification

- `fig:knowledge_formalization_framework` is cited immediately after the figure with `Gambar~\ref{fig:knowledge_formalization_framework}`.
- `fig:knowledge_reconstruction` is cited before and immediately after the figure with `Gambar~\ref{fig:knowledge_reconstruction}`.
- No duplicate labels were found for the two inserted figures.
- The old placeholder label `fig:kerangka_penelitian` is no longer present.
- The placeholder text for the Chapter IV reconstruction figure was removed.

## 5. LaTeX Compilation Risks

- The exact files `Knowledge Formalization Framework.png` and `KnowledgeReconstruction.png` are not currently present in the project root. A normal LaTeX compile will fail or produce missing-graphic output until both PNGs are added with exactly those filenames.
- The first filename contains spaces. The manuscript uses the exact `\includegraphics` command requested, so the final compile should be checked with the thesis LaTeX engine after the PNG file is present.
- No experimental results, metric values, tables, or numerical findings were modified.

## 6. Final Status

☐ Minor Manual Adjustment Required
