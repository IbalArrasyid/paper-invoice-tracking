# Audit Akademik Bab I dan Bab II

**Ruang lingkup:** `Pendahuluan.tex` dan `Kajian-Pustaka.tex`.

**Batas pekerjaan:** Audit konseptual dan blueprint. Tidak ada file LaTeX, gambar, tabel eksperimen, atau hasil eksperimen yang diubah.

## 1. Audit Bab I

### 1.1 Temuan Umum

Bab I lama masih menempatkan integrasi sistem, POD, formalisasi pengetahuan, Operational Labeling Guideline, dan Decision Tree C4.5 sebagai satu kontribusi. Posisi tersebut tidak lagi konsisten dengan metodologi final. Bab I baru harus berpusat pada perbandingan Rule-Based dan Decision Tree dengan label historis admin sebagai ground truth bersama.

### 1.2 Keputusan per Bagian

| Bagian Lama | Keputusan | Alasan Ilmiah |
|---|---|---|
| Konteks administrasi B2B, invoice, dan POD | Pertahankan dan persingkat | Diperlukan untuk menjelaskan domain, tetapi bukan fokus kontribusi. |
| Masalah pelacakan status invoice | Pertahankan secara terbatas | Menjelaskan konteks sistem. Pembahasan arsitektur dan fitur sistem tidak diperlukan di latar belakang. |
| Kondisi perusahaan dan aturan pelanggan | Pertahankan jika didukung data lapangan | Menjelaskan sumber masalah prioritas. Hindari generalisasi tentang inefisiensi atau ketidakkonsistenan tanpa bukti. |
| Teori tacit knowledge dan Knowledge Formalization | Pindahkan ke Bab II dan persingkat | Teori tidak boleh mendominasi Bab I. Knowledge Acquisition hanya mendukung pembentukan Rule-Based. |
| Penjelasan panjang Decision Tree C4.5 | Hapus dari Bab I | Salah terhadap implementasi final dan merupakan materi Bab II. |
| Operational Labeling Guideline sebagai sumber label | Hapus | Ground truth final berasal dari label historis admin, bukan aturan yang dibangun peneliti. |
| Integrasi tracking, POD, formalisasi, dan model sebagai research gap | Ganti | Research gap harus berpusat pada kekurangan bukti komparatif langsung. |
| Sistem web sebagai kontribusi utama | Turunkan menjadi konteks penerapan | Paradigma final adalah comparative analysis, bukan system development. |
| Dua rumusan masalah lama | Ganti | Pertanyaan lama masih mencampur pembangunan sistem, C4.5, dan guideline-based labeling. |
| Dua tujuan lama | Ganti | Tujuan harus sejajar dengan konstruksi metode, evaluasi komparatif, dan analisis karakteristik. |
| Batasan Operational Labeling Guideline dan C4.5 | Ganti | Tidak sesuai dengan ground truth dan implementasi aktual. |
| Rincian hasil, akurasi, dan p-value | Jangan ditambahkan | Bab I merumuskan masalah. Bukti hasil hanya dibahas di Bab IV. |

### 1.3 Bagian yang Terlalu Panjang atau Berulang

1. Paragraf awal menggabungkan transformasi digital, administrasi B2B, arus kas, tracking, prioritas, dan aturan pelanggan. Pecah fungsinya dan sisakan satu ide operasional.
2. Masalah pencarian dokumen, status real-time, POD, audit, dan pengambilan keputusan berulang pada beberapa paragraf. Ringkas menjadi konteks operasional dan masalah prioritas.
3. Penelitian terdahulu dibahas terlalu rinci di Bab I. Bab I cukup menyintesis gap; tabel dan uraian studi ditempatkan di Bab II.
4. Tacit knowledge, Knowledge Formalization, dan karakteristik C4.5 merupakan teori. Pindahkan ke Bab II atau hapus jika tidak mendukung metode final.
5. Latar belakang lama menutup dengan pertanyaan penelitian di dalam paragraf, lalu mengulangnya pada Rumusan Masalah. Pertanyaan hanya ditulis pada subbab Rumusan Masalah.

### 1.4 Struktur Final Bab I

Blueprint lengkap terdapat pada `Chapter-I-Blueprint.md`. Latar belakang ditetapkan tepat enam paragraf:

1. Konteks operasional invoice dan POD.
2. Masalah klasifikasi prioritas invoice.
3. Rule-Based dari SOP.
4. Decision Tree berbasis entropy dari data historis admin.
5. Research gap komparatif.
6. Posisi penelitian dan desain evaluasi umum.

Rumusan masalah, tujuan, dan kontribusi masing-masing memiliki tiga fokus sejajar: konstruksi metode, evaluasi komparatif, dan karakteristik operasional.

## 2. Audit Bab II

### 2.1 Temuan Umum

Bab II lama belum mendukung metodologi final. Urutan teori masih mengikuti paradigma sistem-formalisasi-C4.5. Teori cross-validation, LOOCV, McNemar, dan research gap belum tersedia sebagai bagian khusus. Penelitian terdahulu juga didominasi studi Decision Tree dan konteks sistem, sementara bukti Rule-Based dan studi komparatif langsung belum tersedia.

### 2.2 Audit Teori yang Ada

| Bagian Saat Ini | Status | Tindakan | Alasan Ilmiah |
|---|---|---|---|
| Manajemen Invoice dalam B2B | Relevan sebagian | Ganti menjadi Invoice Tracking dan persingkat | Fokus penelitian adalah prioritas pengiriman dan pelacakan, bukan teori piutang secara luas. |
| Sistem Pelacakan Dokumen Berbasis Web | Relevan | Gabungkan ke 2.1 Invoice Tracking | Sistem hanya konteks penerapan. |
| Proof of Delivery | Relevan | Pertahankan sebagai 2.2 | Menjelaskan bukti penerimaan dan hubungan dengan status pengiriman. |
| Akuisisi dan Formalisasi Pengetahuan | Perlu revisi besar | Pisahkan menjadi 2.4 Knowledge Acquisition dan 2.5 Rule Construction | Ground truth tidak boleh dinyatakan sebagai hasil formalisasi aturan. |
| Rule-Based System | Relevan | Pertahankan sebagai 2.3 dan ringkas | Diperlukan untuk menjelaskan aturan IF-THEN, inference, traceability, dan keterbatasan rule coverage. |
| Klasifikasi Data-Driven | Relevan | Ganti menjadi 2.9 Supervised Classification | Harus menjelaskan fitur, label, data latih, dan data validasi tanpa mengulang Decision Tree. |
| Mekanisme C4.5 | Tidak sesuai sebagai teori metode aktif | Ganti menjadi 2.6 Decision Tree, 2.7 Entropy, dan 2.8 Perbedaan ID3-C4.5-CART | Implementasi tidak menggunakan gain ratio atau prosedur C4.5. |
| Split Information dan Gain Ratio | Tidak relevan untuk implementasi | Hapus dari uraian metode aktif; sebut singkat pada perbandingan algoritma | Mencegah pembaca menyimpulkan bahwa penelitian menerapkan C4.5. |
| Metrik Evaluasi Performa | Relevan tetapi terlalu padat | Pecah menjadi 2.10-2.14 | Setiap metrik membutuhkan definisi, formula, interpretasi, dan batas penggunaan. |
| Cross-validation | Belum ada | Tambahkan 2.15 | Mendukung E3 dan prinsip out-of-fold evaluation. |
| LOOCV | Belum ada | Tambahkan 2.16 | Mendukung E4 dan konsekuensi penggunaan dataset kecil. |
| McNemar | Belum ada | Tambahkan 2.17 | Mendukung uji dua model pada kasus yang sama. |
| Penelitian Terdahulu | Relevan tetapi belum seimbang | Bangun ulang sebagai 2.18 | Perlu pemetaan domain, metode, target, label, validasi, dan relevansi. |
| Research Gap | Belum menjadi subbab mandiri | Tambahkan 2.19 | Gap harus diturunkan dari hasil sintesis studi, bukan klaim umum. |

### 2.3 Koreksi Khusus Decision Tree

Implementasi penelitian menggunakan `DecisionTreeClassifier` dengan `criterion="entropy"`. Implementasi scikit-learn membangun pohon biner dengan pendekatan CART yang dioptimalkan; penggunaan entropy menentukan fungsi impurity, tetapi tidak mengubahnya menjadi C4.5. C4.5 secara khas menggunakan gain ratio dan memiliki prosedur algoritmik tersendiri. Karena implementasi penelitian tidak menghitung gain ratio, istilah yang tepat adalah **Decision Tree berbasis entropy**, bukan **Decision Tree C4.5**.

Urutan teori yang wajib:

1. ID3: pohon klasifikasi dan information gain.
2. C4.5: pengembangan ID3, termasuk gain ratio dan penanganan fitur yang lebih luas.
3. CART: pemisahan biner untuk klasifikasi atau regresi.
4. Implementasi penelitian: Decision Tree scikit-learn dengan pemisahan biner dan kriteria entropy; bukan implementasi C4.5.

Dasar implementasi ini sesuai dengan [dokumentasi Decision Tree scikit-learn](https://scikit-learn.org/stable/modules/tree.html), yang menyatakan bahwa library tersebut menggunakan versi CART yang dioptimalkan dan menyediakan entropy sebagai salah satu kriteria impurity.

### 2.4 Audit Penelitian Terdahulu

| Studi dalam Naskah | Relevansi Nyata | Keputusan | Koreksi yang Diperlukan |
|---|---|---|---|
| Sunindyo dkk. (2014) | Document tracking pada pemerintahan lokal | Pertahankan sebagai konteks tracking | Bukan studi klasifikasi prioritas invoice. |
| Acedo dkk. (2025) | Sistem tracking dokumen berbasis web dan QR | Pertahankan sebagai konteks tracking | Bukan pembanding Rule-Based dan Decision Tree. |
| Marysheva dkk. (2024) | Document flow dengan decision tree | Pertahankan secara bersyarat | Verifikasi mutu sumber, metode, dataset, dan hasil sebelum dipakai. |
| Dharaningtyas dan Nizar (2021) | Perbaikan proses POD dengan DMAIC/Lean Six Sigma | Pertahankan untuk teori POD | Bukan klasifikasi, invoice priority, atau studi komparatif. |
| Siahaan dan Doni (2025) | C4.5 untuk faktor keterlambatan paket | Pertahankan sebagai konteks logistik Decision Tree | Unit analisis dan target berbeda dari invoice delivery priority. |
| Firmansyah dan Yulianto (2021) | Prediksi keterlambatan pembayaran invoice | Pertahankan untuk konteks invoice | Koreksi metode menjadi C5.0 dan target menjadi ketepatan pembayaran, bukan pengiriman invoice. |
| Utami dan Arifyanto (2025) | Random Forest untuk prediksi keterlambatan pembayaran dan prioritas distribusi tagihan | Pertahankan secara terbatas | Koreksi metode menjadi Random Forest; relevan pada prioritas distribusi, bukan Rule-Based atau Decision Tree. |
| Diwandari dkk. (2023) | Decision Tree untuk kelayakan dan AHP untuk prioritas bantuan sosial | Pertahankan sebagai konteks DSS | Jangan menyebutnya C4.5 tanpa bukti; domain dan target berbeda. |

**Kekurangan kumpulan referensi saat ini:**

1. Belum ada studi empiris Rule-Based yang benar-benar menjadi landasan konstruksi dan evaluasi aturan.
2. Belum ada studi komparatif langsung Rule-Based versus Decision Tree pada target dan ground truth yang sama.
3. Studi invoice yang tersedia berfokus pada pembayaran, bukan urgensi pengiriman dokumen.
4. Studi DSS yang tersedia bersifat tidak langsung dan menggunakan domain bantuan sosial.
5. Belum ada sumber metodologis utama untuk paired comparison dan exact McNemar.

**Catatan verifikasi sumber primer/penerbit:**

- [Firmansyah dan Yulianto (2021)](https://ojs.uma.ac.id/index.php/jite/article/view/5066) menggunakan C5.0 untuk prediksi ketepatan pembayaran invoice.
- [Utami dan Arifyanto (2025)](https://www.jurnal.polgan.ac.id/index.php/sinkron/article/view/14340) menggunakan Random Forest untuk prediksi keterlambatan pembayaran dan prioritas distribusi tagihan.
- [Siahaan dan Doni (2025)](https://www.ejournal.marqchainstitute.or.id/index.php/JICT/article/view/273) menggunakan C4.5 pada keterlambatan pengiriman paket.
- [Dharaningtyas dan Nizar (2021)](https://www.ssbfnet.com/ojs/index.php/ijrbs/article/download/1091/834/3672) membahas perbaikan proses POD melalui pendekatan DMAIC/Lean Six Sigma.
- [Diwandari dkk. (2023)](https://journals.itb.ac.id/index.php/jictra/article/view/18893/6172) menggunakan Decision Tree untuk klasifikasi kelayakan dan AHP untuk prioritas bantuan sosial.

Tambahan referensi harus dipilih melalui penelusuran terarah. Jangan memasukkan studi hanya karena menggunakan istilah invoice atau Decision Tree. Prioritaskan kesesuaian target, metode, ground truth, dan desain evaluasi.

### 2.5 Struktur Final Bab II

Blueprint lengkap terdapat pada `Chapter-II-Blueprint.md`. Struktur final:

1. 2.1 Invoice Tracking
2. 2.2 Proof of Delivery
3. 2.3 Rule-Based System
4. 2.4 Knowledge Acquisition
5. 2.5 Rule Construction
6. 2.6 Decision Tree
7. 2.7 Entropy
8. 2.8 Perbedaan ID3, C4.5, dan CART
9. 2.9 Supervised Classification
10. 2.10 Confusion Matrix
11. 2.11 Accuracy
12. 2.12 Precision
13. 2.13 Recall
14. 2.14 F1-score
15. 2.15 Cross Validation
16. 2.16 Leave-One-Out Cross Validation
17. 2.17 McNemar Test
18. 2.18 Penelitian Terdahulu
19. 2.19 Research Gap

## 3. Daftar Inkonsistensi

| Inkonsistensi | Lokasi Saat Ini | Bentuk Final |
|---|---|---|
| Metode disebut C4.5 | Judul, Bab I, Bab II | Decision Tree berbasis entropy |
| Label aturan menjadi ground truth | Bab I dan Bab II | Label historis admin sebagai ground truth |
| Knowledge Formalization membentuk label | Bab II | Knowledge Acquisition dan Rule Construction hanya membentuk Rule-Based |
| Target tiga kelas | Terminologi naskah lama | Target biner `Urgent` dan `Not Urgent` |
| Sistem sebagai kontribusi utama | Latar belakang dan gap lama | Sistem sebagai konteks deployment |
| Integrasi sistem sebagai research gap | Bab I dan Bab II | Kekurangan bukti komparatif langsung |
| Rule-Based dan Decision Tree dianggap representasi komplementer | Dokumen paradigma lama | Dua metode klasifikasi yang dibandingkan terhadap ground truth yang sama |
| Gain ratio diterangkan sebagai mekanisme penelitian | Bab II | Gain ratio hanya menjelaskan C4.5 dalam tabel perbedaan |
| Penelitian Firmansyah disebut Decision Tree umum | Tabel penelitian terdahulu | C5.0 untuk prediksi pembayaran invoice |
| Penelitian Utami disebut machine learning umum | Tabel penelitian terdahulu | Random Forest dengan K-fold dan rolling-window validation |
| Penelitian Diwandari disebut C4.5 | Tabel penelitian terdahulu | Decision Tree dan AHP, kecuali sumber primer membuktikan varian tertentu |
| Tidak ada teori E3, E4, dan uji berpasangan | Bab II | Tambahkan Cross Validation, LOOCV, dan McNemar |
| Gambar dibuat dengan TikZ | Bab II | Saat implementasi, ganti dengan placeholder sesuai Figure-Prompts policy |

## 4. Daftar Istilah yang Harus Diganti

| Istilah Lama | Istilah Final | Ketentuan |
|---|---|---|
| Decision Tree C4.5 | Decision Tree berbasis entropy | C4.5 hanya muncul dalam teori perbedaan algoritma atau studi yang memang menggunakannya. |
| Guideline-Based Ground Truth | Ground truth admin / label historis admin | Ganti seluruh penggunaan pada penelitian aktif. |
| Operational Labeling Guideline | SOP perusahaan / spesifikasi Rule Construction | Hapus sebagai mekanisme pelabelan. |
| HIGH, MEDIUM, NORMAL | Urgent, Not Urgent | HIGH dan NORMAL hanya boleh disebut ketika menjelaskan normalisasi data sumber di Bab III/IV. |
| Knowledge Representation Consistency | Evaluasi komparatif / konsistensi prediksi, sesuai konteks | Hapus sebagai tujuan utama. |
| Operational Knowledge Formalization Framework | Knowledge Acquisition, Rule Construction, dan Rule Validation | Pertahankan hanya sebagai proses pendukung Rule-Based. |
| Decision Tree Reconstruction | Decision Tree training dan prediction | Ganti seluruh penggunaan. |
| Representasi komplementer | Metode klasifikasi yang dibandingkan | Paradigma penelitian sekarang bersifat komparatif. |
| Label ahli berbasis guideline | Label historis admin | Hindari pencampuran sumber label. |
| Metode paling unggul | Menunjukkan performa lebih tinggi / belum berbeda signifikan | Klaim hasil harus mengikuti uji statistik. |

## 5. Roadmap Revisi

### Tahap 1: Penguncian Terminologi

1. Setujui judul tanpa C4.5.
2. Tetapkan istilah `ground truth admin`, `Urgent`, `Not Urgent`, dan `Decision Tree berbasis entropy`.
3. Tetapkan Knowledge Acquisition sebagai proses pendukung Rule-Based.

### Tahap 2: Revisi Bab I

1. Tulis enam paragraf latar belakang sesuai blueprint.
2. Ganti research gap lama.
3. Tulis tiga rumusan masalah, tiga tujuan, dan tiga kontribusi yang sejajar.
4. Perbarui batasan dataset, fitur, metode, evaluasi, dan generalisasi.
5. Hapus hasil eksperimen dan teori rinci dari Bab I.

### Tahap 3: Rekonstruksi Bab II

1. Susun ulang 2.1-2.19.
2. Pisahkan Rule-Based, Knowledge Acquisition, dan Rule Construction.
3. Ganti teori C4.5 dengan Decision Tree, Entropy, dan perbandingan ID3-C4.5-CART.
4. Tambahkan Cross Validation, LOOCV, dan McNemar.
5. Audit semua rumus, definisi, dan sitasi.

### Tahap 4: Penelitian Terdahulu dan Gap

1. Koreksi metode dan target pada studi yang sudah ada.
2. Tambahkan sumber Rule-Based, komparatif, invoice, dan DSS yang memenuhi kriteria relevansi.
3. Susun tabel sintesis berdasarkan domain, metode, target, ground truth, validasi, hasil, keterbatasan, dan relevansi.
4. Turunkan research gap langsung dari tabel tersebut.

### Tahap 5: Integrasi LaTeX

1. Revisi `Pendahuluan.tex` setelah blueprint disetujui.
2. Revisi `Kajian-Pustaka.tex` setelah literatur tambahan diverifikasi.
3. Ganti seluruh gambar TikZ dengan placeholder dan ID Figure Prompt saat implementasi.
4. Kompilasi dan periksa sitasi, penomoran, tabel, serta konsistensi istilah.

### Tahap 6: Audit Lintas Bab

1. Cocokkan Bab I dan Bab II dengan `Metodologi.tex`.
2. Pastikan Bab IV tidak memperkenalkan metode atau metrik yang belum dijelaskan.
3. Revisi abstrak, judul, dan Bab V setelah Bab IV final.

## 6. Checklist Sebelum Revisi LaTeX

### Keputusan Ilmiah

- [ ] Judul baru telah disetujui pembimbing.
- [ ] Ground truth ditetapkan sebagai label historis admin.
- [ ] Bukti provenance `expert_label` tersedia atau keterbatasannya dinyatakan.
- [ ] Decision Tree disebut berbasis entropy, bukan C4.5.
- [ ] Kontribusi utama ditetapkan sebagai analisis komparatif.

### Bab I

- [ ] Enam fungsi paragraf latar belakang telah disetujui.
- [ ] Rumusan masalah, tujuan, dan kontribusi berjumlah sama dan sejajar.
- [ ] Batasan konsisten dengan 99 invoice dan kelas biner.
- [ ] Sistem hanya menjadi konteks penerapan.
- [ ] Tidak ada angka hasil, p-value, atau klaim superioritas.

### Bab II

- [ ] Struktur 2.1-2.19 telah disetujui.
- [ ] Perbedaan ID3, C4.5, CART, dan implementasi penelitian dinyatakan eksplisit.
- [ ] Gain ratio tidak dijelaskan sebagai mekanisme implementasi.
- [ ] Cross Validation, LOOCV, dan McNemar memiliki sumber metodologis.
- [ ] Formula metrik konsisten dengan `Urgent` sebagai kelas positif.
- [ ] Setiap studi terdahulu telah diperiksa metode, target, dataset, dan validasinya.
- [ ] Literatur Rule-Based dan komparatif telah ditambahkan atau kekurangannya dinyatakan transparan.
- [ ] Research gap berasal langsung dari sintesis penelitian terdahulu.

### Integrasi

- [ ] Tidak ada C4.5 pada judul dan metode aktif.
- [ ] Tidak ada Guideline-Based Ground Truth.
- [ ] Tidak ada kelas MEDIUM pada penelitian aktif.
- [ ] Tidak ada Operational Knowledge Formalization Framework sebagai kontribusi utama.
- [ ] Semua TikZ telah ditandai untuk diganti placeholder saat revisi LaTeX.
- [ ] Tidak ada tabel placeholder; setiap tabel nantinya ditulis lengkap dalam LaTeX.
- [ ] Semua sitasi ada di `References.bib` dan benar-benar mendukung klaim terkait.
