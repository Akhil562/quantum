import joblib
import pandas as pd

# Load trained model
model = joblib.load("ai_model.pkl")

def predict_k(temp, freq):
    """
    Predict optimal feedback strength k using AI model
    """

    # Use SAME column names used during training
    X = pd.DataFrame({
        "temp": [temp],
        "freq": [freq]
    })

    k = model.predict(X)[0]

    return float(k)