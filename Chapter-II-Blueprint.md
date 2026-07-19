# Blueprint Final Bab II: Kajian Pustaka

**Status:** Final setelah audit konseptual. Dokumen ini menjadi panduan penulisan, bukan naskah LaTeX.

## 1. Tujuan Ilmiah Bab II

Bab II harus menyediakan dasar teori untuk seluruh keputusan metodologis pada Bab III dan seluruh interpretasi pada Bab IV. Teori disusun dari konteks domain, dua metode klasifikasi, evaluasi prediktif, desain validasi, uji statistik berpasangan, penelitian terdahulu, lalu research gap.

Bab II tidak boleh menyampaikan hasil eksperimen penelitian ini. Setiap kelebihan atau keterbatasan metode harus didukung literatur, bukan opini penulis.

## 2. Prinsip Penulisan

1. Setiap subbab menjawab satu kebutuhan teori.
2. Definisi umum dibatasi pada konsep yang dipakai di Bab III atau Bab IV.
3. Implementasi disebut **Decision Tree berbasis entropy**, bukan C4.5.
4. Knowledge Acquisition dan Rule Construction hanya membentuk Rule-Based, bukan ground truth.
5. Formula harus langsung diikuti definisi simbol dan interpretasi dalam konteks kelas `Urgent`.
6. Penelitian terdahulu disintesis, bukan diringkas satu per satu tanpa hubungan.
7. Research gap diturunkan dari bukti pada tabel penelitian terdahulu.

## 3. Struktur dan Isi per Subbab

### 2.1 Invoice Tracking

**Tujuan:** Menjelaskan invoice sebagai objek administrasi yang memiliki identitas, status, waktu, dan riwayat pergerakan.

**Isi wajib:**

- Definisi invoice tracking.
- Elemen status dan audit trail.
- Hubungan tracking dengan pemantauan pengiriman dokumen.
- Posisi rekomendasi prioritas sebagai informasi pendukung, bukan keputusan otomatis final.

**Tindakan terhadap naskah lama:** Gabungkan materi Manajemen Invoice B2B dan Sistem Pelacakan Dokumen. Persingkat teori arus kas dan web architecture.

**Batas:** Jangan membahas detail fitur aplikasi, database, atau antarmuka.

### 2.2 Proof of Delivery

**Tujuan:** Menjelaskan POD sebagai bukti penerimaan dan bagian dari riwayat pengiriman invoice.

**Isi wajib:**

- Definisi dan fungsi POD.
- Hubungan POD dengan verifikasi penerimaan.
- Posisi POD dalam sistem tracking.
- Keterbatasan POD sebagai konteks; POD bukan fitur target klasifikasi kecuali Bab III menyatakannya demikian.

**Tindakan:** Pertahankan dan ringkas materi lama. Hindari klaim bahwa integrasi POD merupakan research gap utama.

### 2.3 Rule-Based System

**Tujuan:** Menjelaskan metode klasifikasi berbasis aturan yang menjadi pembanding pertama.

**Isi wajib:**

- Aturan IF-THEN, fakta, rule base, dan inference process.
- Urutan prioritas aturan dan default rule.
- Rule traceability, rule coverage, dan rule conflict.
- Kelebihan yang didukung literatur: transparansi dan keterlacakan keputusan.
- Keterbatasan yang didukung literatur: ketergantungan pada kelengkapan, validasi, dan pemeliharaan aturan.

**Tindakan:** Pertahankan teori inti. Hapus klaim bahwa Rule-Based membentuk ground truth.

**Hubungan dengan Bab III:** Menjadi dasar aturan R1-R8 dan prosedur Rule Validation.

### 2.4 Knowledge Acquisition

**Tujuan:** Menjelaskan proses memperoleh pengetahuan operasional untuk membangun Rule-Based.

**Isi wajib:**

- Sumber pengetahuan: SOP, dokumen operasional, dan keterangan pihak perusahaan sesuai bukti yang tersedia.
- Proses ekstraksi kondisi, tindakan, dan pengecualian.
- Verifikasi makna aturan dengan pihak yang berwenang.
- Risiko bias, ketidaklengkapan, dan perubahan pengetahuan.

**Tindakan:** Pisahkan dari formalisasi ground truth. Jangan menyatakan tacit knowledge digunakan jika tidak ada wawancara atau bukti akuisisi yang terdokumentasi.

### 2.5 Rule Construction

**Tujuan:** Menjelaskan perubahan pengetahuan hasil akuisisi menjadi aturan klasifikasi yang dapat dijalankan.

**Isi wajib:**

- Penetapan kondisi, operator, konsekuensi, Rule ID, dan urutan aturan.
- Penanganan kondisi yang tumpang tindih.
- Default rule untuk kasus yang tidak memenuhi aturan khusus.
- Validasi sintaks, validasi logika, traceability ke SOP, coverage, dan conflict checking.
- Pembekuan rule base sebelum evaluasi untuk menghindari penyesuaian terhadap hasil uji.

**Tindakan:** Tambahkan sebagai subbab baru. Istilah Operational Knowledge Formalization Framework tidak digunakan sebagai kontribusi.

**Hubungan dengan Bab III:** Menjadi dasar prosedur Rule Construction dan Rule Validation, bukan proses pelabelan data.

### 2.6 Decision Tree

**Tujuan:** Menjelaskan metode supervised classification yang menjadi pembanding kedua.

**Isi wajib:**

- Node akar, node internal, cabang, daun, dan recursive partitioning.
- Pemilihan split berdasarkan penurunan impurity.
- Prediksi kelas pada daun.
- Interpretability, risiko overfitting, ketidakstabilan terhadap perubahan data, dan kebutuhan pengendalian kompleksitas.
- Parameter yang relevan: `max_depth` dan `min_samples_leaf`.

**Pernyataan wajib:**

> Penelitian ini menggunakan Decision Tree berbasis entropy melalui `DecisionTreeClassifier`. Penggunaan entropy menunjukkan kriteria impurity pada pemilihan split dan tidak menjadikan implementasi tersebut sebagai algoritma C4.5.

**Batas:** Jangan membahas hasil kedalaman pohon, parameter terpilih, atau feature importance penelitian ini.

### 2.7 Entropy

**Tujuan:** Menjelaskan ukuran impurity yang digunakan oleh Decision Tree penelitian.

**Isi wajib:**

- Definisi entropy sebagai ketidakmurnian distribusi kelas pada node.
- Formula entropy untuk klasifikasi biner atau multikelas.
- Makna entropy nol dan entropy tinggi.
- Penurunan entropy sebagai dasar pemilihan split.

**Formula yang diperlukan:**

`H(S) = - sum p_i log_2(p_i)`

**Tindakan:** Pertahankan entropy dan information gain secukupnya. Hapus Split Information dan Gain Ratio dari uraian implementasi aktif.

### 2.8 Perbedaan ID3, C4.5, dan CART

**Tujuan:** Mencegah kesalahan penamaan algoritma.

**Tabel wajib:**

| Aspek | ID3 | C4.5 | CART | Implementasi Penelitian |
|---|---|---|---|---|
| Tugas utama | Klasifikasi | Klasifikasi | Klasifikasi dan regresi | Klasifikasi biner |
| Bentuk split | Umumnya multiway untuk atribut kategorikal | Multiway untuk kategorikal dan ambang biner untuk numerik | Biner | Biner |
| Kriteria yang dikenal | Information gain | Gain ratio | Gini atau kriteria impurity lain | Entropy |
| Pruning | Terbatas pada bentuk awal | Memiliki prosedur pruning C4.5 | Cost-complexity pada implementasi tertentu | Kompleksitas dikendalikan melalui parameter yang diuji |
| Status dalam penelitian | Teori pembanding | Bukan metode aktif | Keluarga implementasi scikit-learn | Decision Tree berbasis entropy |

**Penjelasan wajib:** Scikit-learn menggunakan implementasi CART yang dioptimalkan dan mendukung entropy sebagai kriteria klasifikasi. Penelitian tidak menghitung gain ratio dan tidak menerapkan prosedur C4.5. Oleh karena itu, istilah C4.5 tidak boleh dipakai untuk metode penelitian.

**Tindakan:** Ganti seluruh subbab Mekanisme Algoritma C4.5 lama dengan perbandingan ringkas dan akurat.

### 2.9 Supervised Classification

**Tujuan:** Menjelaskan hubungan fitur, label, data latih, model, dan data validasi.

**Isi wajib:**

- Pasangan fitur dan label dalam supervised learning.
- Pemisahan data latih dan validasi.
- Generalisasi pada data yang tidak digunakan untuk pelatihan.
- Risiko data leakage.
- Label admin sebagai target, bukan keluaran Rule-Based.

**Tindakan:** Gunakan kembali materi klasifikasi data-driven yang relevan. Hilangkan contoh fitur yang tidak dipakai pada Bab III.

### 2.10 Confusion Matrix

**Tujuan:** Menetapkan dasar perhitungan semua metrik dan analisis kesalahan.

**Isi wajib:**

- `Urgent` sebagai kelas positif.
- Definisi TP, TN, FP, dan FN.
- Makna operasional FP dan FN pada prioritas invoice.

**Tabel wajib:** Matriks 2 x 2 dengan aktual pada baris dan prediksi pada kolom. Tidak diperlukan gambar dekoratif.

### 2.11 Accuracy

**Tujuan:** Menjelaskan proporsi seluruh prediksi benar.

**Isi wajib:** Formula, interpretasi, dan keterbatasan pada distribusi kelas tidak seimbang.

**Batas:** Accuracy tidak boleh menjadi satu-satunya dasar perbandingan.

### 2.12 Precision

**Tujuan:** Menjelaskan ketepatan prediksi `Urgent`.

**Isi wajib:** Formula `TP/(TP+FP)`, hubungan dengan false alarm, dan kondisi denominator nol bila relevan pada implementasi.

### 2.13 Recall

**Tujuan:** Menjelaskan kemampuan menemukan invoice aktual `Urgent`.

**Isi wajib:** Formula `TP/(TP+FN)` dan hubungan langsung dengan False Negative.

### 2.14 F1-score

**Tujuan:** Menjelaskan rata-rata harmonik precision dan recall.

**Isi wajib:** Formula, alasan penggunaan, dan perbedaan F1 kelas `Urgent` dengan macro F1.

**Batas:** Jangan menyatakan F1 mewakili seluruh biaya operasional tanpa cost matrix.

### 2.15 Hold-out Validation

**Tujuan:** Menjelaskan evaluasi dengan satu pembagian data latih dan data uji.

**Isi wajib:**

- Pemisahan data latih dan data uji.
- Stratifikasi untuk mempertahankan proporsi kelas.
- Hubungan rasio 80:20 dengan E1 dan rasio 70:30 dengan E2.
- Seluruh preprocessing, konstruksi aturan, dan pemilihan parameter dilakukan tanpa menggunakan label data uji.
- Keterbatasan hasil yang dapat dipengaruhi oleh satu pembagian data.

**Batas:** Jangan menyamakan hold-out dengan K-fold cross-validation dan jangan memilih skenario berdasarkan hasil terbaik saja.

### 2.16 Cross Validation

**Tujuan:** Menjelaskan evaluasi berulang melalui pembagian fold.

**Isi wajib:**

- K-fold cross-validation.
- Stratifikasi untuk mempertahankan proporsi kelas.
- Prediksi out-of-fold.
- Pemisahan antara evaluasi luar dan pemilihan parameter di data latih.
- Hubungan dengan E3.

**Tindakan:** Tambahkan teori baru dengan sumber metodologis utama.

### 2.17 Leave-One-Out Cross Validation

**Tujuan:** Menjelaskan evaluasi ketika satu observasi menjadi data uji pada setiap iterasi.

**Isi wajib:**

- Jumlah iterasi sama dengan jumlah observasi.
- Setiap invoice memperoleh satu prediksi out-of-sample.
- Kelebihan penggunaan data latih yang hampir lengkap.
- Keterbatasan biaya komputasi dan potensi variasi model.
- Hubungan dengan E4.

**Batas:** Jangan menyatakan LOOCV otomatis paling baik; posisikan sebagai salah satu skenario evaluasi.

### 2.18 McNemar Test

**Tujuan:** Menjelaskan uji statistik untuk dua classifier pada kasus yang sama.

**Isi wajib:**

- Tabel kesesuaian benar/salah kedua metode.
- Kasus concordant dan discordant.
- Definisi `b`: hanya Rule-Based benar.
- Definisi `c`: hanya Decision Tree benar.
- Hipotesis nol tentang kesetaraan proporsi kesalahan marginal.
- Exact McNemar dua sisi dan taraf signifikansi 0,05.

**Interpretasi wajib:** p-value di atas 0,05 berarti bukti belum cukup untuk menolak hipotesis nol. Hal tersebut tidak membuktikan kedua metode identik.

### 2.19 Penelitian Terdahulu

**Tujuan:** Menunjukkan apa yang telah diteliti, apa yang belum dijawab, dan mengapa penelitian ini diperlukan.

**Kelompok studi:**

1. Invoice tracking dan POD.
2. Rule-Based classification atau expert system.
3. Decision Tree pada invoice atau logistik.
4. Perbandingan Rule-Based dan metode machine learning.
5. DSS atau klasifikasi prioritas operasional.

**Kolom tabel wajib:**

| Peneliti/Tahun | Domain | Metode | Target | Sumber Ground Truth | Validasi | Temuan Utama | Keterbatasan | Relevansi |
|---|---|---|---|---|---|---|---|---|

**Aturan sintesis:**

- Setelah tabel, kelompokkan pola temuan berdasarkan tema, bukan mengulang setiap baris.
- Bedakan relevansi langsung dan tidak langsung.
- Jangan menyebut varian algoritma tanpa bukti dari sumber primer.
- Jangan membuat klaim "belum pernah diteliti" hanya dari delapan studi.

**Kebutuhan literatur tambahan:** Studi Rule-Based empiris, studi komparatif Rule-Based versus Decision Tree atau classifier yang setara, dan studi DSS prioritas dengan indikator evaluasi yang jelas.

### 2.20 Research Gap

**Tujuan:** Menutup Bab II dengan argumen yang langsung mengarah ke Bab III.

**Struktur tiga paragraf:**

1. **Apa yang sudah diketahui:** Literatur menjelaskan tracking/POD, penggunaan Decision Tree untuk invoice atau logistik, serta metode prioritas pada domain lain.
2. **Apa yang belum dijawab:** Kumpulan studi yang ditinjau belum memberikan perbandingan langsung Rule-Based berbasis SOP dan Decision Tree berbasis data historis admin pada kasus invoice delivery priority dengan ground truth, kasus validasi, analisis kesalahan, dan uji statistik yang sama.
3. **Posisi penelitian:** Penelitian membangun Rule-Based melalui Knowledge Acquisition, Rule Construction, dan Rule Validation; melatih Decision Tree entropy; lalu membandingkan keduanya pada E1-E4 menggunakan label admin.

**Rumusan akhir yang direkomendasikan:**

> Berdasarkan penelitian yang ditinjau, masih diperlukan evaluasi komparatif langsung antara Rule-Based berbasis SOP dan Decision Tree berbasis data historis admin untuk klasifikasi prioritas pengiriman invoice. Penelitian ini mengisi kebutuhan tersebut dengan menggunakan ground truth admin dan kasus validasi yang sama, evaluasi multi-skenario, analisis kesalahan per invoice, serta uji statistik berpasangan.

## 4. Tabel yang Diperlukan

1. Tabel perbedaan ID3, C4.5, CART, dan implementasi penelitian.
2. Tabel confusion matrix biner.
3. Tabel ringkas definisi metrik, formula, dan fokus kesalahan, jika dibutuhkan untuk mengurangi repetisi.
4. Tabel sintesis penelitian terdahulu.

Semua tabel harus ditulis lengkap dalam LaTeX pada tahap implementasi. Tidak boleh menggunakan placeholder tabel.

## 5. Kebijakan Gambar

Tidak ada gambar yang wajib untuk memahami Bab II. Diagram siklus invoice, arsitektur Rule-Based, struktur Decision Tree, dan confusion matrix lama dapat dihapus jika tabel dan narasi sudah memadai.

Jika pembimbing tetap meminta gambar, gunakan placeholder LaTeX dan satu Figure Prompt untuk setiap gambar. Jangan menggunakan TikZ, Mermaid, PlantUML, Graphviz, atau ASCII diagram.

## 6. Rencana Sitasi

| Bagian | Jenis Sumber |
|---|---|
| Invoice Tracking dan POD | Artikel primer tentang document tracking, invoice administration, dan POD |
| Rule-Based | Buku atau artikel primer tentang rule-based/expert systems, verification, coverage, dan conflict |
| Knowledge Acquisition dan Rule Construction | Literatur knowledge engineering dan validation of knowledge bases |
| Decision Tree dan entropy | Sumber algoritmik utama dan dokumentasi implementasi yang digunakan |
| ID3-C4.5-CART | Sumber primer atau buku machine learning yang membedakan algoritma secara eksplisit |
| Metrik klasifikasi | Buku atau artikel metodologis evaluasi classifier |
| Hold-out, Cross Validation, dan LOOCV | Literatur resampling dan model assessment |
| McNemar | Literatur uji paired nominal outcomes atau evaluasi classifier |
| Research gap | Sumber primer yang telah dipetakan pada tabel penelitian terdahulu |

Dokumentasi scikit-learn dapat digunakan untuk menjelaskan perilaku library. Konsep algoritmik tetap sebaiknya didukung buku atau artikel ilmiah utama.

## 7. Hubungan dengan Bab III dan Bab IV

| Konsep Bab II | Implementasi Bab III | Analisis Bab IV |
|---|---|---|
| Knowledge Acquisition dan Rule Construction | Pembentukan R1-R8 | Traceability, coverage, conflict, dan error Rule-Based |
| Supervised Classification dan Decision Tree | Training pipeline dan parameter | Tree structure, feature importance, dan error Decision Tree |
| Entropy | `criterion="entropy"` | Interpretasi model tanpa menyebut C4.5 |
| Hold-out Validation | E1 dan E2 | Perbandingan hasil dua proporsi data latih-uji |
| Cross Validation dan LOOCV | E3 dan E4 | Stabilitas hasil multi-skenario |
| Confusion Matrix dan metrik | Prosedur evaluasi | Accuracy, precision, recall, F1, FP, dan FN |
| McNemar | Uji berpasangan | Interpretasi signifikansi statistik |
| Penelitian terdahulu dan gap | Dasar desain komparatif | Hubungan temuan dengan literatur |

## 8. Kriteria Penerimaan

- [ ] Struktur Bab II tepat 2.1-2.20.
- [ ] Setiap teori mendukung langkah Bab III atau analisis Bab IV.
- [ ] Decision Tree penelitian dinyatakan berbasis entropy dan bukan C4.5.
- [ ] ID3, C4.5, CART, dan implementasi penelitian dibedakan secara eksplisit.
- [ ] Gain ratio tidak dinyatakan sebagai mekanisme penelitian.
- [ ] Knowledge Acquisition dan Rule Construction tidak membentuk ground truth.
- [ ] `Urgent` ditetapkan sebagai kelas positif pada seluruh definisi metrik.
- [ ] Hold-out, Cross Validation, LOOCV, dan exact McNemar dijelaskan.
- [ ] Studi terdahulu mencakup tracking/POD, invoice, Rule-Based, komparatif, dan DSS atau kekurangannya dinyatakan transparan.
- [ ] Research gap diturunkan dari tabel penelitian terdahulu.
- [ ] Tidak ada hasil eksperimen penelitian ini pada Bab II.
- [ ] Tidak ada gambar TikZ pada versi LaTeX final.
