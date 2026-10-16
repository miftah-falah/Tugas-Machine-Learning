# 📱 Social Media Impact Prediction

Proyek ini adalah sistem *Machine Learning* *End-to-End* untuk memprediksi dampak penggunaan media sosial (Netral, Bermanfaat, atau Negatif) terhadap kehidupan seseorang berdasarkan demografi, kebiasaan digital, dan kondisi psikologis (kesehatan mental & kualitas tidur).

> **💡 Catatan Pengembangan (Upgrade dari Materi Dasar):**
> Pada materi perkuliahan, *deployment* diajarkan menggunakan **Flask**. Namun, dalam proyek praktikum ini, *backend* telah ditingkatkan (*upgraded*) menggunakan **FastAPI**. Pemilihan FastAPI dilakukan karena framework ini menawarkan performa yang lebih cepat, validasi data otomatis menggunakan Pydantic, serta menyediakan dokumentasi UI interaktif bawaan (Swagger UI) yang sangat memudahkan pengujian model API secara langsung.

## 🚀 Fitur Proyek
Proyek ini mencakup seluruh siklus *machine learning*, mulai dari pemrosesan data hingga antarmuka pengguna:
1. **Model Training:** Eksplorasi data, prapemrosesan, dan pelatihan model menggunakan *Random Forest Classifier*.
2. **Backend API (FastAPI):** Melayani *request* prediksi secara *real-time* dengan validasi input yang ketat dan dokumentasi API otomatis.
3. **Frontend (Web UI):** Antarmuka web interaktif menggunakan **Streamlit** untuk memudahkan pengguna memasukkan data tanpa perlu menyusun file JSON manual.
4. **Monitoring:** Pencatatan (*logging*) otomatis ke dalam file `.log` untuk setiap aktivitas prediksi guna keperluan evaluasi dan deteksi *data drift* ke depannya.

## 📁 Struktur File
* `Social_media_impact_on_life.csv` : Dataset mentah yang digunakan untuk melatih model.
* `main.ipynb` : Jupyter Notebook berisi analisis data (EDA), pembuatan *pipeline preprocessing*, pelatihan model *Random Forest*, dan ekspor model.
* `social_media_impact_model.pkl` : File model *machine learning* yang telah dilatih dan disimpan (menggunakan `joblib`).
* `app.py` : Skrip *backend* FastAPI untuk menjalankan server API prediksi.
* `web.py` : Skrip *frontend* Streamlit untuk menampilkan antarmuka web interaktif.
* `model_monitoring.log` : File log yang otomatis mencatat riwayat input pengguna dan hasil prediksi API.

## 🛠️ Teknologi yang Digunakan
* **Bahasa:** Python 3.14
* **Data Science & ML:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib, Joblib
* **Deployment Backend:** FastAPI, Uvicorn, Pydantic
* **Deployment Frontend:** Streamlit, Requests

## 💻 Cara Menjalankan Aplikasi Secara Lokal (Localhost)

### 1. Instalasi Library (Prasyarat)
Buka terminal/command prompt dan instal pustaka yang dibutuhkan:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib fastapi uvicorn pydantic streamlit requests