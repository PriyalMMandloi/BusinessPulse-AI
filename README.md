# 📊 BusinessPulse-AI

> End-to-End Customer Churn Prediction Platform built with Machine Learning, FastAPI, and Streamlit.

---

## 🚀 Project Overview

BusinessPulse-AI is an end-to-end Machine Learning application designed to predict customer churn using customer demographics, subscribed services, billing information, and contract details.

The project integrates a Machine Learning model, a FastAPI backend, and an interactive Streamlit dashboard to help businesses identify customers at risk of churn and make data-driven retention decisions.

This project demonstrates the complete Machine Learning workflow, from data preprocessing and model training to API development, dashboard creation, and deployment-ready architecture.

---

# ✨ Features

- 📊 Customer Churn Prediction
- 🤖 Machine Learning Model (Random Forest)
- ⚡ FastAPI REST API
- 🎨 Interactive Streamlit Dashboard
- 📈 Churn Probability Visualization
- 🚦 Risk Level Detection
- 💡 Business Recommendations
- 📁 Prediction History Storage
- 📦 Modular Project Architecture
- 🧩 Responsive User Interface
- 🌙 Dark & Light Theme Support

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|-----------------------------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-Learn | Machine Learning |
| Random Forest | Classification Model |
| FastAPI | Backend API |
| Streamlit | Interactive Dashboard |
| Joblib | Model Serialization |
| Requests | API Communication |
| Git & GitHub | Version Control |

---

# 🏗 Project Architecture

```text
                    User
                      │
                      ▼
          Streamlit Dashboard
                      │
                      ▼
             FastAPI Backend
                      │
                      ▼
        Machine Learning Model
                      │
                      ▼
        Churn Prediction Result
                      │
                      ▼
     Business Recommendation
```

---

# 📂 Project Structure

```text
BusinessPulse-AI
│
├── api/
│   └── main.py
│
├── dashboard/
│   ├── app.py
│   ├── api_utils.py
│   ├── config.py
│   ├── forms.py
│   ├── results_ui.py
│   └── styles.py
│
├── data/
│   ├── customer_churn.csv
│   └── customer_churn_clean.csv
│
├── database/
│   └── prediction_history.csv
│
├── models/
│   ├── final_model.pkl
│   ├── scaler.pkl
│   └── feature_encoder.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Model_Training.ipynb
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📸 Project Screenshots

## 🏠 Dashboard Home

![Dashboard](screenshots/dashboard_home.png)

---

## 📝 Customer Input Form

![Customer Input](screenshots/customer_input_form.png)

---

## 🟢 Low Risk Prediction

![Low Risk](screenshots/prediction_result_low_risk.png)

---

## 🔴 High Risk Prediction

![High Risk](screenshots/prediction_result_high_risk.png)

---

## 📡 FastAPI Swagger Documentation

![Swagger API](screenshots/swagger_api.png)

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/PriyalMMandloi/BusinessPulse-AI.git
```

```bash
cd BusinessPulse-AI
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Start FastAPI Server

```bash
cd api
uvicorn main:app --reload
```

API:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Start Streamlit Dashboard

Open a new terminal and run:

```bash
streamlit run dashboard/app.py
```

Dashboard:

```
http://localhost:8501
```

---

# 📊 Machine Learning Pipeline

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Encoding
- Feature Scaling
- Model Training
- Model Evaluation
- Model Serialization
- FastAPI Integration
- Streamlit Dashboard Development

---

# 📈 Model Information

| Model | Accuracy |
|--------|----------|
| Random Forest Classifier | **95%** |

### Input Features

- Customer Demographics
- Internet Services
- Contract Details
- Billing Information
- Payment Method
- Tenure
- Monthly Charges
- Total Charges

### Output

- Customer Churn Prediction
- Churn Probability
- Risk Level
- Business Recommendation

---

# 📡 API Endpoint

## POST `/predict`

### Sample Response

```json
{
  "Prediction": "Yes",
  "Churn Probability": 0.8946
}
```

---

# 💡 Business Recommendations

BusinessPulse-AI automatically provides business recommendations based on the predicted churn probability.

## 🔴 High Risk

- Offer customer retention discounts
- Contact the customer proactively
- Recommend a long-term contract
- Provide personalized support

## 🟢 Low Risk

- Customer appears loyal
- Continue regular engagement
- No immediate action required

---

# 📌 Future Improvements

- 🔐 User Authentication
- ☁️ Cloud Deployment (AWS / Azure)
- 🗄 MySQL / PostgreSQL Integration
- 📊 Dashboard Analytics
- 📧 Email Notifications
- 👥 Customer Segmentation
- 🧠 Explainable AI (SHAP)
- 🤖 Docker Containerization

---

# 👩‍💻 Developer

**Priyal Mangesh Mandloi**

Data Science Undergraduate passionate about Machine Learning, Artificial Intelligence, Data Analytics, and Backend Development.

### Skills

- Python
- Machine Learning
- FastAPI
- Streamlit
- SQL
- Data Analytics
- Git & GitHub

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps support the project and encourages future development.