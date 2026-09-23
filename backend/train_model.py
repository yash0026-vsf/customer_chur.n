import numpy as np
import pandas as pd
from sklearn.svm import SVC
import joblib
import os

# Create a small dataset (from the original notebook)
data = {
    "Age": [30, 25, 35, 20, 40, 55, 32, 28],
    "MonthlyCharges": [50, 60, 80, 40, 100, 120, 70, 55],
    "Churn": [0, 1, 0, 1, 0, 1, 0, 1]  # 0 = stay, 1 = churn
}
df = pd.DataFrame(data)

X = df[["Age", "MonthlyCharges"]]
y = df["Churn"]

# Train the model
svc_model = SVC(kernel="linear", C=1.0)
svc_model.fit(X, y)

# Save the trained model to a file
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
joblib.dump(svc_model, model_path)
print(f"Model trained and saved to {model_path}")
