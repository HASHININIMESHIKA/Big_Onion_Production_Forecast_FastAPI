from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load the saved model, scaler, and columns used during training
model = joblib.load("Random_Forest.pkl")
scaler = joblib.load("scaler.pkl")
train_columns = joblib.load("train_columns.pkl")

# Create the FastAPI app
app = FastAPI()

# Define the input data model
class OnionProductionInput(BaseModel):
    Extent: float
    Air_Temp_Mean: float
    Relative_Humidity_D: float
    Relative_Humidity_N: float
    Rainfall: float
    Area: str
    Season: str

# Create an endpoint for onion production prediction
@app.post("/predict_onion_production/")
def predict_onion_production(data: OnionProductionInput):
    try:
        # Convert the input into a dictionary and then into a DataFrame
        input_data = data.dict()
        input_df = pd.DataFrame([input_data])

        # One-hot encode categorical features (Area and Season)
        input_df_encoded = pd.get_dummies(input_df, columns=['Area', 'Season'], drop_first=False)

        # Ensure all columns used during training are present in the input data
        for col in train_columns:
            if col not in input_df_encoded.columns:
                input_df_encoded[col] = 0  # Add missing columns with default value 0

        # Reorder columns to match the training data
        input_df_encoded = input_df_encoded[train_columns]

        # Scale the input data using the saved scaler
        input_scaled = scaler.transform(input_df_encoded)

        # Predict the onion production using the loaded model
        predicted_production = model.predict(input_scaled)

        # # Return the prediction
        # return {"predicted_onion_production": f"{predicted_production[0]:,.2f} metric tons"}

         # Return the prediction along with the corresponding area
        return {
            "area": data.Area,
            "predicted_onion_production": f"{predicted_production[0]:,.2f} metric tons"
        }
    except Exception as e:
        return {"error": str(e)}

# Add a root endpoint for GET requests
@app.get("/")
def read_root():
    return {"message": "Welcome to the Big Onion Production Prediction API. Use the /predict_onion_production/ endpoint for predictions."}