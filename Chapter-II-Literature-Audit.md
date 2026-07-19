# Audit Literatur Bab II

**Status:** Blueprint bibliografi sebelum revisi `Kajian-Pustaka.tex`.

**Ruang lingkup:** Landasan teori, penelitian terdahulu, research gap, dan kualitas daftar pustaka. Tidak ada file LaTeX atau hasil eksperimen yang diubah.

## 1. Kesimpulan Audit

Daftar pustaka saat ini belum memadai. `References.bib` hanya memuat 10 sumber. Sebagian besar merupakan studi konteks, bukan sumber teori utama. Belum tersedia rujukan yang kuat untuk Rule-Based System, Knowledge Acquisition, Rule Construction, supervised classification, hold-out validation, cross-validation, LOOCV, data leakage, metrik klasifikasi, dan exact McNemar.

Korpus final yang direkomendasikan berisi 26 sumber. Sebanyak 22 sumber dinilai bereputasi berdasarkan peer review, indeks Scopus/WoS, penerbit akademik utama, atau forum ilmiah utama. Empat sumber tidak dihitung sebagai sumber bereputasi: dua jurnal SINTA 3, satu sumber dengan status indeks yang masih perlu diverifikasi, dan dokumentasi resmi scikit-learn.

**Perhitungan konservatif:**

- Total sumber: 26.
- Sumber bereputasi: 22.
- Sumber pendukung yang tidak dihitung: 4.
- Persentase bereputasi: `22 / 26 x 100% = 84,62%`.
- Target minimal 80%: **terpenuhi**.

Quartile dapat berubah setiap tahun. Status Q1-Q4 pada dokumen ini mengacu pada data 2024 yang ditemukan saat audit atau kategori terbaik yang dilaporkan. Status harus diperiksa kembali melalui Scopus Sources atau SCImago sebelum naskah final dikumpulkan.

## 2. Koreksi Struktur Bab II

Blueprint sebelumnya belum memisahkan hold-out validation. Tambahkan satu subbab dan geser nomor setelahnya:

1. 2.15 Hold-out Validation.
2. 2.16 Cross Validation.
3. 2.17 Leave-One-Out Cross Validation.
4. 2.18 McNemar Test.
5. 2.19 Penelitian Terdahulu.
6. 2.20 Research Gap.

Penambahan ini diperlukan karena E1 dan E2 menggunakan hold-out, sedangkan E3 dan E4 menggunakan prosedur yang berbeda.

## 3. Kecukupan Literatur per Subbab

| Subbab | Kondisi Saat Ini | Status | Referensi Inti yang Direkomendasikan | Alasan |
|---|---|---|---|---|
| Invoice Tracking | Hanya Sunindyo dan sumber web-tracking yang kualitasnya tidak pasti | Sebagian | Sunindyo et al. (2014); Schoonbee et al. (2022) | Sunindyo menjelaskan document tracking; Schoonbee memberi konteks invoice dan DSS. |
| Proof of Delivery | Satu studi proses POD dengan reputasi belum terverifikasi | Kurang | Lin et al. (2026); Dharaningtyas dan Nizar (2021) sebagai pendukung | Lin memberi bukti peer-reviewed mutakhir tentang konfigurasi POD digital. |
| Rule-Based System | Belum memiliki teori utama | Tidak cukup | Buchanan dan Shortliffe (1984); Liu et al. (2016); Ben-David (2008) | Mencakup arsitektur aturan, rule base, interpretability, dan maintainability. |
| Knowledge Acquisition | Tidak ada sumber utama | Tidak cukup | Studer et al. (1998); Buchanan dan Shortliffe (1984) | Menjelaskan perolehan dan pemodelan pengetahuan untuk knowledge-based system. |
| Rule Construction | Tidak ada sumber verifikasi aturan | Tidak cukup | Meseguer (1992); Ben-David (2008) | Mendukung validasi, redundansi, konsistensi, dan pemeliharaan rule base. |
| Decision Tree | Sumber lama berfokus pada C4.5 | Tidak sesuai | Quinlan (1986); Breiman et al. (1984); James et al. (2023); Pedregosa et al. (2011) | Memisahkan teori ID3/CART dari implementasi library. |
| Entropy | Dijelaskan sebagai bagian C4.5 | Tidak sesuai | Quinlan (1986); James et al. (2023); dokumentasi scikit-learn | Entropy dijelaskan sebagai impurity criterion, bukan bukti implementasi C4.5. |
| ID3, C4.5, CART | Belum dibedakan secara akurat | Tidak cukup | Quinlan (1986, 1993); Breiman et al. (1984); dokumentasi scikit-learn | Sumber primer untuk tiap keluarga algoritma. |
| Supervised Classification | Hanya uraian umum tanpa sumber kuat | Kurang | James et al. (2023); Pedregosa et al. (2011); Kapoor dan Narayanan (2023) | Mendukung training-validation separation dan data leakage. |
| Confusion Matrix | Belum memiliki sumber metodologis | Tidak cukup | Sokolova dan Lapalme (2009); James et al. (2023) | Menjelaskan TP, TN, FP, FN dan hubungan dengan metrik. |
| Accuracy | Formula tersedia tanpa basis literatur kuat | Kurang | Sokolova dan Lapalme (2009) | Mendukung definisi dan keterbatasan accuracy. |
| Precision | Formula tersedia tanpa basis literatur kuat | Kurang | Sokolova dan Lapalme (2009) | Mendukung interpretasi kesalahan positif. |
| Recall | Formula tersedia tanpa basis literatur kuat | Kurang | Sokolova dan Lapalme (2009) | Mendukung hubungan recall dan false negative. |
| F1-score | Formula tersedia tanpa basis literatur kuat | Kurang | Sokolova dan Lapalme (2009) | Mendukung harmonic mean dan pemilihan metrik. |
| Hold-out Validation | Belum menjadi subbab | Tidak ada | James et al. (2023); Kohavi (1995) | Mendukung train-test split dan keterbatasan satu pembagian data. |
| Cross Validation | Belum ada | Tidak ada | Arlot dan Celisse (2010); Kohavi (1995) | Menjelaskan K-fold, stratifikasi, bias, dan variance. |
| LOOCV | Belum ada | Tidak ada | Arlot dan Celisse (2010); Kohavi (1995) | Menjelaskan leave-one-out sebagai bentuk leave-p-out serta keterbatasannya. |
| McNemar Test | Belum ada | Tidak ada | McNemar (1947); Dietterich (1998) | Mendukung data berpasangan dan perbandingan classifier. |
| Penelitian Terdahulu | Ada delapan studi, tetapi tidak seimbang | Kurang | Berhane et al. (2018); Schoonbee et al. (2022); Diwandari et al. (2023); Firmansyah dan Yulianto (2021); Utami dan Arifyanto (2025) | Menambah studi komparatif, invoice, DSS, dan prioritas. |
| Research Gap | Masih berasal dari klaim integrasi sistem | Tidak sesuai | Seluruh matriks penelitian terdahulu | Gap harus diturunkan dari perbedaan metode, target, ground truth, dan validasi. |

## 4. Literature Matrix

| No | Referensi | Tahun | Jenis | Reputasi | Bagian Bab II | Digunakan untuk |
|---:|---|---:|---|---|---|---|
| 1 | [Sunindyo et al., Document Tracking Technology to Support Indonesian Local E-Governments](https://doi.org/10.1007/978-3-642-55032-4_33) | 2014 | Conference paper, Springer | Peer-reviewed Springer proceedings | Invoice Tracking; Penelitian Terdahulu | Konsep document tracking dan audit trail dalam proses administrasi. |
| 2 | [Lin, Lin, dan Hsieh, Digitalization and Decarbonization in Last-Mile Logistics](https://doi.org/10.1080/19427867.2026.2623085) | 2026 | Journal article | Taylor & Francis; Scopus record tersedia; quartile perlu verifikasi | Proof of Delivery; Penelitian Terdahulu | POD digital, konfigurasi paper/digital/AI/blockchain, dan konteks logistik. |
| 3 | [Buchanan dan Shortliffe, Rule-Based Expert Systems: The MYCIN Experiments](https://people.dbmi.columbia.edu/~ehs7001/Buchanan-Shortliffe-1984/MYCIN%20Book.htm) | 1984 | Buku akademik | Addison-Wesley; AAAI Classic Book | Rule-Based; Knowledge Acquisition; Expert System | Arsitektur sistem berbasis aturan, knowledge base, inference, dan lessons learned. |
| 4 | [Liu, Gegov, dan Cocea, Rule-Based Systems: A Granular Computing Perspective](https://doi.org/10.1007/s41066-016-0021-6) | 2016 | Journal article | Springer; peer-reviewed; quartile perlu verifikasi | Rule-Based System | Aturan IF-THEN, expert-based versus data-based rules, dan representasi aturan. |
| 5 | [Studer, Benjamins, dan Fensel, Knowledge Engineering: Principles and Methods](https://doi.org/10.1016/S0169-023X(97)00056-6) | 1998 | Journal article | Elsevier, Data & Knowledge Engineering; Scopus | Knowledge Acquisition; Rule Construction | Knowledge engineering sebagai proses pemodelan, bukan transfer label. |
| 6 | [Meseguer, Towards a Conceptual Framework for Expert System Validation](https://doi.org/10.3233/AIC-1992-5301) | 1992 | Journal article | AI Communications; status quartile perlu verifikasi | Rule Validation; Rule Construction | Pembedaan verification, validation, evaluation, dan testing. |
| 7 | [Ben-David, Rule Effectiveness in Rule-Based Systems](https://doi.org/10.1016/j.eswa.2007.05.003) | 2008 | Journal article | Expert Systems with Applications, Elsevier; Q1 | Rule-Based; Rule Validation | Redundansi aturan, comprehensibility, maintainability, dan kontribusi rule terhadap accuracy. |
| 8 | [Quinlan, Induction of Decision Trees](https://doi.org/10.1007/BF00116251) | 1986 | Journal article | Machine Learning, Springer; Scopus | Decision Tree; Entropy; ID3 | Sumber primer ID3, information gain, dan induksi pohon. |
| 9 | [Quinlan, C4.5: Programs for Machine Learning](https://books.google.com/books?id=HExncpjbYroC) | 1993 | Buku akademik | Morgan Kaufmann | Perbedaan ID3-C4.5-CART | Gain ratio, fitur C4.5, dan dasar untuk menjelaskan mengapa metode aktif bukan C4.5. |
| 10 | [Breiman et al., Classification and Regression Trees](https://search.worldcat.org/title/757024130) | 1984 | Buku akademik | Wadsworth/Brooks-Cole | Decision Tree; CART | Pemisahan biner, classification tree, regression tree, dan pruning CART. |
| 11 | [James et al., An Introduction to Statistical Learning with Applications in Python](https://doi.org/10.1007/978-3-031-38747-0) | 2023 | Buku akademik | Springer Texts in Statistics | Supervised Classification; Decision Tree; metrik; hold-out | Dasar modern supervised learning, model assessment, dan tree-based methods. |
| 12 | [Pedregosa et al., Scikit-learn: Machine Learning in Python](https://www.jmlr.org/papers/v12/pedregosa11a.html) | 2011 | Journal article | Journal of Machine Learning Research; Q1 | Decision Tree; Implementasi | Dasar ilmiah penggunaan library scikit-learn. |
| 13 | [Sokolova dan Lapalme, A Systematic Analysis of Performance Measures for Classification Tasks](https://doi.org/10.1016/j.ipm.2009.03.002) | 2009 | Journal article | Information Processing & Management, Elsevier; Q1 | Confusion Matrix; Accuracy; Precision; Recall; F1 | Definisi dan keterbatasan metrik klasifikasi. |
| 14 | [Arlot dan Celisse, A Survey of Cross-Validation Procedures for Model Selection](https://doi.org/10.1214/09-SS054) | 2010 | Journal article | Statistics Surveys; Q1 | Cross Validation; LOOCV | Pemilihan prosedur CV, risk estimation, dan model selection. |
| 15 | [Kohavi, A Study of Cross-Validation and Bootstrap](https://www.ijcai.org/Proceedings/95-2/Papers/016.pdf) | 1995 | Conference paper | IJCAI; forum AI utama | Hold-out; Cross Validation; LOOCV | Perbandingan estimasi performa, stratifikasi, dan keterbatasan LOOCV. |
| 16 | [Kapoor dan Narayanan, Leakage and the Reproducibility Crisis in Machine-Learning-Based Science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | Journal article | Patterns, Cell Press; Q1 | Supervised Classification; Data Leakage | Risiko leakage dan kebutuhan memisahkan preprocessing/tuning dari data uji. |
| 17 | [McNemar, Note on the Sampling Error of the Difference Between Correlated Proportions](https://doi.org/10.1007/BF02295996) | 1947 | Journal article | Psychometrika, Springer; peer-reviewed | McNemar Test | Sumber asli uji proporsi berkorelasi. |
| 18 | [Dietterich, Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms](https://doi.org/10.1162/089976698300017197) | 1998 | Journal article | Neural Computation, MIT Press; Scopus | McNemar Test; Comparative Evaluation | Penggunaan uji statistik pada perbandingan classifier. |
| 19 | [Rudin, Stop Explaining Black Box Machine Learning Models](https://doi.org/10.1038/s42256-019-0048-x) | 2019 | Journal article | Nature Machine Intelligence; Q1 | Rule Transparency; Explainability; DSS | Dasar pentingnya model yang dapat dipahami dalam keputusan berdampak tinggi. |
| 20 | [Berhane et al., Decision-Tree, Rule-Based, and Random Forest Classification](https://doi.org/10.3390/rs10040580) | 2018 | Journal article | Remote Sensing; Q1 | Comparative Study; Penelitian Terdahulu | Contoh perbandingan DT, rule-based, dan RF pada data serta evaluasi yang sama. |
| 21 | [Shim et al., Past, Present, and Future of Decision Support Technology](https://doi.org/10.1016/S0167-9236(01)00139-7) | 2002 | Journal article | Decision Support Systems, Elsevier; Q1 | Decision Support System | Posisi sistem sebagai pendukung keputusan, bukan pengganti pengambil keputusan. |
| 22 | [Schoonbee, Moore, dan Van Vuuren, A Machine-Learning Approach Towards Solving the Invoice Payment Prediction Problem](https://doi.org/10.7166/33-4-2726) | 2022 | Journal article | South African Journal of Industrial Engineering; Scopus Q3 | Invoice; DSS; Penelitian Terdahulu | Prediksi perilaku pembayaran invoice dan prioritisasi sumber daya penagihan. |
| 23 | [Diwandari et al., The Utility of Decision Tree and AHP in Prioritizing Social Aid Distribution](https://doi.org/10.5614/itbj.ict.res.appl.2023.17.1.6) | 2023 | Journal article | Journal of ICT Research and Applications; Scopus, Q2/Q3 menurut kategori | DSS; Prioritization; Penelitian Terdahulu | Decision Tree untuk eligibility dan AHP untuk prioritas pada domain lain. |
| 24 | [Firmansyah dan Yulianto, Machine Learning dengan Decision Tree untuk Prediksi Pembayaran Invoice](https://doi.org/10.31289/jite.v5i1.5066) | 2021 | Journal article | JITE; SINTA 3 | Invoice; Penelitian Terdahulu | Konteks invoice dan C5.0 untuk prediksi pembayaran. |
| 25 | [Utami dan Arifyanto, Digital Transformation of Electricity Bill Collection](https://doi.org/10.33395/sinkron.v9i1.14340) | 2025 | Journal article | Sinkron; riwayat jurnal menunjukkan SINTA 3; verifikasi status terkini | Invoice/Billing; Penelitian Terdahulu | Random Forest, K-fold, rolling-window validation, dan prioritas distribusi tagihan. |
| 26 | [Scikit-learn, Decision Trees User Guide](https://scikit-learn.org/stable/modules/tree.html) | 2026, versi daring | Dokumentasi resmi | Dokumentasi resmi, bukan artikel ilmiah | Decision Tree; Entropy; ID3-C4.5-CART | Membuktikan perilaku library: optimized CART, binary splits, dan entropy criterion. |

## 5. Reference Quality Matrix

`X` menunjukkan kategori yang digunakan dalam audit. Kolom "Lain" dipakai untuk konferensi bereputasi, Scopus tanpa quartile yang terverifikasi, atau status yang masih memerlukan pemeriksaan.

| No | Referensi Singkat | Q1 | Q2 | Q3 | Q4 | SINTA | Buku | Dokumentasi Resmi | Lain |
|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Sunindyo et al. (2014) |  |  |  |  |  |  |  | Springer proceedings |
| 2 | Lin et al. (2026) |  |  |  |  |  |  |  | Scopus/Taylor & Francis; Q perlu verifikasi |
| 3 | Buchanan dan Shortliffe (1984) |  |  |  |  |  | X |  | AAAI Classic Book |
| 4 | Liu et al. (2016) |  |  |  |  |  |  |  | Springer peer-reviewed; Q perlu verifikasi |
| 5 | Studer et al. (1998) |  |  |  |  |  |  |  | Elsevier/Scopus; Q perlu verifikasi |
| 6 | Meseguer (1992) |  |  |  |  |  |  |  | Indeks/quartile perlu verifikasi |
| 7 | Ben-David (2008) | X |  |  |  |  |  |  | Expert Systems with Applications |
| 8 | Quinlan (1986) | X |  |  |  |  |  |  | Machine Learning |
| 9 | Quinlan (1993) |  |  |  |  |  | X |  | Morgan Kaufmann |
| 10 | Breiman et al. (1984) |  |  |  |  |  | X |  | Wadsworth/Brooks-Cole |
| 11 | James et al. (2023) |  |  |  |  |  | X |  | Springer |
| 12 | Pedregosa et al. (2011) | X |  |  |  |  |  |  | JMLR |
| 13 | Sokolova dan Lapalme (2009) | X |  |  |  |  |  |  | Information Processing & Management |
| 14 | Arlot dan Celisse (2010) | X |  |  |  |  |  |  | Statistics Surveys |
| 15 | Kohavi (1995) |  |  |  |  |  |  |  | IJCAI peer-reviewed conference |
| 16 | Kapoor dan Narayanan (2023) | X |  |  |  |  |  |  | Patterns |
| 17 | McNemar (1947) |  |  |  |  |  |  |  | Psychometrika; current Q perlu verifikasi |
| 18 | Dietterich (1998) |  |  |  |  |  |  |  | Neural Computation/Scopus; Q perlu verifikasi |
| 19 | Rudin (2019) | X |  |  |  |  |  |  | Nature Machine Intelligence |
| 20 | Berhane et al. (2018) | X |  |  |  |  |  |  | Remote Sensing |
| 21 | Shim et al. (2002) | X |  |  |  |  |  |  | Decision Support Systems |
| 22 | Schoonbee et al. (2022) |  |  | X |  |  |  |  | SAJIE, Scopus 2024 |
| 23 | Diwandari et al. (2023) |  | X |  |  |  |  |  | Q2 pada kategori terbaik; Q3 pada kategori lain |
| 24 | Firmansyah dan Yulianto (2021) |  |  |  |  | SINTA 3 |  |  | Tidak dihitung dalam target SINTA 1-2 |
| 25 | Utami dan Arifyanto (2025) |  |  |  |  | SINTA 3* |  |  | Status terkini perlu verifikasi |
| 26 | Scikit-learn User Guide |  |  |  |  |  |  | X | Pendukung implementasi |

### Interpretasi Kualitas

1. Buku klasik tetap digunakan karena merupakan sumber primer algoritma atau expert system.
2. Sumber Q1-Q3 digunakan sebagai literatur ilmiah bereputasi.
3. Springer/IJCAI proceedings dihitung bereputasi meskipun tidak memiliki quartile jurnal.
4. Dokumentasi scikit-learn hanya mendukung klaim implementasi library.
5. Firmansyah dan Utami dipertahankan sebagai konteks domain Indonesia, bukan fondasi teori.
6. Meseguer dipakai karena nilai historis-metodologisnya, tetapi tidak dihitung dalam persentase konservatif sampai status indeks diverifikasi.

## 6. Audit Penelitian Terdahulu

| Kategori yang Dibutuhkan | Bukti yang Tersedia | Status | Tindakan |
|---|---|---|---|
| Rule-Based | Ben-David (2008); Liu et al. (2016) | Cukup untuk teori dan satu kasus empiris | Gunakan Ben-David sebagai studi kasus rule maintenance. |
| Decision Tree | Quinlan (1986); Berhane et al. (2018); Diwandari et al. (2023) | Cukup | Bedakan teori algoritmik dan aplikasi. |
| Comparative Study | Berhane et al. (2018) | Ada, tetapi domain berbeda | Jelaskan bahwa perbandingan dilakukan pada wetland imagery dan rule-based tidak berasal dari SOP invoice. |
| Decision Support System | Shim et al. (2002); Schoonbee et al. (2022); Diwandari et al. (2023) | Cukup | Gunakan untuk posisi sistem sebagai pendukung keputusan. |
| Invoice | Schoonbee et al. (2022); Firmansyah dan Yulianto (2021); Utami dan Arifyanto (2025) | Cukup secara domain dekat | Targetnya pembayaran, bukan prioritas pengiriman. |
| Logistics/Document Tracking | Sunindyo et al. (2014); Lin et al. (2026) | Cukup untuk konteks | Jangan mengklaim keduanya meneliti klasifikasi invoice. |
| Expert System | Buchanan dan Shortliffe (1984); Meseguer (1992) | Cukup | Digunakan sebagai dasar Rule-Based dan validasi. |
| Machine Learning Classification | James et al. (2023); Pedregosa et al. (2011); Kapoor dan Narayanan (2023) | Cukup | Digunakan untuk training, validation, dan leakage prevention. |

Tidak ditemukan dalam korpus terverifikasi ini studi yang sekaligus memenuhi seluruh unsur berikut: Rule-Based dari SOP invoice, Decision Tree dari label historis admin, kasus uji yang sama, error analysis per invoice, dan paired McNemar. Temuan ini hanya berlaku pada korpus yang diaudit, bukan klaim bahwa studi tersebut tidak ada di seluruh literatur.

## 7. Research Gap Matrix

| Penelitian | Metode | Dataset | Kelebihan | Keterbatasan yang Terverifikasi | Gap yang Diisi Penelitian Ini |
|---|---|---|---|---|---|
| Sunindyo et al. (2014) | Document tracking technology | Proses dokumen pemerintah lokal Indonesia | Relevan untuk tracking dan audit trail | Tidak mengevaluasi classifier prioritas invoice | Menambahkan klasifikasi prioritas dan evaluasi metode. |
| Lin et al. (2026) | Perbandingan empat konfigurasi POD | Data transaksi perusahaan 3PL Taiwan | Bukti mutakhir tentang digital POD | Fokus pada life-cycle assessment, bukan klasifikasi prioritas | Menggunakan POD sebagai konteks penerapan keputusan invoice. |
| Ben-David (2008) | Rule-based expert system | Kasus credit scoring institusi keuangan | Membahas redundancy, accuracy, dan maintainability aturan | Studi satu rule base; tidak membandingkan dengan Decision Tree pada label admin | Membandingkan rule base SOP dengan model data-driven pada kasus yang sama. |
| Berhane et al. (2018) | Decision Tree, Rule-Based, Random Forest | High-resolution multispectral wetland imagery | Perbandingan beberapa classifier pada satu tugas | Domain citra; rule set terkait proses tree/ruleset, bukan SOP operasional admin | Membandingkan expert-authored SOP rules dengan Decision Tree pada invoice. |
| Shim et al. (2002) | Kajian teknologi DSS | Literatur dan perkembangan DSS | Menetapkan sistem sebagai pendukung keputusan | Tidak menyediakan eksperimen klasifikasi | Menguji metode klasifikasi sebelum rekomendasi diterapkan pada sistem. |
| Schoonbee et al. (2022) | Beberapa kandidat machine learning dalam DSS | Data invoice industri nyata | Invoice-level prediction dan prioritisasi sumber daya | Target adalah interval keterlambatan pembayaran; tidak ada Rule-Based SOP | Mengubah target ke urgensi pengiriman dan menambahkan pembanding Rule-Based. |
| Firmansyah dan Yulianto (2021) | C5.0 | Data invoice Gramedia | Domain invoice dan prediksi pembayaran | Bukan C4.5; target pembayaran; tidak ada paired comparison | Menggunakan Decision Tree entropy dan Rule-Based pada delivery priority. |
| Utami dan Arifyanto (2025) | Random Forest; K-fold dan rolling window | 227.163 data pelanggan listrik 2018-2023 | Data besar dan lebih dari satu skenario validasi | Target keterlambatan pembayaran; bukan Rule-Based versus Decision Tree | Menggunakan label admin untuk perbandingan dua metode pada target pengiriman. |
| Diwandari et al. (2023) | Decision Tree dan AHP | Data kelayakan bantuan sosial | Menghubungkan klasifikasi dengan prioritas DSS | Domain berbeda; Decision Tree dan AHP memiliki fungsi berbeda; tidak ada Rule-Based SOP | Membandingkan dua classifier terhadap ground truth dan kasus validasi yang sama. |

### Rumusan Gap yang Aman

> Berdasarkan korpus penelitian yang ditinjau, studi invoice cenderung berfokus pada prediksi pembayaran, studi document tracking dan POD berfokus pada pemantauan proses, sedangkan studi komparatif Rule-Based dan Decision Tree ditemukan pada domain lain. Korpus tersebut belum memberikan evaluasi langsung antara Rule-Based yang diturunkan dari SOP dan Decision Tree berbasis data historis admin untuk klasifikasi prioritas pengiriman invoice dengan ground truth, kasus validasi, analisis kesalahan, dan uji berpasangan yang sama.

## 8. Claim Evidence Matrix

| Klaim dalam Skripsi | Bukti Pendukung | Ketentuan Penulisan |
|---|---|---|
| Rule-Based dapat merepresentasikan pengetahuan dalam aturan IF-THEN | Buchanan dan Shortliffe (1984); Liu et al. (2016) | Klaim teoritis. |
| Rule-Based penelitian dibangun dari SOP | Dokumen SOP, tabel traceability, dan prosedur Bab III; Studer et al. (1998) sebagai dasar proses | Literatur tidak membuktikan bahwa R1-R8 benar-benar berasal dari SOP; bukti internal wajib. |
| Knowledge Acquisition mendahului Rule Construction | Studer et al. (1998); Buchanan dan Shortliffe (1984) | Jangan hubungkan proses ini dengan pembentukan ground truth. |
| Rule Validation memeriksa konsistensi, redundansi, dan kelayakan aturan | Meseguer (1992); Ben-David (2008); bukti validasi perusahaan | Bedakan verification dari empirical evaluation. |
| Decision Tree merupakan supervised classifier | Quinlan (1986); James et al. (2023) | Jelaskan fitur, label, dan recursive partitioning. |
| Implementasi menggunakan entropy dan bukan C4.5 | Konfigurasi eksperimen; dokumentasi scikit-learn; Quinlan (1993); Breiman et al. (1984) | Entropy adalah criterion; tidak membuktikan C4.5. |
| Scikit-learn menggunakan optimized CART dengan binary splits | Dokumentasi resmi scikit-learn; Pedregosa et al. (2011) | Dokumentasi resmi menjadi bukti utama perilaku library. |
| Ground truth berasal dari `expert_label` admin | Dataset, data dictionary, dan bukti provenance perusahaan | Tidak boleh dibuktikan hanya dengan artikel ilmiah. |
| Dataset bersih terdiri atas 99 invoice | Dataset audit dan artefak preprocessing Bab III | Gunakan bukti reproduksibilitas internal. |
| Pemisahan fitur dan tuning dari data uji mencegah leakage | Kapoor dan Narayanan (2023); prosedur pipeline Bab III | Klaim hanya berlaku jika implementasi konsisten. |
| Accuracy, precision, recall, dan F1 mengukur aspek yang berbeda | Sokolova dan Lapalme (2009) | Jangan menilai metode dari accuracy saja. |
| Hold-out, 5-fold CV, dan LOOCV memiliki sifat evaluasi berbeda | James et al. (2023); Kohavi (1995); Arlot dan Celisse (2010) | Jangan memilih skenario hanya karena memberi hasil tertinggi. |
| McNemar sesuai untuk prediksi benar/salah yang berpasangan | McNemar (1947); Dietterich (1998) | Gunakan kasus validasi yang sama. |
| Decision Tree menunjukkan performa deskriptif lebih tinggi | Tabel hasil Bab IV | Tidak memerlukan klaim teoritis; laporkan sesuai angka. |
| Perbedaan belum signifikan secara statistik | Hasil exact McNemar Bab IV; McNemar (1947) untuk interpretasi | `p = 0,2891` tidak membuktikan kedua metode identik. |
| Rule-Based lebih mudah ditelusuri dan diaudit | Buchanan dan Shortliffe (1984); Ben-David (2008); Rudin (2019); Rule ID Bab III | Gunakan "lebih mudah ditelusuri" jika traceability benar-benar tersedia. |
| Rule-Based lebih mudah dipelihara | Ben-David (2008) | Klaim harus bersyarat; rule base besar justru dapat sulit dipelihara. |
| Decision Tree lebih adaptif | Belum cukup dibuktikan oleh eksperimen penelitian ini | Tulis sebagai karakteristik prosedural: pembaruan memerlukan data dan retraining. Jangan klaim hasil empiris. |
| Salah satu metode lebih scalable | Belum ada eksperimen skala khusus | Jangan membuat klaim empiris. Laporkan hanya kompleksitas prosedural atau waktu komputasi yang benar-benar diukur. |

## 9. Audit Sitasi Saat Ini

| Kunci Saat Ini | Keputusan | Alasan Akademik | Pengganti/Posisi |
|---|---|---|---|
| `10.1007/978-3-642-55032-4_33` | Pertahankan | Springer proceedings dan relevan untuk document tracking | 2.1 dan penelitian terdahulu. |
| `gemma` | Hapus dari korpus inti | Status indeks dan reputasi belum dapat dipastikan; relevansi hanya pada aplikasi tracking | Gunakan Sunindyo; tambahkan sumber tracking bereputasi jika ditemukan. |
| `marrysheva` | Hapus sampai terverifikasi | DOI mengarah ke Zenodo; peer review, volume, issue, dan penerbit belum terbukti | Jangan digunakan dalam gap sebelum sumber jurnal primer tersedia. |
| `gunadhya_rajawali_logistik_2021` | Pertahankan sebagai pendukung | Relevan langsung pada POD Indonesia, tetapi reputasi indeks belum terverifikasi | Pasangkan dengan Lin et al. (2026), jangan dijadikan sumber teori tunggal. |
| `nazifah_2023` | Hapus dari teori utama | Fokus pada C4.5 dan venue bukan sumber primer algoritma | Ganti dengan Quinlan (1986, 1993), Breiman et al. (1984), dan James et al. (2023). |
| `Rim2020` | Hapus | Membahas optimasi C4.5 yang tidak diterapkan | Ganti dengan sumber algoritmik primer. |
| `Siahaan_Doni_2025` | Hapus dari korpus inti | C4.5 pada keterlambatan paket; status indeks belum terverifikasi dan target berbeda | Berhane et al. (2018) lebih kuat untuk studi komparatif; Schoonbee untuk invoice. |
| `dyahikbal` | Pertahankan sebagai studi konteks | Relevan pada tagihan, prioritisasi, dan validasi; metode sebenarnya Random Forest | Koreksi uraian metode dan jangan jadikan bukti Decision Tree. |
| `firmansyah` | Pertahankan sebagai studi konteks | Relevan langsung pada invoice; metode sebenarnya C5.0 | Koreksi metode dan target pembayaran. |
| `Diwandari...2023` | Pertahankan | Scopus dan relevan pada DSS/prioritization | Koreksi metode menjadi Decision Tree + AHP, bukan C4.5. |

## 10. Referensi yang Harus Ditambah

### Teori Dasar dan Supervised Learning

1. James et al. (2023).
2. Pedregosa et al. (2011).
3. Kapoor dan Narayanan (2023).

### Rule-Based dan Expert System

1. Buchanan dan Shortliffe (1984).
2. Liu et al. (2016).
3. Ben-David (2008).
4. Rudin (2019).

### Knowledge Acquisition dan Rule Validation

1. Studer et al. (1998).
2. Meseguer (1992).

### Decision Tree, Entropy, ID3, C4.5, dan CART

1. Quinlan (1986).
2. Quinlan (1993).
3. Breiman et al. (1984).
4. Scikit-learn Decision Trees User Guide.

### Machine Learning Evaluation dan Statistik

1. Sokolova dan Lapalme (2009).
2. Arlot dan Celisse (2010).
3. Kohavi (1995).
4. McNemar (1947).
5. Dietterich (1998).

### Penelitian Terdahulu, DSS, Invoice, dan POD

1. Lin et al. (2026).
2. Berhane et al. (2018).
3. Shim et al. (2002).
4. Schoonbee et al. (2022).

## 11. Referensi yang Harus Dihapus atau Diturunkan

### Hapus

1. Acedo et al. (`gemma`): reputasi belum terverifikasi dan hanya relevan tidak langsung.
2. Marysheva et al. (`marrysheva`): peer review dan identitas jurnal belum terverifikasi.
3. Nazifah dan Prianto (`nazifah_2023`): bukan sumber primer dan masih menarik naskah ke C4.5.
4. Rim dan Liu (`Rim2020`): optimasi C4.5 tidak digunakan.
5. Siahaan dan Doni (`Siahaan_Doni_2025`): domain dan algoritma tidak cukup dekat, reputasi belum terverifikasi.

### Turunkan menjadi Pendukung

1. Dharaningtyas dan Nizar: hanya untuk konteks POD lokal.
2. Firmansyah dan Yulianto: hanya untuk konteks invoice payment dengan C5.0.
3. Utami dan Arifyanto: hanya untuk konteks billing priority dengan Random Forest.

## 12. Rekomendasi Daftar Pustaka Final per Kelompok

| Kelompok | Referensi Utama |
|---|---|
| Teori dasar | James et al. (2023); Pedregosa et al. (2011) |
| Rule-Based | Buchanan dan Shortliffe (1984); Liu et al. (2016); Ben-David (2008); Rudin (2019) |
| Knowledge Acquisition | Studer et al. (1998); Buchanan dan Shortliffe (1984) |
| Rule Construction/Validation | Meseguer (1992); Ben-David (2008) |
| Decision Tree | Quinlan (1986); Breiman et al. (1984); James et al. (2023) |
| ID3-C4.5-CART | Quinlan (1986, 1993); Breiman et al. (1984); scikit-learn documentation |
| Machine Learning Evaluation | Sokolova dan Lapalme (2009); Kohavi (1995); Arlot dan Celisse (2010); Kapoor dan Narayanan (2023) |
| Statistik | McNemar (1947); Dietterich (1998) |
| Comparative Study | Berhane et al. (2018) |
| Decision Support System | Shim et al. (2002); Schoonbee et al. (2022); Diwandari et al. (2023) |
| Invoice | Schoonbee et al. (2022); Firmansyah dan Yulianto (2021); Utami dan Arifyanto (2025) |
| Invoice Tracking | Sunindyo et al. (2014); Schoonbee et al. (2022) |
| Proof of Delivery | Lin et al. (2026); Dharaningtyas dan Nizar (2021) sebagai pendukung |

## 13. Roadmap Revisi Kajian Pustaka

### Tahap 1: Penguncian Sumber

1. Verifikasi ulang quartile dan indeks pada tanggal finalisasi.
2. Unduh metadata resmi DOI/BibTeX untuk 26 sumber.
3. Periksa nama penulis, judul, tahun, volume, issue, halaman, DOI, dan ISBN.
4. Masukkan hanya entri terverifikasi ke `References.bib`.

### Tahap 2: Revisi Struktur

1. Tambahkan Hold-out Validation sebagai subbab tersendiri.
2. Gunakan struktur 2.1-2.20.
3. Pastikan setiap subbab mendukung Bab III atau Bab IV.

### Tahap 3: Penulisan Teori

1. Tulis Invoice Tracking dan POD secara ringkas.
2. Tulis Rule-Based, Knowledge Acquisition, dan Rule Construction secara terpisah.
3. Tulis Decision Tree dan entropy tanpa menyebut metode aktif sebagai C4.5.
4. Tulis tabel perbedaan ID3, C4.5, CART, dan implementasi penelitian.
5. Tulis supervised learning, leakage, metrik, hold-out, CV, LOOCV, dan McNemar.

### Tahap 4: Penelitian Terdahulu

1. Gunakan studi yang benar-benar mewakili Rule-Based, Decision Tree, comparative study, DSS, invoice, tracking, dan POD.
2. Nyatakan metode dan target setiap studi secara akurat.
3. Bedakan relevansi langsung dan tidak langsung.
4. Jangan mengisi keterbatasan studi dengan dugaan.

### Tahap 5: Research Gap

1. Sintesis pola studi terdahulu.
2. Tunjukkan perbedaan domain, target, ground truth, dan evaluasi.
3. Nyatakan gap hanya pada korpus yang ditinjau.
4. Hubungkan gap langsung dengan desain Bab III.

### Tahap 6: Audit Akhir

1. Periksa setiap klaim dengan Claim Evidence Matrix.
2. Hapus sitasi yang tidak mendukung kalimat terkait.
3. Pastikan Bab II tidak memuat hasil Bab IV.
4. Kompilasi dan periksa seluruh citation key setelah revisi LaTeX dimulai.

## 14. Checklist Kesiapan Sebelum Menulis `Kajian-Pustaka.tex`

### Bibliografi

- [ ] Minimal 15 referensi tersedia; rekomendasi saat ini 26.
- [ ] Minimal 80% bereputasi; hasil audit konservatif 84,62%.
- [ ] Semua DOI, ISBN, volume, issue, dan halaman telah diverifikasi.
- [ ] Status Scopus/SINTA diperiksa kembali pada tanggal finalisasi.
- [ ] Tidak ada blog, Medium, Scribd, Wikipedia, atau repository non-peer-reviewed sebagai sumber teori.
- [ ] Dokumentasi resmi hanya digunakan untuk perilaku library.

### Teori

- [ ] Rule-Based memiliki sumber expert system dan sumber maintainability.
- [ ] Knowledge Acquisition tidak digunakan untuk membentuk ground truth.
- [ ] Rule Construction memiliki dasar verification dan validation.
- [ ] Decision Tree dibedakan dari C4.5.
- [ ] Entropy dijelaskan sebagai impurity criterion.
- [ ] Data leakage memiliki sumber ilmiah.
- [ ] Hold-out, cross-validation, LOOCV, dan McNemar memiliki sumber metodologis.
- [ ] Semua metrik menggunakan `Urgent` sebagai kelas positif.

### Penelitian Terdahulu dan Gap

- [ ] Ada studi Rule-Based empiris.
- [ ] Ada studi Decision Tree.
- [ ] Ada comparative study.
- [ ] Ada studi DSS.
- [ ] Ada studi invoice, tracking, dan POD.
- [ ] Metode Firmansyah ditulis C5.0.
- [ ] Metode Utami ditulis Random Forest.
- [ ] Metode Diwandari ditulis Decision Tree dan AHP.
- [ ] Research gap berasal dari Research Gap Matrix.
- [ ] Tidak ada klaim "belum pernah diteliti".

### Konsistensi Penelitian

- [ ] Ground truth dinyatakan sebagai label historis admin.
- [ ] Bukti provenance `expert_label` tersedia atau keterbatasannya dinyatakan.
- [ ] Rule-Based dan Decision Tree ditempatkan sebagai metode yang dibandingkan.
- [ ] Sistem ditempatkan sebagai konteks penerapan.
- [ ] Tidak ada nilai accuracy atau p-value penelitian ini di Bab II.
- [ ] Tidak ada klaim Decision Tree lebih unggul.
