import streamlit as st
import requests

# Konfigurasi halaman web
st.set_page_config(page_title="Prediksi Dampak Media Sosial", page_icon="📱", layout="wide")

st.title("📱 Prediksi Dampak Media Sosial")
st.write("Masukkan data kebiasaan dan keseharian di bawah ini untuk melihat prediksi dampaknya.")

# Membuat form input untuk pengguna dengan layout 3 kolom agar rapi
with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Profil & Demografi")
        age = st.number_input("Umur", min_value=10, max_value=100, value=20)
        gender = st.selectbox("Jenis Kelamin", ['Female', 'Male', 'Non-Binary', 'Prefer not to say'])
        academic = st.selectbox("Tingkat Pendidikan", ['Undergraduate', 'High School', 'Postgraduate'])
        gpa = st.number_input("IPK / Nilai Akademik (GPA)", min_value=0.0, max_value=4.0, value=3.0, step=0.1)
        
    with col2:
        st.subheader("Kebiasaan Digital")
        platform = st.selectbox("Platform Utama", ['Snapchat', 'Instagram', 'TikTok', 'YouTube', 'LinkedIn', 'Reddit', 'X (Twitter)'])
        device = st.selectbox("Perangkat Utama", ['Smartphone', 'Tablet', 'Laptop/PC'])
        daily_hours = st.slider("Durasi Penggunaan Harian (Jam)", min_value=0.0, max_value=24.0, value=3.0, step=0.5)
        weekend_hours = st.slider("Tambahan Waktu di Akhir Pekan (Jam)", min_value=0.0, max_value=24.0, value=1.0, step=0.5)
        late_night = st.checkbox("Sering Menggunakan di Larut Malam?")
        
    with col3:
        st.subheader("Kesehatan & Psikologi")
        sleep_hours = st.slider("Durasi Tidur (Jam)", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
        sleep_quality = st.slider("Skor Kualitas Tidur (1-10)", min_value=1, max_value=10, value=5)
        stress_score = st.slider("Skor Stres (0-40)", min_value=0.0, max_value=40.0, value=20.0, step=1.0)
        mental_health = st.slider("Indeks Kesehatan Mental (0-100)", min_value=0, max_value=100, value=70)
        comparison = st.selectbox("Seberapa Sering Membandingkan Diri Sosial?", ['Always', 'Sometimes', 'Frequently', 'Never', 'Rarely'])
    
    # Tombol submit
    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button("Analisis Prediksi Dampak", use_container_width=True)

# Logika ketika tombol ditekan
if submit_button:
    # Menyiapkan data untuk dikirim ke FastAPI sesuai dengan parameter di app.py
    data = {
        "Age": age,
        "Gender": gender,
        "Academic_Level": academic,
        "Primary_Platform": platform,
        "Daily_Usage_Hours": daily_hours,
        "Weekend_Extra_Hours": weekend_hours,
        "Device_Type": device,
        "Sleep_Duration_Hours": sleep_hours,
        "Sleep_Quality_Score": sleep_quality,
        "Late_Night_Usage": late_night,
        "Social_Comparison_Frequency": comparison,
        "Perceived_Stress_Score": stress_score,
        "Mental_Health_Index": mental_health,
        "Academic_Performance_GPA": gpa
    }
    
    with st.spinner("Menghitung prediksi..."):
        try:
            # Mengirim request ke API FastAPI
            response = requests.post("http://127.0.0.1:8000/predict", json=data)
            
            if response.status_code == 200:
                result = response.json()
                prediksi = result["prediction"]
                
                st.success("Analisis Selesai!")
                
                # Memberikan warna berbeda berdasarkan hasil prediksi
                if prediksi == 'Beneficial':
                    st.info(f"**🌟 Prediksi Dampak: {prediksi} (Bermanfaat)**")
                elif prediksi == 'Negative':
                    st.error(f"**⚠️ Prediksi Dampak: {prediksi} (Negatif)**")
                else:
                    st.warning(f"**⚖️ Prediksi Dampak: {prediksi} (Netral)**")
                    
            else:
                st.error(f"Gagal memproses prediksi. Status code: {response.status_code}")
                st.write(response.text) # Membantu melihat detail pesan error dari backend
                
        except requests.exceptions.ConnectionError:
            st.error("Gagal terhubung ke server API. Pastikan uvicorn app:app --reload sedang berjalan!")