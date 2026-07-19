# Laporan Eksperimen Komparatif

## 1. Dataset

Sumber: `dataset_invoice.xlsx`, lembar `Data Labeling`.

| Item | Hasil |
|---|---:|
| Baris sumber | 101 |
| Invoice unik | 99 |
| Duplikat yang dihapus | 2 |
| Urgent | 30 (30,30%) |
| Not Urgent | 69 (69,70%) |

Kolom `expert_label` dinormalisasi menjadi `HIGH = Urgent` dan `NORMAL = Not Urgent` sesuai arah penelitian. Tidak ada label yang dibuat ulang oleh Rule-Based. Bukti administratif tentang asal label tetap perlu dicantumkan dalam skripsi karena nama kolom sumber bukan `admin_label`.

## 2. Kontrol Kebocoran Data

Fitur yang dikeluarkan: `expert_reason`, `sent_date`, `invoice_no`, identitas pelanggan, dan `Driver`. Nilai `days_to_cutoff` dihitung ulang berdasarkan kondisi saat `receive_date`, bukan `sent_date`. Prapemrosesan dan pemilihan parameter Decision Tree dilakukan hanya pada data latih.

## 3. Desain Eksperimen

- E1: stratified hold-out 80:20.
- E2: stratified hold-out 70:30.
- E3: stratified 5-fold cross-validation.
- E4: leave-one-out cross-validation.

Rule-Based dan Decision Tree diuji pada invoice validasi yang sama. Decision Tree menggunakan kriteria entropy dan pencarian `max_depth` serta `min_samples_leaf` pada data latih.

## 4. Hasil Utama

| Skenario | Metode | Akurasi | Precision Urgent | Recall Urgent | F1 Urgent | Macro F1 |
|---|---|---:|---:|---:|---:|---:|
| E1 80:20 | Rule-Based | 1,0000 | 1,0000 | 1,0000 | 1,0000 | 1,0000 |
| E1 80:20 | Decision Tree | 1,0000 | 1,0000 | 1,0000 | 1,0000 | 1,0000 |
| E2 70:30 | Rule-Based | 0,9333 | 1,0000 | 0,7778 | 0,8750 | 0,9148 |
| E2 70:30 | Decision Tree | 0,9667 | 1,0000 | 0,8889 | 0,9412 | 0,9590 |
| E3 5-fold | Rule-Based | 0,9394 | 1,0000 | 0,8000 | 0,8889 | 0,9236 |
| E3 5-fold | Decision Tree | 0,9596 | 0,9643 | 0,9000 | 0,9310 | 0,9512 |
| E4 LOOCV | Rule-Based | 0,9394 | 1,0000 | 0,8000 | 0,8889 | 0,9236 |
| E4 LOOCV | Decision Tree | 0,9798 | 0,9667 | 0,9667 | 0,9667 | 0,9761 |

## 5. Interpretasi

Decision Tree lebih tinggi secara deskriptif pada E2-E4, terutama pada recall kelas `Urgent`. Pada E4, Rule-Based menghasilkan 6 false negative dan tidak menghasilkan false positive; Decision Tree menghasilkan 1 false negative dan 1 false positive.

Perbedaan belum signifikan pada uji berpasangan. Nilai exact McNemar adalah `p = 0,7266` untuk E3 dan `p = 0,2891` untuk E4. Karena itu, hasil mendukung kecenderungan Decision Tree yang lebih baik pada dataset ini, bukan klaim superioritas umum.

E1 menghasilkan akurasi 100% untuk kedua metode. Hasil tersebut hanya berlaku pada 20 invoice uji dan tidak boleh dijadikan kesimpulan tunggal.

## 6. Pola Kesalahan

Enam false negative Rule-Based pada evaluasi seluruh data berasal dari invoice `Urgent` yang masuk aturan default. Semuanya berkaitan dengan jadwal penerimaan terbatas dan jarak hari penerimaan berikutnya 2-5 hari. Pola ini menunjukkan bahwa ambang Rule-Based lebih konservatif daripada keputusan pada label sumber.

Model Decision Tree interpretatif yang dilatih pada seluruh data memiliki kedalaman 2 dan 4 daun. Kontribusi impurity tertinggi berasal dari `limited_receive_schedule_flag` (56,96%), `days_to_cutoff_feature` (39,78%), dan `cutoff_value_feature` (3,26%). Nilai ini bersifat deskriptif, bukan bukti sebab-akibat.

## 7. Kesimpulan Sementara

Decision Tree lebih konsisten mendeteksi invoice `Urgent`, sedangkan Rule-Based tidak menghasilkan false positive pada evaluasi penuh. Kesimpulan akhir harus tetap dibatasi pada 99 invoice unik, satu konteks perusahaan, dan bukti asal label yang tersedia.

Hasil lengkap tersedia di folder `comparative_experiment`. Eksperimen dapat dijalankan ulang melalui `run_comparative_experiment.py`.
