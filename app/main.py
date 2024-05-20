from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Define the request body model
class PredictionRequest(BaseModel):
    cpu_usage: float
    memory_usage: float
    network_traffic: float
    power_consumption: float
    num_executed_instructions: float
    execution_time: float

# Load the pre-trained Linear Regression model
try:
    model = joblib.load('lr_model.joblib')
except Exception as e:
    raise RuntimeError("Model loading failed. Ensure 'lr_model.joblib' is in the current directory.") from e

# Initialize the FastAPI app
app = FastAPI()

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        # Prepare the input data for prediction
        input_data = np.array([[request.cpu_usage, request.memory_usage, request.network_traffic,
                                request.power_consumption, request.num_executed_instructions, request.execution_time]])
        
        # Make the prediction using the loaded model
        prediction = model.predict(input_data)
        
        # Return the prediction result
        return {"energy_efficiency": prediction[0]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Energy Efficiency Prediction API"}
