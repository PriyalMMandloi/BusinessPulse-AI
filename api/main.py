# ============================================================
# BusinessPulse-AI
# FastAPI Backend
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

# ============================================================
# Create FastAPI Application
# ============================================================

app = FastAPI(
    title="BusinessPulse-AI API",
    description="Customer Churn Prediction using Machine Learning",
    version="1.0.0"
)

# ============================================================
# Load Machine Learning Artifacts
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "final_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
ENCODER_PATH = BASE_DIR / "models" / "feature_encoder.pkl"

final_model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_encoder = joblib.load(ENCODER_PATH)

print("=" * 60)
print("Machine Learning Artifacts Loaded Successfully")
print("=" * 60)

# ============================================================
# Customer Input Schema
# ============================================================

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# ============================================================
# Home Endpoint
# ============================================================

@app.get("/")
def home():
    return {
        "Project": "BusinessPulse-AI",
        "Status": "API Running Successfully",
        "Version": "1.0.0"
    }

# ============================================================
# Health Check Endpoint
# ============================================================

@app.get("/health")
def health():
    return {
        "Status": "Healthy"
    }
# ============================================================
# Prediction Endpoint
# ============================================================

@app.post("/predict")
def predict(customer: CustomerData):

    # Convert request to DataFrame
    input_df = pd.DataFrame([customer.model_dump()])

    # Encode categorical features
    input_encoded = feature_encoder.transform(input_df)

    # Scale features
    input_scaled = scaler.transform(input_encoded)

    # Predict
    prediction = final_model.predict(input_scaled)[0]

    # Predict probability
    probability = final_model.predict_proba(input_scaled)[0][1]

    prediction_text = "Yes" if prediction == 1 else "No"

    return {
        "Prediction": prediction_text,
        "Churn Probability": round(float(probability), 4)
    }