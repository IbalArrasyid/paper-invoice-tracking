# Blueprint Bab IV: Hasil dan Pembahasan

## 1. Tujuan Bab

Bab IV harus menjawab perbandingan Rule-Based dan Decision Tree, bukan hanya melaporkan metrik masing-masing. Analisis mencakup kinerja prediksi, pola kesalahan, kestabilan, interpretabilitas, dan karakteristik operasional.

## 2. Batas Bukti

- Dataset sumber berisi 101 baris dan 99 invoice unik setelah dua duplikat dihapus.
- Distribusi kelas terdiri atas 30 `Urgent` dan 69 `Not Urgent`.
- Kolom sumber adalah `expert_label`, dengan normalisasi `HIGH = Urgent` dan `NORMAL = Not Urgent`.
- Bukti bahwa `expert_label` berasal dari keputusan admin harus dicantumkan dalam skripsi.
- Hasil E1-E4 tidak boleh diubah atau dipilih berdasarkan hasil yang paling menguntungkan.
- `p = 0,2891` tidak membuktikan kedua metode sama. Nilai tersebut menunjukkan bukti belum cukup untuk menyatakan perbedaan tingkat kesalahan pada taraf 5%.
- Temuan berlaku pada dataset dan konteks perusahaan yang diteliti.

## 3. Struktur Bab IV

### 4.1 Analisis Dataset dan Ground Truth

**Tujuan**

Menjelaskan kualitas data, distribusi kelas, proses pembersihan, dan dasar penggunaan label sebelum hasil model dibahas.

**Isi yang dibahas**

1. Sumber dan unit analisis data.
2. Perubahan dari 101 baris menjadi 99 invoice unik.
3. Distribusi 30 `Urgent` dan 69 `Not Urgent`.
4. Normalisasi label `HIGH` dan `NORMAL` menjadi kelas biner.
5. Enam catatan kualitas data pada empat invoice terkait cutoff dan jadwal penerimaan.
6. Penghapusan fitur yang berisiko bocor: `expert_reason`, `sent_date`, identifier, identitas pelanggan, dan `Driver`.
7. Perhitungan ulang fitur cutoff berdasarkan kondisi pada `receive_date`.
8. Batas provenance kolom `expert_label`.

**Tabel yang diperlukan**

- Tabel 4.1: Audit dataset, duplikat, dan distribusi kelas.
- Tabel 4.2: Kebijakan fitur, kebocoran data, dan masalah kualitas.

Semua tabel harus dibuat sebagai tabel LaTeX lengkap saat tahap penulisan.

**Gambar yang diperlukan**

Tidak ada gambar wajib. Grafik distribusi kelas bersifat opsional karena informasinya sudah cukup disampaikan melalui Tabel 4.1.

**Interpretasi utama**

- Distribusi kelas tidak seimbang sempurna, tetapi kedua kelas tetap terwakili.
- Pembersihan menghasilkan unit analisis berbasis invoice unik.
- Penghapusan fitur pascakeputusan mengurangi risiko kebocoran target.
- Ground truth adalah referensi operasional, bukan kebenaran universal.

### 4.2 Desain Eksperimen

**Tujuan**

Menunjukkan bahwa perbandingan dilakukan secara adil, berpasangan, dan dapat direproduksi.

**Isi yang dibahas**

1. E1: stratified hold-out 80:20.
2. E2: stratified hold-out 70:30.
3. E3: stratified 5-fold cross-validation.
4. E4: leave-one-out cross-validation.
5. Penggunaan invoice validasi yang sama untuk kedua metode.
6. Penetapan `Urgent` sebagai kelas positif.
7. Random seed 42.
8. Rule Base dibekukan sebelum evaluasi.
9. One-hot encoding dan pemilihan parameter Decision Tree dilakukan pada data latih.
10. Kandidat `max_depth` adalah 2, 3, 4, atau tanpa batas; `min_samples_leaf` adalah 1, 2, atau 4.
11. Metrik E3 dan E4 dihitung dari gabungan prediksi out-of-fold.
12. Exact McNemar digunakan untuk perbandingan berpasangan.

**Tabel yang diperlukan**

- Tabel 4.3: Konfigurasi E1-E4.
- Tabel 4.4: Konfigurasi metode, metrik, dan kontrol validitas.

**Gambar yang diperlukan**

- Gunakan rancangan `FP-02` untuk alur desain eksperimen dan evaluasi berpasangan.
- Saat dimasukkan ke LaTeX, gunakan placeholder dengan komentar `% Figure Prompt: FP-02`.

**Interpretasi utama**

- E1 dan E2 menunjukkan sensitivitas terhadap pembagian data.
- E3 dan E4 memberi prediksi out-of-fold untuk seluruh invoice.
- Beberapa skenario mengurangi ketergantungan pada satu pembagian data.

### 4.3 Hasil Rule-Based

**Tujuan**

Menilai kemampuan aturan SOP dalam mereproduksi kelas pada ground truth dan menjelaskan setiap keputusan melalui Rule ID.

**Isi yang dibahas**

1. Metrik Rule-Based pada E1-E4.
2. Matriks kebingungan setiap skenario.
3. Aktivasi R1-R8, termasuk aturan yang tidak aktif.
4. Penggunaan R8 sebagai aturan default pada 75 invoice.
5. Konflik atau aktivasi lebih dari satu aturan, misalnya `R3;R6`.
6. Enam false negative dan nol false positive pada evaluasi 99 invoice.
7. Traceability dari kondisi SOP menuju Rule ID dan hasil klasifikasi.

**Tabel yang diperlukan**

- Tabel 4.5: Metrik dan matriks kebingungan Rule-Based per skenario.
- Tabel 4.6: Aktivasi aturan, default, konflik, dan ringkasan kesalahan.

**Gambar yang diperlukan**

Tidak ada gambar wajib. Grafik aktivasi aturan boleh digunakan jika tidak mengulang Tabel 4.6.

**Interpretasi utama**

- Rule-Based konsisten tidak menghasilkan false positive pada E3 dan E4.
- Recall `Urgent` sebesar 0,8000 menunjukkan enam invoice urgent tidak tertangkap.
- Precision tinggi tidak boleh dibaca tanpa mempertimbangkan false negative.
- R8 yang dominan menunjukkan sebagian besar invoice tidak memenuhi kondisi urgensi eksplisit.

### 4.4 Hasil Decision Tree

**Tujuan**

Menilai kemampuan Decision Tree mempelajari pola label historis dan menjelaskan kompleksitas model.

**Isi yang dibahas**

1. Metrik Decision Tree pada E1-E4.
2. Matriks kebingungan setiap skenario.
3. Parameter terpilih pada setiap skenario atau fold.
4. Kedalaman dan jumlah daun.
5. Model interpretatif seluruh data: kedalaman 2 dan 4 daun.
6. Feature importance: `limited_receive_schedule_flag` 56,96%, `days_to_cutoff_feature` 39,78%, dan `cutoff_value_feature` 3,26%.
7. Representative decision path untuk kasus benar dan salah.
8. Pemisahan tegas antara model interpretatif seluruh data dan metrik validasi.

**Tabel yang diperlukan**

- Tabel 4.7: Metrik dan matriks kebingungan Decision Tree per skenario.
- Tabel 4.8: Parameter, kompleksitas, dan feature importance model interpretatif.

**Gambar yang diperlukan**

- Visualisasi Decision Tree interpretatif direkomendasikan.
- Buat prompt baru di `Figure-Prompts.md` sebelum menambahkan placeholder LaTeX. Gunakan calon ID `FP-03`.
- Caption harus menyatakan bahwa pohon dilatih pada seluruh data untuk interpretasi, bukan estimasi performa.

**Interpretasi utama**

- Decision Tree menunjukkan struktur sederhana pada dataset ini.
- Importance menggambarkan kontribusi terhadap pengurangan impurity, bukan hubungan sebab-akibat.
- Performa validasi harus diambil dari E1-E4, bukan dari model seluruh data.

### 4.5 Analisis Performa Komparatif

**Tujuan**

Membandingkan kedua metode secara langsung pada invoice validasi yang sama.

**Isi yang dibahas**

1. Perbandingan accuracy, precision, recall, F1 `Urgent`, dan macro F1.
2. Perbandingan FP dan FN.
3. Perubahan hasil antar-skenario.
4. Hasil berpasangan dan exact McNemar.
5. Perbedaan antara keunggulan deskriptif dan signifikansi statistik.

**Tabel yang diperlukan**

- Tabel 4.9: Metrik kedua metode dan selisih deskriptif per skenario.
- Tabel 4.10: Prediksi berpasangan dan exact McNemar.

Stabilitas per fold dapat ditempatkan dalam lampiran jika tabel utama menjadi terlalu padat.

**Gambar yang diperlukan**

- Grafik komparatif metrik E1-E4 direkomendasikan.
- Buat prompt baru dengan calon ID `FP-04` sebelum placeholder LaTeX dibuat.
- Skala sumbu harus ditampilkan jelas dan tidak boleh melebih-lebihkan selisih kecil.

**Interpretasi per skenario**

- E1: kedua metode memperoleh akurasi 1,0000 pada 20 invoice uji. Hasil ini tidak cukup untuk kesimpulan umum.
- E2: Decision Tree menunjukkan akurasi dan recall `Urgent` lebih tinggi.
- E3: Decision Tree menunjukkan accuracy 0,9596 dibanding 0,9394, tetapi `p = 0,7266`.
- E4: Decision Tree menunjukkan accuracy 0,9798 dibanding 0,9394 dan recall `Urgent` 0,9667 dibanding 0,8000.
- E4 menghasilkan `p = 0,2891`; bukti belum cukup untuk menyatakan perbedaan statistik.

Jangan menghitung rata-rata sederhana E1-E4 karena ukuran dan struktur validasinya berbeda serta kasus evaluasinya saling tumpang tindih.

### 4.6 Analisis Karakteristik Komparatif

**Tujuan**

Membandingkan karakteristik operasional dengan indikator yang dapat ditelusuri. Bagian ini tidak boleh menggunakan opini tanpa bukti.

**Tabel utama yang diperlukan**

- Tabel 4.11: Matriks indikator, bukti, dan batas interpretasi karakteristik metode.

**Gambar yang diperlukan**

Tidak ada gambar wajib. Matriks tabel lebih tepat daripada radar chart karena sebagian indikator bersifat kualitatif dan tidak berada pada skala yang sama.

**Indikator ilmiah**

| Aspek | Indikator | Rule-Based | Decision Tree | Batas interpretasi |
|---|---|---|---|---|
| Explainability | Ketersediaan jejak keputusan dan panjang penjelasan | Rule ID, kondisi aktif, prioritas | Decision path, threshold, kedalaman | Bandingkan traceability, bukan preferensi pribadi |
| Maintainability | Jumlah komponen, dependensi, konflik, dan langkah validasi | Jumlah aturan dan konflik | Pipeline, parameter, versi model | Memerlukan prosedur terdokumentasi |
| Adaptability | Prosedur merespons perubahan | Ubah aturan saat SOP berubah | Tambah label, latih ulang, validasi ulang | Analisis prosedural karena belum ada eksperimen perubahan |
| Scalability | Pertumbuhan kompleksitas | Interaksi aturan ketika kondisi bertambah | Waktu latih dan kompleksitas saat data/fitur bertambah | Hanya konseptual tanpa scale experiment |
| Computational cost | Waktu training dan inference, dipisahkan | Tidak ada training; ukur inference | Ukur training dan inference | Harus diulang pada lingkungan yang sama sebelum ranking |
| Rule transparency | Hubungan langsung antara kondisi dan keluaran | Kondisi eksplisit dan Rule ID | Threshold pada decision path | Decision Tree bukan Rule Base SOP |
| Ease of updating | Langkah perubahan dan validasi | Edit, cek konflik, validasi aturan | Kumpulkan label, retrain, revalidate | Jangan menyamakan sedikit langkah dengan governance yang lebih baik |
| SOP compliance | Traceability ke klausul SOP | Langsung melalui matriks rule-to-SOP | Tidak langsung; analisis path-to-concept | Kepatuhan SOP berbeda dari kecocokan dengan label admin |
| Auditability | Artefak yang dapat direproduksi | Versi Rule Base dan Rule ID | Versi model, fitur, parameter, path | Nilai hanya berdasarkan artefak yang tersedia |

**Interpretasi utama**

- Rule-Based menyediakan hubungan keputusan yang lebih langsung dengan SOP.
- Decision Tree menyediakan decision path, tetapi strukturnya berasal dari pola data.
- Adaptability dan scalability belum diuji secara empiris. Kesimpulan harus disebut prosedural atau konseptual.
- Waktu komputasi tidak boleh dibandingkan tanpa memisahkan training dan inference serta mengontrol lingkungan pengukuran.

### 4.7 Analisis Error dan Misclassification

**Tujuan**

Menjelaskan mengapa selisih metrik muncul dan menunjukkan bahwa kedua metode memiliki pola keputusan berbeda.

**Dasar analisis utama: E4 LOOCV**

| Kelompok | Jumlah | Kasus |
|---|---:|---|
| Keduanya benar | 91 | Pilih contoh `Urgent` dan `Not Urgent` yang representatif |
| Hanya Rule-Based benar | 2 | `S202605-1801`, `S202605-1800` |
| Hanya Decision Tree benar | 6 | `S202605-0737`, `S202605-0715`, `S202605-0632`, `S202605-0721`, `S202605-0710`, `S202605-0708` |
| Keduanya salah | 0 | Tidak ada pada E4 |

Jika kategori keduanya salah perlu dibahas, gunakan kasus `S202605-0708` pada E3 dan nyatakan skenarionya secara eksplisit. Jangan mencampur jumlah E3 dengan E4.

Pada E4, enam kasus hanya Decision Tree benar merupakan false negative Rule-Based. Dua kasus hanya Rule-Based benar terdiri atas false negative Decision Tree (`S202605-1801`) dan false positive Decision Tree (`S202605-1800`).

**Isi yang dibahas**

1. Ground truth dan prediksi kedua metode.
2. Fitur cutoff dan jadwal penerimaan.
3. Rule ID atau R8 sebagai default.
4. Decision path dan probabilitas prediksi.
5. Jenis kesalahan FP atau FN.
6. Perubahan hasil kasus yang sama antar-skenario.
7. Implikasi operasional tanpa mengarang biaya kesalahan.

Enam false negative Rule-Based berkaitan dengan jadwal penerimaan terbatas dan jarak jadwal berikutnya 2-5 hari. Pola ini menunjukkan bahwa ambang aturan lebih konservatif daripada pola pada label sumber.

**Tabel yang diperlukan**

- Tabel 4.12: Kelompok prediksi E4 dan detail kasus terpilih.

Kasus tidak stabil antar-skenario dapat dibahas dalam teks atau lampiran.

**Gambar yang diperlukan**

Tidak ada gambar wajib. Tabel kasus lebih informatif karena harus menampilkan atribut, Rule ID, dan decision path.

**Nilai ilmiah bagian ini**

- Menjelaskan perbedaan yang tidak terlihat dari accuracy.
- Menunjukkan trade-off nol false positive dan jumlah false negative Rule-Based.
- Menunjukkan invoice yang dipelajari Decision Tree di luar ambang aturan eksplisit.
- Menjadi dasar pembahasan relevansi operasional kedua metode.

### 4.8 Pembahasan

**Tujuan**

Mengintegrasikan temuan performa, statistik, error, teori, dan konteks Decision Support System.

#### 4.8.1 Penjelasan Hasil

Bahas secara hati-hati:

1. Performa Decision Tree yang lebih tinggi konsisten dengan kemampuannya mempelajari kombinasi pola historis di luar ambang Rule-Based.
2. Pola enam false negative Rule-Based mendukung penjelasan tentang batas aturan yang konservatif.
3. Penjelasan tersebut bersifat konsisten dengan data, bukan bukti kausal.
4. Perbedaan statistik belum terdeteksi karena hanya sedikit prediksi yang tidak sama dan ukuran sampel terbatas.
5. Pada E4 hanya delapan kasus discordant: dua hanya Rule-Based benar dan enam hanya Decision Tree benar.
6. `p = 0,2891` berarti hipotesis nol tidak dapat ditolak pada taraf 5%, bukan berarti metode identik.

#### 4.8.2 Relevansi Metode

Rule-Based layak dipertimbangkan ketika:

- keputusan harus mengikuti SOP secara eksplisit;
- audit membutuhkan Rule ID yang langsung;
- aturan relatif stabil; dan
- data historis berlabel terbatas.

Decision Tree layak dipertimbangkan ketika:

- tersedia label historis yang representatif;
- pola keputusan tidak seluruhnya tertulis dalam SOP;
- deteksi `Urgent` menjadi perhatian utama; dan
- organisasi mampu melakukan retraining, versioning, dan validasi.

Pernyataan tersebut adalah kondisi penggunaan, bukan rekomendasi final. Rekomendasi sistem memerlukan prioritas risiko dan tata kelola dari perusahaan.

#### 4.8.3 Hubungan dengan Teori dan Penelitian Terdahulu

- Hubungkan Rule-Based dengan explicit knowledge representation, traceability, dan ketergantungan pada kelengkapan aturan.
- Hubungkan Decision Tree dengan supervised learning, recursive partitioning, interpretability, dan risiko overfitting.
- Bandingkan hasil dengan penelitian terdahulu hanya jika target, dataset, dan desain evaluasinya sebanding.
- Gunakan referensi yang sudah diverifikasi di Bab II. Jangan membuat sitasi baru tanpa sumber.
- Jelaskan kontribusi DSS sebagai penyedia rekomendasi, bukan pengganti keputusan manusia.

#### 4.8.4 Threats to Validity

| Jenis ancaman | Ancaman | Mitigasi atau batas klaim |
|---|---|---|
| Construct validity | `expert_label` dipakai sebagai keputusan admin, tetapi provenance tidak tertulis di workbook | Tambahkan bukti dari perusahaan dan nyatakan label sebagai referensi operasional |
| Internal validity | Penilaian manusia dapat subjektif | Dokumentasikan sumber, waktu, dan proses pemberian label |
| Internal validity | Penyusunan Rule Base melibatkan interpretasi SOP | Tampilkan rule-to-SOP traceability dan validasi pakar |
| Data validity | Enam catatan derivasi fitur pada empat invoice | Laporkan penanganan dan lakukan pemeriksaan sensitivitas bila diperlukan |
| Statistical conclusion validity | Hanya 99 invoice dan sedikit kasus discordant | Laporkan exact McNemar dan hindari klaim superioritas |
| Statistical conclusion validity | Hold-out sensitif terhadap pembagian data | Gunakan E1-E4 dan utamakan pola konsisten |
| Model validity | Decision Tree dapat overfit | Gunakan inner validation, batas kedalaman, dan out-of-fold evaluation |
| Method validity | Rule-Based bergantung pada kelengkapan SOP | Laporkan default rule, coverage, konflik, dan kasus yang terlewat |
| Temporal validity | SOP dan pola admin dapat berubah | Batasi hasil pada periode data dan sarankan validasi berkala |
| External validity | Satu perusahaan dan satu proses invoice | Jangan menggeneralisasi ke organisasi lain tanpa validasi eksternal |

**Tabel yang diperlukan**

- Tabel 4.13: Threats to validity dan mitigasi.

Sintesis dengan teori ditulis dalam paragraf agar tidak mengulang tabel hasil.

**Gambar yang diperlukan**

Tidak ada gambar wajib.

### 4.9 Ringkasan Bab

**Tujuan**

Merangkum jawaban ilmiah Bab IV tanpa mengulang seluruh angka.

**Poin yang harus ditulis**

1. Decision Tree menunjukkan nilai performa deskriptif lebih tinggi pada E2-E4, terutama untuk mendeteksi kelas `Urgent`.
2. Perbedaan belum menunjukkan signifikansi statistik pada evaluasi berpasangan.
3. Rule-Based tetap relevan karena traceability SOP dan tidak menghasilkan false positive pada evaluasi penuh.
4. Kedua metode memiliki pola kesalahan dan kebutuhan tata kelola yang berbeda.
5. Pemilihan metode bergantung pada kebutuhan deteksi urgency, kepatuhan SOP, auditability, dan kemampuan pemeliharaan model.
6. Temuan dibatasi oleh ukuran dataset, provenance label, dan konteks satu perusahaan.

**Larangan**

- Jangan menulis bahwa Decision Tree terbukti lebih unggul.
- Jangan menafsirkan `p > 0,05` sebagai bukti kesamaan metode.
- Jangan memasukkan angka baru.
- Jangan mengulang tabel hasil.
- Jangan menambahkan rekomendasi yang tidak didukung kebutuhan perusahaan.

## 4. Daftar Artefak Sumber

| Bukti | Lokasi |
|---|---|
| Ringkasan eksperimen | `Comparative-Experiment-Report.md` |
| Metrik E1-E4 | `comparative_experiment/tables/metrics_by_scenario.csv` |
| Matriks kebingungan | `comparative_experiment/tables/confusion_matrices.csv` |
| Perbandingan berpasangan | `comparative_experiment/tables/paired_comparison.csv` |
| Metrik per fold | `comparative_experiment/tables/five_fold_metrics.csv` |
| Aktivasi aturan | `comparative_experiment/tables/rule_usage.csv` |
| Kompleksitas Decision Tree | `comparative_experiment/tables/decision_tree_complexity.csv` |
| Feature importance | `comparative_experiment/tables/final_tree_feature_importance.csv` |
| Kasus kesalahan | `comparative_experiment/tables/misclassification_cases.csv` |
| Prediksi per invoice | `comparative_experiment/predictions/all_scenario_predictions.csv` |

## 5. Urutan Implementasi LaTeX

1. Tulis Bagian 4.1 dan 4.2 untuk menetapkan bukti dan desain.
2. Tulis hasil Rule-Based dan Decision Tree tanpa membuat kesimpulan komparatif lebih awal.
3. Bangun Tabel 4.9 dan 4.10 sebagai pusat perbandingan.
4. Tulis analisis error berdasarkan E4 dan tandai jelas jika memakai E3.
5. Lengkapi indikator karakteristik hanya dengan bukti yang tersedia.
6. Tulis pembahasan setelah seluruh tabel stabil.
7. Tulis ringkasan paling akhir.
8. Buat tabel sebagai LaTeX lengkap dengan caption dan label.
9. Gunakan placeholder untuk setiap gambar dan tambahkan prompt yang sesuai ke `Figure-Prompts.md`.
10. Audit semua angka terhadap artefak sumber sebelum kompilasi.

## 6. Kriteria Penerimaan

- [ ] Struktur 4.1-4.9 diterapkan.
- [ ] E1-E4 dibahas tanpa memilih hasil tertentu.
- [ ] Kedua metode dibandingkan pada kasus yang sama.
- [ ] FP dan FN diberi interpretasi operasional.
- [ ] Exact McNemar dijelaskan dengan benar.
- [ ] Error analysis menggunakan invoice yang terverifikasi.
- [ ] Karakteristik empiris, prosedural, dan konseptual dibedakan.
- [ ] Rule-Based tidak diposisikan sebagai pesaing yang tidak relevan.
- [ ] Decision Tree tidak disebut lebih unggul secara statistik.
- [ ] Threats to validity mencakup data, label, metode, statistik, waktu, dan generalisasi.
- [ ] Semua tabel lengkap saat diimplementasikan dalam LaTeX.
- [ ] Semua gambar menggunakan placeholder dan prompt.
- [ ] Tidak ada hasil legacy tiga kelas yang digunakan.
