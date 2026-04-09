import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Training data representing smaller quantum lab hardware
data = pd.DataFrame({
    "temp": [
        0.02,0.03,0.04,0.05,0.06,
        0.07,0.08,0.09,0.10,0.12,
        0.14,0.15
    ],

    "freq": [
        6e9,5.8e9,5.5e9,5.2e9,5e9,
        4.8e9,4.5e9,4.2e9,4e9,3.8e9,
        3.5e9,3.2e9
    ],

    "optimal_k": [
        0.28,0.32,0.36,0.40,0.44,
        0.50,0.56,0.62,0.68,0.74,
        0.82,0.90
    ]
})

# Features
X = data[["temp","freq"]]

# Target
y = data["optimal_k"]

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# Save model
joblib.dump(model, "ai_model.pkl")

print("AI model trained for small-lab quantum systems.")