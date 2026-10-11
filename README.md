# Analisis Dampak Media Sosial terhadap Kehidupan (Social Media Impact on Life - Machine Learning Project)

Repitori ini berisi proyek praktikum *Machine Learning* yang bertujuan untuk menganalisis dan memprediksi dampak keseluruhan penggunaan media sosial terhadap kehidupan seseorang (responden) berdasarkan berbagai fitur perilaku, demografi, dan kebiasaan digital.

---

## 📋 Daftar Isi
1. [Tentang Proyek](#tentang-proyek)
2. [Struktur Dataset](#struktur-dataset)
3. [Alur Kerja (Workflow)](#alur-kerja-workflow)
4. [Instalasi dan Kebutuhan Sistem](#instalasi-dan-kebutuhan-sistem)
5. [Cara Menjalankan Proyek](#cara-menjalankan-proyek)
6. [Hasil dan Evaluasi Model](#hasil-dan-evaluasi-model)
7. [Kontributor](#kontributor)

---

## 🎯 Tentang Proyek
Media sosial memiliki berbagai dampak positif dan negatif dalam kehidupan sehari-hari, mulai dari produktivitas, kesehatan mental, hingga interaksi sosial. Proyek ini menggunakan pendekatan *Supervised Learning* (Klasifikasi) dengan algoritma **Random Forest** untuk memprediksi tingkat dampak keseluruhan (`Overall_Impact`) dari media sosial terhadap individu berdasarkan pola penggunaan mereka.

---

## 📊 Struktur Dataset
Dataset yang digunakan dalam proyek ini adalah `Social_media_impact_on_life.csv` yang mencakup berbagai variabel, antara lain:
* **Fitur Demografi/Identitas**: ID Responden, dll.
* **Fitur Numerik**: Durasi waktu harian, frekuensi akses, usia, dll.
* **Fitur Kategorikal**: Jenis platform yang sering digunakan, kebiasaan, dan respons subjektif.
* **Variabel Target (`Overall_Impact`)**: Kategori dampak keseluruhan penggunaan media sosial.

---

## 🔄 Alur Kerja (Workflow)
Notebook ini dirancang secara sistematis melalui beberapa tahapan utama:
1. **Pemuatan Dataset & Eksplorasi Awal (EDA)**: Memuat data, memeriksa informasi dasar, dimensi, serta tipe data.
2. **Pengecekan Kualitas Data**: Menganalisis *missing values* (nilai kosong) dan baris data yang duplikat.
3. **Eksplorasi Statistik & Visualisasi**: 
   * Membuat *box plot* untuk mendeteksi *outliers* pada fitur numerik.
   * Visualisasi *countplot* untuk melihat distribusi kelas pada variabel target.
4. **Prapemrosesan Data (Preprocessing Pipeline)**:
   * Penanganan *missing value* (Imputasi median untuk numerik, modus untuk kategorikal).
   * Standarisasi fitur numerik menggunakan `StandardScaler`.
   * *One-Hot Encoding* untuk fitur kategorikal menggunakan `OneHotEncoder`.
5. **Pembagian Data (Data Splitting)**: Membagi dataset menjadi *training set* (80%) dan *test set* (20%) secara stratified.
6. **Pemodelan (Model Training)**: Melatih model klasifikasi menggunakan **Random Forest Classifier** yang diintegrasikan ke dalam *Scikit-Learn Pipeline*.
7. **Evaluasi Model**: Menguji performa model menggunakan metrik *Accuracy*, *Classification Report* (Precision, Recall, F1-Score), serta visualisasi *Confusion Matrix*.

---

## 🛠️ Instalasi dan Kebutuhan Sistem
Pastikan Anda telah menginstal Python (disarankan versi 3.8 ke atas) beserta pustaka-pustaka berikut:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## 🚀 Cara Menjalankan Proyek
1. Clone atau unduh repositori ini ke komputer lokal Anda:
   ```bash
   git clone https://github.com/miftah-falah/Tugas-Machine-Learning.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd repository-name
   ```
3. Pastikan file dataset `Social_media_impact_on_life.csv` berada di direktori yang sama dengan file notebook.
4. Buka Jupyter Notebook atau JupyterLab:
   ```bash
   jupyter notebook main.ipynb
   ```
5. Jalankan sel (*cells*) secara berurutan dari atas ke bawah.

---

## 📈 Hasil dan Evaluasi Model
* **Model yang Digunakan**: `RandomForestClassifier` (dengan *ensemble trees*).
* **Metrik Evaluasi**: 
  * *Accuracy Score*
  * *Precision*, *Recall*, dan *F1-Score* per kelas.
  * *Confusion Matrix* (divisualisasikan menggunakan *Seaborn Heatmap*).

---

## 👥 Kontributor
Proyek ini dikembangkan sebagai bagian dari materi praktikum *Machine Learning*. Silakan buat *pull request* atau laporkan *issue* jika Anda memiliki saran pengembangan.