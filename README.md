# Onion Production Forecast API

This project provides a **FastAPI-based REST API** for predicting **Big Onion production** in Sri Lanka. The API uses a **pre-trained Random Forest model** to make predictions based on input features such as area, season, weather conditions, and more.

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
  - [Deployment](#deployment)
- [Usage](#usage)
  - [Example Request](#example-request)
  - [Example Response](#example-response)
- [Technologies Used](#technologies-used)
- [License](#license)

---

## 📖 Project Overview
The goal of this project is to predict **Big Onion production** in Sri Lanka based on historical data. The API takes input features such as:

- **Extent**: Cultivated area (in hectares).
- **Air Temp (Mean)**: Average air temperature.
- **Relative Humidity (Day/Night)**: Humidity levels during the day and night.
- **Rainfall**: Amount of rainfall.
- **Area**: Cultivation area (e.g., Anuradhapura, Kurunegala).
- **Season**: Cultivation season (e.g., Yala, Maha).

The API returns the **predicted onion production** in **metric tons**.

---

## 🚀 Features
✅ **Machine Learning Model**: Uses a pre-trained **Random Forest** model for accurate predictions.  
✅ **FastAPI**: Provides a **fast and scalable** REST API.  
✅ **Deployment**: Hosted on **Render** for public access.  
✅ **Input Validation**: Uses **Pydantic** for robust input validation.  
✅ **Scalability**: Designed to handle multiple requests efficiently.  

---

## 🌐 API Endpoints

### 1️⃣ Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Welcome message and instructions for using the API.
- **Response**:
```json
{
  "message": "Welcome to the Big Onion Production Prediction API. Use the /predict_onion_production/ endpoint for predictions."
}
```

### 2️⃣ Prediction Endpoint
- **URL**: `/predict_onion_production/`
- **Method**: `POST`
- **Description**: Predicts onion production based on input features.
- **Request Body**:
```json
{
  "Extent": 1000,
  "Air_Temp_Mean": 25.5,
  "Relative_Humidity_D": 70.0,
  "Relative_Humidity_N": 80.0,
  "Rainfall": 150.0,
  "Area": "Ampara",
  "Season": "Yala"
}
```
- **Response**:
```json
{
  "area": "Ampara",
  "predicted_onion_production": "11,239.05 metric tons"
}
```

---

## ⚙️ Setup Instructions

### 🔹 Prerequisites
Ensure you have the following installed:
- **Python 3.8 or higher**
- **pip** (Python package manager)

### 🔹 Local Setup
1. **Clone the Repository**:
```bash
git clone https://github.com/your-username/OnionProductionForecastFastAPI.git
cd OnionProductionForecastFastAPI
```
2. **Create a Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```
3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
4. **Run the Application**:
```bash
uvicorn main:app 
```
5. **Access the API**:
- Open your browser or API client (e.g., Postman) and navigate to:
```
http://127.0.0.1:8000/
```

---

## ☁️ Deployment
The API is deployed on **Render** and can be accessed at:
```
[[https://onion-production-forecast-api.onrender.com](https://big-onion-production-forecast-fastapi-1.onrender.com)](https://big-onion-production-forecast-fastapi-1.onrender.com
)
```

### 🔹 Deployment Steps:
1. Push your code to a **GitHub repository**.
2. Create a new **Web Service** on **Render**.
3. Connect your **GitHub repository**.
4. Specify the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Deploy the application.

---

## 📌 Usage
### 🔹 Example Request
```bash
curl -X POST "https://onion-production-forecast-api.onrender.com/predict_onion_production/" \
-H "Content-Type: application/json" \
-d '{
  "Extent": 1000,
  "Air_Temp_Mean": 25.5,
  "Relative_Humidity_D": 70.0,
  "Relative_Humidity_N": 80.0,
  "Rainfall": 150.0,
  "Area": "Ampara",
  "Season": "Yala"
}'
```

### 🔹 Example Response
```json
{
  "area": "Ampara",
  "predicted_onion_production": "11,239.05 metric tons"
}
```

---

## 🛠 Technologies Used
- **Python**: Primary programming language.
- **FastAPI**: Web framework for building the API.
- **Random Forest**: Machine learning model for predictions.
- **Pandas**: Data manipulation and preprocessing.
- **Scikit-learn**: Machine learning tools.
- **Render**: Cloud platform for deployment.

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
