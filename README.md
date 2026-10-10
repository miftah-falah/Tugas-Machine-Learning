# Klasifikasi Dampak Media Sosial Menggunakan Decision Tree dan Random Forest

Proyek ini merupakan Laporan Praktikum Machine Learning (Pertemuan 3) pada Program Studi Teknik Informatika, Universitas Pamulang. 

Proyek ini bertujuan untuk mengklasifikasikan dampak penggunaan media sosial terhadap mahasiswa (*Beneficial*, *Neutral*, atau *Negative*) berdasarkan indikator psikologis, durasi penggunaan, dan performa akademik menggunakan algoritma **Decision Tree** dan **Random Forest**.

---

## 📌 Anggota Penyusun & Identitas
* **Nama:** Miftakhul Fal’ah
* **NIM:** 241011400237
* **Kelas:** 05TPLP018
* **Dosen Pengampu:** Asep Erlan Maulana, S.Kom., M.Kom.
* **Instansi:** Universitas Pamulang (UNPAM)

---

## 📊 Ringkasan Hasil Model

| Algoritma | Akurasi | Weighted F1-Score | Precision (Negative) | Recall (Negative) |
| :--- | :---: | :---: | :---: | :---: |
| **Decision Tree** | 96.44% | 0.96 | 0.83 | 0.91 |
| **Random Forest** | **98.22%** | **0.98** | **0.94** | **0.91** |

### 💡 Temuan Utama:
1. **Random Forest** memberikan performa keseluruhan yang lebih tinggi dan stabil dalam menekan kesalahan prediksi (*False Positives*) pada kelas minoritas (*Negative*).
2. Fitur paling dominan yang memengaruhi dampak media sosial meliputi:
   * **Perceived Stress Score** (Skor Tingkat Stres)
   * **Mental Health Index** (Indeks Kesehatan Mental)
   * **Daily Usage Hours** (Durasi Penggunaan Harian)
   * **Academic Performance GPA** (IPK Akademis)

---

## 📁 Struktur Repository

```text
.
├── main.ipynb                           # Notebook Jupyter berisi alur pipeline & eksperimen
├── Social_media_impact_on_life.csv      # Dataset input
├── LAPORAN PRAKTIKUM MACHINE LEARNING.docx  # Dokumen laporan resmi
└── README.md                            # Dokumentasi repository
