from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import logging

# Konfigurasi Logging untuk Monitoring
logging.basicConfig(filename='model_monitoring.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

app = FastAPI(title="Social Media Impact Prediction API")

# Memuat model yang telah disimpan
model = joblib.load('social_media_impact_model.pkl')

# Mendefinisikan format input menggunakan Pydantic (Sesuai dengan dataset asli)
class UserInput(BaseModel):
    Age: int
    Gender: str
    Academic_Level: str
    Primary_Platform: str
    Daily_Usage_Hours: float
    Weekend_Extra_Hours: float
    Device_Type: str
    Sleep_Duration_Hours: float
    Sleep_Quality_Score: int
    Late_Night_Usage: bool
    Social_Comparison_Frequency: str
    Perceived_Stress_Score: float
    Mental_Health_Index: int
    Academic_Performance_GPA: float

@app.get("/")
def read_root():
    return {"message": "Server berjalan! Silakan gunakan Streamlit atau tambahkan /docs di URL untuk menguji model."}

@app.post("/predict")
def predict_impact(data: UserInput):
    # Mengubah input JSON menjadi DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Melakukan prediksi
    prediction = model.predict(input_data)
    
    # Logging untuk Monitoring (Mencatat input dan hasil prediksi)
    logging.info(f"Input: {data.dict()} | Prediction: {prediction[0]}")
    
    return {"prediction": prediction[0]}