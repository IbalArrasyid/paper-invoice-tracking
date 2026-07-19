# Rencana Pemutakhiran Referensi

Tanggal penelusuran: 20 Juli 2026

## Tujuan

Dokumen ini merencanakan pemutakhiran referensi untuk evaluasi machine learning, sistem berbasis aturan, pelacakan dokumen dan POD, serta sistem pendukung keputusan. Pemutakhiran referensi tidak boleh mengubah metodologi final, hasil eksperimen, atau posisi penelitian sebagai analisis komparatif antara Rule-Based berbasis SOP dan Decision Tree berbasis data historis admin.

## Keputusan Umum

1. Referensi lama tidak dihapus hanya karena tahun terbitnya. Referensi fondasional tetap dipertahankan ketika mendukung definisi asli atau perkembangan historis.
2. Referensi terbaru digunakan untuk mendukung praktik evaluasi modern, interpretabilitas, human-AI decision support, dan konteks digitalisasi logistik.
3. Neuro-symbolic AI, automatic rule extraction, blockchain, cloud, dan RAG tidak boleh ditulis sebagai metode penelitian ini karena tidak diimplementasikan.
4. Paper tentang rule extraction hanya dapat ditempatkan pada penelitian terdahulu atau saran penelitian selanjutnya. Rule-Based penelitian tetap dibangun secara manual dari SOP.
5. Paper blockchain hanya dapat mendukung konteks traceability modern. Paper tersebut tidak membuktikan bahwa sistem penelitian menggunakan arsitektur blockchain.

## Verifikasi Dampak Metodologis Prioritas 1

| Referensi | Hasil verifikasi repository | Keputusan penggunaan |
|---|---|---|
| `RainioEtAl2024` | Pipeline melaporkan confusion matrix, accuracy, precision kelas Urgent, recall kelas Urgent, F1 kelas Urgent, macro F1, FP, dan FN. Exact McNemar dihitung dari prediksi berpasangan pada invoice yang sama. | Digunakan untuk menjustifikasi pembacaan multi-metrik dan pemilihan uji berpasangan. Tidak digunakan sebagai sitasi dekoratif. |
| `BatesEtAl2024CV` | Pemilihan parameter dilakukan melalui validasi internal pada data latih setiap fold luar. E3 menggabungkan prediksi out-of-fold, tetapi penelitian tidak menghitung interval kepercayaan atau estimasi varians CV khusus. | Digunakan untuk membatasi interpretasi: fold tidak dianggap replikasi independen dan tidak ada klaim uncertainty estimation. Tidak diklaim bahwa seluruh prosedur inferensi Bates telah diimplementasikan. |
| `RudinEtAl2022` | Kompleksitas Decision Tree dikendalikan melalui `max_depth` dan `min_samples_leaf`. Pohon hasil evaluasi memiliki kedalaman 2--3 dan pohon interpretatif penuh memiliki kedalaman 2 dengan 4 daun. | Digunakan untuk mendukung keterperiksaan struktural. Naskah menyatakan bahwa pemahaman manusia belum divalidasi melalui studi admin. |
| `StoreyEtAl2024` | Sistem menghasilkan rekomendasi prioritas, sedangkan keputusan akhir tetap berada pada admin. | Digunakan untuk memosisikan sistem sebagai dukungan keputusan manusia-AI, bukan pengganti pengambil keputusan. |

Metadata resmi juga menunjukkan bahwa nama penulis pertama `RainioEtAl2024` adalah Oona Rainio, bukan Oskari Rainio. Entri BibTeX menggunakan metadata yang telah dikoreksi.

## A. Evaluasi dan Metrik Kinerja

### Referensi Utama yang Direkomendasikan

| Citation key usulan | Referensi terverifikasi | Fungsi dalam skripsi | Prioritas |
|---|---|---|---|
| `RainioEtAl2024` | Rainio, O., Teuho, J., dan Klén, R. (2024). [Evaluation Metrics and Statistical Tests for Machine Learning](https://doi.org/10.1038/s41598-024-56706-x). *Scientific Reports*, 14, 6086. | Confusion matrix, accuracy, precision, recall, F1-score, pemilihan uji statistik, dan McNemar dalam evaluasi ML modern. | Wajib |
| `BatesEtAl2024CV` | Bates, S., Hastie, T., dan Tibshirani, R. (2024). [Cross-Validation: What Does It Estimate and How Well Does It Do It?](https://doi.org/10.1080/01621459.2023.2197686). *Journal of the American Statistical Association*, 119(546), 1434--1445. | Makna estimasi cross-validation, ketergantungan antar-fold, keterbatasan estimasi varians, dan interpretasi hasil CV. | Wajib |
| `Opitz2024Metrics` | Opitz, J. (2024). [A Closer Look at Classification Evaluation Metrics and a Critical Reflection of Common Evaluation Practice](https://doi.org/10.1162/tacl_a_00675). *Transactions of the Association for Computational Linguistics*, 12, 820--836. | Alasan pemilihan metrik dan kehati-hatian dalam membaca macro F1. Konteks artikelnya dominan NLP sehingga digunakan sebagai pendamping, bukan satu-satunya sumber. | Pendamping |
| `KapoorNarayanan2023` | Kapoor, S., dan Narayanan, A. (2023). [Leakage and the Reproducibility Crisis in Machine-Learning-Based Science](https://doi.org/10.1016/j.patter.2023.100804). *Patterns*, 4(9), 100804. | Pencegahan data leakage dan pemisahan proses yang belajar dari data. Entri sudah tersedia dalam `References.bib`. | Pertahankan |
| `JamesEtAl2023` | James, G., Witten, D., Hastie, T., Tibshirani, R., dan Taylor, J. (2023). [An Introduction to Statistical Learning: With Applications in Python](https://doi.org/10.1007/978-3-031-38747-0). Springer. | Definisi supervised classification, hold-out, cross-validation, Decision Tree, dan evaluasi prediksi. Entri sudah tersedia dalam `References.bib`. | Pertahankan |

### Keputusan terhadap Referensi Lama

| Referensi lama | Keputusan | Pengganti atau pendamping | Alasan ilmiah |
|---|---|---|---|
| Sokolova dan Lapalme (2009) | Ganti pada sitasi aktif metrik | Rainio et al. (2024) | Rainio membahas metrik klasifikasi dan pemilihan uji statistik dalam konteks ML modern. Sokolova dapat tetap berada di bibliografi atau digunakan sebagai sumber historis analisis metrik. |
| Arlot dan Celisse (2010) | Pertahankan sebagai survei fondasional, tambahkan sumber baru | Bates et al. (2024) dan James et al. (2023) | Arlot masih relevan untuk taksonomi prosedur CV dan LOOCV. Bates memperbarui interpretasi statistik dan keterbatasan CV. |
| Kohavi (1995) | Pertahankan hanya untuk temuan historis tentang stratifikasi | James et al. (2023), Bates et al. (2024), dan Kapoor dan Narayanan (2023) | Kohavi tetap relevan untuk stratified CV. Praktik evaluasi umum dan pencegahan leakage sebaiknya didukung sumber yang lebih baru. |
| Dietterich (1998) | Ganti pada panduan praktis uji statistik, pertahankan bila membahas sejarah perbandingan classifier | Rainio et al. (2024) | Rainio memberikan panduan modern tentang data berpasangan, pemilihan uji, dan McNemar. Dietterich tetap bernilai sebagai referensi metodologis klasik. |

### Rencana Penempatan

- `Kajian-Pustaka.tex`, Confusion Matrix sampai F1-score: gunakan `RainioEtAl2024`; `SokolovaLapalme2009` menjadi opsional.
- `Kajian-Pustaka.tex`, Hold-out, Cross Validation, dan LOOCV: gunakan kombinasi `JamesEtAl2023`, `BatesEtAl2024CV`, dan `Kohavi1995` khusus untuk stratifikasi.
- `Kajian-Pustaka.tex`, McNemar Test: gunakan `McNemar1947` dan `RainioEtAl2024`; `Dietterich1998` dapat dipertahankan sebagai pendamping.
- `Hasil-dan-Pembahasan.tex`, interpretasi distribusi kelas: ganti sitasi tunggal `SokolovaLapalme2009` dengan `RainioEtAl2024` atau gunakan keduanya.
- `Hasil-dan-Pembahasan.tex`, interpretasi Exact McNemar: gunakan `RainioEtAl2024` bersama sumber asli `McNemar1947`.

## B. Sistem Berbasis Aturan dan Interpretabilitas

### Referensi Utama yang Direkomendasikan

| Citation key usulan | Referensi terverifikasi | Fungsi dalam skripsi | Prioritas |
|---|---|---|---|
| `RudinEtAl2022` | Rudin, C., Chen, C., Chen, Z., Huang, H., Semenova, L., dan Zhong, C. (2022). [Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges](https://doi.org/10.1214/21-SS133). *Statistics Surveys*, 16, 1--85. | Interpretabilitas model, model logis yang ringkas, dan Decision Tree sebagai model intrinsik yang dapat diperiksa. | Wajib |
| `KiernerEtAl2023` | Kierner, S., Kucharski, J., dan Kierner, Z. (2023). [Taxonomy of Hybrid Architectures Involving Rule-Based Reasoning and Machine Learning in Clinical Decision Systems: A Scoping Review](https://doi.org/10.1016/j.jbi.2023.104428). *Journal of Biomedical Informatics*, 144, 104428. | Konteks modern hubungan rules dan machine learning serta arsitektur paralel. Domainnya klinis sehingga digunakan untuk konsep arsitektur, bukan bukti pada domain invoice. | Pendamping |
| `KovasHatzilygeroudis2024` | Kovas, K., dan Hatzilygeroudis, I. (2024). [ACRES: A Framework for (Semi)automatic Generation of Rule-Based Expert Systems with Uncertainty from Datasets](https://doi.org/10.1111/exsy.13723). *Expert Systems*, 41(12), e13723. | Contoh pembentukan aturan otomatis dari data. Hanya untuk penelitian terdahulu atau saran penelitian selanjutnya. | Opsional |
| `GengEtAl2024` | Geng, X., Ma, H., Jiao, L., dan Zhou, Z.-J. (2024). [Data- and Knowledge-Driven Belief Rule Learning for Hybrid Classification](https://doi.org/10.1016/j.ins.2024.121201). *Information Sciences*, 681, 121201. | Contoh integrasi pengetahuan ahli dan data dalam klasifikasi hybrid. Tidak menggambarkan metode penelitian saat ini. | Opsional |
| `BalcanSharma2024` | Balcan, M.-F., dan Sharma, D. (2024). [Learning Accurate and Interpretable Decision Trees](https://proceedings.mlr.press/v244/balcan24a.html). *Proceedings of the 40th Conference on Uncertainty in Artificial Intelligence*, PMLR 244, 288--307. | Interpretabilitas, kompleksitas, dan trade-off akurasi pada Decision Tree. Metadata diverifikasi melalui PMLR. | Pendamping |
| `GarcezLamb2023` | Garcez, A. d'Avila, dan Lamb, L. C. (2023). [Neurosymbolic AI: The 3rd Wave](https://doi.org/10.1007/s10462-023-10448-w). *Artificial Intelligence Review*, 56(11), 12387--12406. | Konteks umum integrasi pembelajaran dan penalaran simbolik. Hanya diperlukan jika Bab II menambahkan konteks neuro-symbolic secara singkat. | Opsional |

### Keputusan terhadap Referensi Lama

| Referensi lama | Keputusan | Pendamping modern | Alasan ilmiah |
|---|---|---|---|
| Buchanan dan Shortliffe (1984) | Pertahankan | Rudin et al. (2022) dan Kierner et al. (2023) | Sumber ini tetap relevan untuk struktur klasik knowledge base, inference, dan aturan IF--THEN. Literatur hybrid tidak menggantikan definisi sistem pakar klasik. |
| Studer et al. (1998) | Pertahankan | Kovas dan Hatzilygeroudis (2024) hanya sebagai konteks perkembangan | Studer mendukung proses Knowledge Acquisition dan knowledge modeling yang benar-benar digunakan. Automatic rule generation merupakan metode berbeda. |
| Meseguer (1992) | Pertahankan | Tidak ada pengganti langsung yang lebih tepat untuk metodologi final | Meseguer membedakan verification, validation, evaluation, dan testing pada expert system. Paper V&V modern yang ditemukan berfokus pada neuro-symbolic atau learning-enabled systems, bukan validasi Rule Base SOP. |

### Batas Penggunaan

- Jangan menulis bahwa penelitian menggunakan neuro-symbolic AI.
- Jangan menulis bahwa aturan Rule-Based diekstraksi dari Decision Tree.
- Jangan menulis bahwa Rule-Based dan Decision Tree membentuk model hybrid.
- `KovasHatzilygeroudis2024` dan `GengEtAl2024` hanya mendukung arah penelitian selanjutnya.
- `KiernerEtAl2023` dapat digunakan untuk menunjukkan bahwa rules dan ML dapat ditempatkan secara paralel, tetapi penelitian ini tetap melakukan perbandingan dua classifier, bukan integrasi model.

### Rencana Penempatan

- `Kajian-Pustaka.tex`, Rule-Based System: pertahankan `BuchananShortliffe1984` dan `LiuEtAl2016RuleBased`; tambahkan `RudinEtAl2022` untuk interpretabilitas modern.
- `Kajian-Pustaka.tex`, Knowledge Acquisition dan Rule Construction: pertahankan `StuderEtAl1998` dan `Meseguer1992`.
- `Kajian-Pustaka.tex`, Decision Tree: tambahkan `BalcanSharma2024` bila diperlukan untuk membahas pohon yang ringkas dan dapat diperiksa.
- `Kajian-Pustaka.tex`, Penelitian Terdahulu: tambahkan `KiernerEtAl2023`; tempatkan `KovasHatzilygeroudis2024` dan `GengEtAl2024` hanya sebagai pendekatan yang berbeda dari penelitian ini.
- `Hasil-dan-Pembahasan.tex`, karakteristik operasional: tambahkan `RudinEtAl2022` untuk memperkuat interpretasi explainability tanpa menghapus bukti internal berupa Rule ID dan kedalaman pohon.

## C. Pelacakan Dokumen, POD, dan Sistem Pendukung Keputusan

### Referensi Utama yang Direkomendasikan

| Citation key usulan | Referensi terverifikasi | Fungsi dalam skripsi | Prioritas |
|---|---|---|---|
| `StoreyEtAl2024` | Storey, V. C., Hevner, A. R., dan Yoon, V. Y. (2024). [The Design of Human-Artificial Intelligence Systems in Decision Sciences: A Look Back and Directions Forward](https://doi.org/10.1016/j.dss.2024.114230). *Decision Support Systems*, 182, 114230. | Posisi sistem sebagai dukungan keputusan sosio-teknis dan pembagian peran manusia dengan AI. | Wajib |
| `LinEtAl2026POD` | Lin, H.-J., Lin, H.-P., dan Hsieh, I.-Y. L. (2026). [Digitalization and Decarbonization in Last-Mile Logistics: A Life Cycle Assessment of Proof of Delivery Systems](https://doi.org/10.1080/19427867.2026.2623085). *Transportation Letters*. | Konteks langsung digitalisasi POD. Entri sudah tersedia dalam `References.bib`. | Pertahankan |
| `AzevedoEtAl2023` | Azevedo, P., Gomes, J., dan Romão, M. (2023). [Supply Chain Traceability Using Blockchain](https://doi.org/10.1007/s12063-023-00359-y). *Operations Management Research*, 16, 1359--1381. | Traceability, provenance, chain of custody, dan audit trail dalam sistem logistik modern. Blockchain hanya konteks penelitian terdahulu. | Pendamping |
| `CulottaEtAl2024` | Culotta, C., Blome, C., dan Henke, M. (2024). [Theories of Digital Platforms for Supply Chain Management: A Systematic Literature Review](https://doi.org/10.1108/IJPDLM-01-2023-0016). *International Journal of Physical Distribution and Logistics Management*, 54(5), 449--475. | Konteks digital platform dalam supply chain. Tidak digunakan untuk mengklaim arsitektur sistem penelitian. | Opsional |
| `WuEtAl2023Traceability` | Wu, H., Jiang, S., dan Cao, J. (2023). [High-Efficiency Blockchain-Based Supply Chain Traceability](https://doi.org/10.1109/TITS.2022.3205445). *IEEE Transactions on Intelligent Transportation Systems*, 24(4), 3748--3758. | Contoh traceability terdesentralisasi dan isu efisiensi pencarian rekaman. Hanya untuk penelitian terdahulu. | Opsional |

### Keputusan terhadap Referensi Lama

| Referensi lama | Keputusan | Pengganti atau pendamping | Alasan ilmiah |
|---|---|---|---|
| Sunindyo et al. (2014) | Pertahankan hanya sebagai penelitian terdahulu Indonesia | Lin et al. (2026) dan Azevedo et al. (2023) | Sunindyo tetap relevan untuk konteks document tracking pemerintah lokal, tetapi bukan dasar arsitektur modern atau evaluasi classifier. |
| Shim et al. (2002) | Ganti pada klaim aktif tentang DSS modern | Storey et al. (2024) | Storey membahas DSS kontemporer sebagai human-AI socio-technical system dan mendukung posisi keluaran model sebagai bantuan bagi pengambil keputusan. Shim dapat tetap digunakan untuk sejarah perkembangan DSS. |

### Batas Penggunaan

- Jangan menambahkan RAG karena penelitian tidak menggunakan retrieval-augmented generation.
- Jangan menyatakan sistem berbasis cloud, microservices, atau blockchain tanpa bukti implementasi pada repository.
- Jangan memakai paper blockchain untuk membenarkan fungsi POD dasar. Gunakan `LinEtAl2026POD` untuk POD dan paper blockchain hanya untuk konteks traceability.
- Jangan mengganti penelitian terdahulu Indonesia hanya karena sumbernya lebih lama. Relevansi domain dan lokasi tetap bernilai.

### Rencana Penempatan

- `Pendahuluan.tex`, konteks pelacakan invoice dan POD: gunakan `LinEtAl2026POD`; pertahankan Sunindyo hanya bila konteks e-government Indonesia diperlukan.
- `Kajian-Pustaka.tex`, Invoice Tracking dan Proof of Delivery: gunakan `LinEtAl2026POD` dan, bila diperlukan, `AzevedoEtAl2023` untuk konsep traceability.
- `Kajian-Pustaka.tex`, Penelitian Terdahulu: pertahankan Sunindyo dan tambahkan Azevedo sebagai perkembangan sistem traceability modern.
- `Kajian-Pustaka.tex`, konteks DSS: gunakan `StoreyEtAl2024`; pindahkan `ShimEtAl2002` menjadi sumber historis.
- `Hasil-dan-Pembahasan.tex`, posisi rekomendasi sebagai bantuan admin: ganti atau dampingi `ShimEtAl2002` dengan `StoreyEtAl2024`.

## Prioritas Implementasi

### Prioritas 1: Telah ditambahkan dan digunakan

- `RainioEtAl2024`
- `BatesEtAl2024CV`
- `RudinEtAl2022`
- `StoreyEtAl2024`

Status: seluruh referensi Prioritas 1 telah ditambahkan ke `References.bib` dan digunakan secara aktif pada Bab II--IV. Integrasi dilakukan tanpa mengubah kode, data, atau hasil eksperimen.

### Prioritas 2: Tambahkan secara selektif

- `Opitz2024Metrics`
- `KiernerEtAl2023`
- `BalcanSharma2024`
- `AzevedoEtAl2023`

### Prioritas 3: Hanya penelitian terdahulu atau saran

- `KovasHatzilygeroudis2024`
- `GengEtAl2024`
- `GarcezLamb2023`
- `CulottaEtAl2024`
- `WuEtAl2023Traceability`

## Referensi yang Tidak Direkomendasikan sebagai Sumber Inti

1. Artikel e-POD yang tidak memiliki bukti indeks atau menggunakan blog komersial sebagai dasar utama.
2. Paper blockchain yang tidak sesuai dengan arsitektur sistem penelitian.
3. Paper RAG atau LLM karena tidak berkaitan dengan metode dan artefak penelitian final.
4. Review cross-validation dari penerbit yang reputasi dan proses telaahnya belum jelas, meskipun memiliki DOI.
5. Preprint ketika tersedia artikel jurnal atau prosiding resmi yang mendukung klaim yang sama.

## Urutan Implementasi yang Aman

1. Tambahkan entri BibTeX Prioritas 1 tanpa menghapus entri lama.
2. Perbarui sitasi Bab II pada subbab metrik, cross-validation, McNemar, Rule-Based, Decision Tree, POD, dan DSS.
3. Perbarui sitasi pendukung di Bab I dan Bab IV tanpa mengubah kalimat hasil atau metodologi.
4. Tambahkan referensi Prioritas 2 hanya jika terdapat klaim yang benar-benar memerlukannya.
5. Jangan memasukkan referensi Prioritas 3 ke metodologi sebagai metode yang digunakan.
6. Kompilasi dokumen dan periksa seluruh citation key yang belum terdefinisi.
7. Lakukan audit bibliografi terakhir untuk duplikasi, metadata, DOI, dan konsistensi format.

## Hasil yang Diharapkan

Setelah rencana ini diterapkan, referensi evaluasi ML dan DSS akan memiliki dukungan 2023--2024, konteks POD akan didukung sumber langsung tahun 2026 yang sudah tersedia, dan teori Rule-Based tetap memiliki fondasi klasik yang tepat serta pendamping modern. Pemutakhiran tersebut memperkuat kebaruan literatur tanpa mengubah penelitian menjadi neuro-symbolic, hybrid, blockchain, cloud, atau RAG.
