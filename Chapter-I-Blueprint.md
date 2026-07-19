# Blueprint Final Bab I: Pendahuluan

**Status:** Final setelah audit akademik. Dokumen ini menjadi panduan revisi, bukan naskah LaTeX.

## 1. Posisi Ilmiah Bab I

Bab I harus mengantar pembaca pada kebutuhan analisis komparatif antara klasifikasi Rule-Based dan Decision Tree untuk prioritas pengiriman invoice. Label historis admin menjadi ground truth bersama. Sistem invoice tracking dan Proof of Delivery (POD) hanya menjadi konteks penerapan.

Kontribusi utama bukan algoritma baru, sistem baru, atau Operational Knowledge Formalization Framework. Knowledge Acquisition, Rule Construction, dan Rule Validation tetap dipertahankan sebagai proses pembentukan Rule-Based.

## 2. Judul yang Direkomendasikan

**Bahasa Indonesia**

> Analisis Komparatif Metode Rule-Based dan Decision Tree untuk Klasifikasi Prioritas Pengiriman Invoice

**Bahasa Inggris**

> Comparative Analysis of Rule-Based and Decision Tree Methods for Invoice Delivery Priority Classification

Istilah C4.5 harus dihapus dari judul karena implementasi menggunakan `DecisionTreeClassifier` berbasis entropy, bukan algoritma C4.5.

## 3. Struktur Bab I

1. 1.1 Latar Belakang
2. 1.2 Rumusan Masalah
3. 1.3 Tujuan Penelitian
4. 1.4 Batasan Masalah
5. 1.5 Kontribusi Penelitian, jika diizinkan format program studi
6. 1.6 Sistematika Penulisan, jika diwajibkan format program studi

## 4. Blueprint Latar Belakang

Latar belakang wajib terdiri atas enam paragraf. Setiap paragraf hanya memuat satu ide utama.

### Paragraf 1: Konteks Operasional

**Fungsi:** Menjelaskan peran invoice dan POD dalam administrasi penagihan B2B.

**Muatan:** Invoice perlu dikirim, dilacak, dan dibuktikan penerimaannya. POD mendukung verifikasi penerimaan. Sistem pelacakan menyimpan status dan riwayat dokumen.

**Batas:** Jangan memasukkan teori panjang, rincian arsitektur sistem, atau klaim dampak finansial tanpa data perusahaan.

### Paragraf 2: Masalah Prioritas Invoice

**Fungsi:** Menetapkan masalah keputusan yang diteliti.

**Muatan:** Perbedaan jadwal penerimaan dan cutoff menuntut penentuan invoice yang perlu didahulukan. Target keputusan adalah `Urgent` dan `Not Urgent`. Keputusan perlu konsisten, dapat dijelaskan, dan dapat dievaluasi.

**Batas:** Jangan menyatakan keputusan admin tidak konsisten atau SOP tidak efektif tanpa bukti.

### Paragraf 3: Rule-Based

**Fungsi:** Memperkenalkan pendekatan berbasis pengetahuan.

**Muatan:** SOP diperoleh melalui Knowledge Acquisition, diterjemahkan melalui Rule Construction, dan diperiksa melalui Rule Validation. Hasilnya adalah Rule-Based yang transparan dan dapat ditelusuri ke aturan operasional.

**Batas:** Knowledge Engineering adalah proses pendukung Rule-Based, bukan kontribusi utama penelitian. Rincian aturan R1-R8 ditempatkan di Bab III.

### Paragraf 4: Decision Tree

**Fungsi:** Memperkenalkan pendekatan berbasis data.

**Muatan:** Decision Tree mempelajari hubungan atribut historis dengan label admin. Model dapat menghasilkan jalur keputusan yang dapat diperiksa, tetapi tetap memerlukan data representatif, pengendalian overfitting, dan evaluasi pada data yang tidak digunakan untuk pelatihan.

**Batas:** Sebut metode sebagai Decision Tree berbasis entropy, bukan C4.5. Jangan menyatakan performanya lebih tinggi sebelum Bab IV.

### Paragraf 5: Research Gap

**Fungsi:** Menjelaskan alasan ilmiah perbandingan dilakukan.

**Muatan:** Literatur yang digunakan saat ini membahas invoice, pelacakan dokumen, POD, Decision Tree, dan prioritas pada konteks yang terpisah. Bukti yang secara langsung membandingkan klasifikasi berbasis SOP dan klasifikasi berbasis data historis admin pada kasus prioritas pengiriman invoice masih belum ditunjukkan oleh kumpulan referensi tersebut. Perbandingan memerlukan ground truth yang tidak dibentuk oleh salah satu metode.

**Rumusan gap:**

> Kumpulan penelitian terdahulu yang ditinjau belum memberikan bukti komparatif langsung mengenai performa, pola kesalahan, dan karakteristik operasional Rule-Based berbasis SOP dan Decision Tree berbasis data historis admin untuk klasifikasi prioritas pengiriman invoice.

Gunakan frasa "kumpulan penelitian yang ditinjau". Klaim bahwa tidak pernah ada penelitian serupa memerlukan penelusuran literatur yang lebih sistematis.

### Paragraf 6: Posisi Penelitian

**Fungsi:** Menjelaskan tindakan dan batas kontribusi penelitian.

**Muatan:** Rule-Based dibangun dari SOP, sedangkan Decision Tree dilatih menggunakan data historis berlabel admin. Keduanya dievaluasi pada kasus validasi dan ground truth yang sama melalui hold-out terstratifikasi, 5-fold cross-validation, dan LOOCV. Perbandingan mencakup performa, pola kesalahan, uji berpasangan, serta karakteristik operasional. Hasil klasifikasi digunakan sebagai rekomendasi dalam konteks sistem invoice tracking dan POD.

**Batas:** Jangan menuliskan nilai akurasi, p-value, hasil eksperimen, atau kesimpulan superioritas metode.

## 5. Rumusan Masalah

1. Bagaimana membangun klasifikasi Rule-Based dari SOP perusahaan dan Decision Tree berbasis entropy dari data historis berlabel admin pada target biner yang sama?
2. Bagaimana perbandingan performa dan pola kesalahan kedua metode pada skenario E1-E4 ketika dievaluasi terhadap label historis admin yang sama?
3. Bagaimana perbedaan karakteristik Rule-Based dan Decision Tree ditinjau dari indikator explainability, maintainability, adaptability, scalability, biaya komputasi, transparansi aturan, kemudahan pembaruan, dan kepatuhan terhadap SOP?

Rumusan masalah tidak menggunakan pertanyaan "metode mana yang paling unggul" karena kesimpulan harus mempertimbangkan hasil statistik dan konteks penggunaan.

## 6. Tujuan Penelitian

1. Membangun dan memvalidasi Rule-Based melalui Knowledge Acquisition, Rule Construction, dan Rule Validation serta melatih Decision Tree berbasis entropy menggunakan data historis berlabel admin.
2. Mengevaluasi dan membandingkan performa serta pola kesalahan kedua metode pada skenario E1-E4 terhadap ground truth yang sama.
3. Menganalisis perbedaan karakteristik operasional kedua metode menggunakan indikator yang dinyatakan secara eksplisit.

Gunakan verba terukur: membangun, memvalidasi, melatih, mengevaluasi, membandingkan, dan menganalisis. Hindari "membuktikan keunggulan".

## 7. Kontribusi Penelitian

1. Prosedur pembentukan Rule-Based yang dapat ditelusuri dari SOP melalui Knowledge Acquisition, Rule Construction, dan Rule Validation.
2. Evaluasi komparatif berpasangan antara Rule-Based dan Decision Tree pada ground truth admin dan kasus validasi yang sama.
3. Analisis yang menggabungkan metrik prediksi, FP/FN, kesalahan per invoice, uji McNemar, serta karakteristik operasional kedua metode.

Sistem invoice tracking dan POD adalah konteks penerapan hasil, bukan kontribusi ilmiah utama.

## 8. Keselarasan Rumusan Masalah, Tujuan, dan Kontribusi

| Fokus | Rumusan Masalah | Tujuan | Kontribusi |
|---|---|---|---|
| Konstruksi metode | RM1 | T1 | Rule-Based tertelusur ke SOP dan Decision Tree entropy yang terdefinisi jelas |
| Evaluasi komparatif | RM2 | T2 | Evaluasi berpasangan dan analisis kesalahan pada E1-E4 |
| Karakteristik metode | RM3 | T3 | Perbandingan operasional berbasis indikator |

Tidak boleh ada tujuan atau kontribusi yang tidak memiliki pasangan pada rumusan masalah.

## 9. Batasan Masalah

1. Unit analisis adalah 99 invoice unik dari 101 baris sumber setelah dua duplikat ditangani.
2. Distribusi dataset bersih adalah 30 `Urgent` dan 69 `Not Urgent`.
3. Ground truth berasal dari `expert_label` sebagai label historis admin.
4. Penelitian dibatasi pada satu perusahaan dan periode data yang tersedia.
5. Metode yang dibandingkan adalah Rule-Based dan Decision Tree berbasis entropy.
6. Rule-Based menggunakan aturan R1-R8 yang diturunkan dari SOP dan dibekukan sebelum evaluasi.
7. Predictor hanya menggunakan informasi yang tersedia pada waktu keputusan.
8. `sent_date`, `expert_reason`, identifier, identitas pelanggan, dan `Driver` tidak digunakan sebagai predictor.
9. Evaluasi menggunakan E1 hold-out 80:20, E2 hold-out 70:30, E3 stratified 5-fold cross-validation, dan E4 LOOCV.
10. Evaluasi kuantitatif meliputi confusion matrix, accuracy, precision, recall, F1-score, macro F1, FP/FN, dan exact McNemar.
11. Adaptability dan scalability dibahas secara prosedural atau konseptual karena tidak diuji melalui eksperimen perubahan SOP atau peningkatan skala data khusus.
12. Penelitian tidak melakukan validasi temporal, eksternal, atau lintas perusahaan.
13. Sistem hanya menjadi konteks penerapan rekomendasi prioritas, pelacakan invoice, dan penyimpanan POD.

## 10. Sistematika Penulisan

- Bab I menjelaskan masalah, tujuan, batasan, dan kontribusi penelitian.
- Bab II menyusun teori, penelitian terdahulu, dan research gap.
- Bab III menjelaskan dataset, pembentukan Rule-Based, pelatihan Decision Tree, pengendalian data leakage, dan desain eksperimen.
- Bab IV menyajikan hasil dan analisis komparatif.
- Bab V merumuskan kesimpulan, keterbatasan, dan saran.

## 11. Larangan Isi Bab I

- Tidak menjelaskan rumus entropy atau metrik evaluasi.
- Tidak memuat aturan R1-R8 secara rinci.
- Tidak memuat parameter Decision Tree secara rinci.
- Tidak memuat angka performa, p-value, atau hasil eksperimen.
- Tidak mengklaim Decision Tree lebih unggul.
- Tidak menggunakan label HIGH, MEDIUM, atau NORMAL sebagai kelas penelitian aktif.
- Tidak menggunakan Guideline-Based Ground Truth.
- Tidak menempatkan Operational Knowledge Formalization Framework sebagai kontribusi utama.

## 12. Kriteria Penerimaan

- [ ] Judul tidak menyebut C4.5.
- [ ] Latar belakang tepat enam paragraf dan satu ide utama per paragraf.
- [ ] Alur latar belakang mengikuti konteks operasional, masalah prioritas, Rule-Based, Decision Tree, research gap, dan posisi penelitian.
- [ ] Ground truth dinyatakan sebagai label historis admin.
- [ ] Rumusan masalah, tujuan, dan kontribusi memiliki tiga fokus yang sejajar.
- [ ] Knowledge Engineering hanya mendukung pembentukan Rule-Based.
- [ ] Sistem hanya diposisikan sebagai konteks penerapan.
- [ ] Tidak ada hasil eksperimen atau klaim superioritas.
- [ ] Batasan konsisten dengan 99 invoice, kelas biner, fitur, dan E1-E4.
- [ ] Semua klaim teoritis memiliki sitasi yang relevan.
