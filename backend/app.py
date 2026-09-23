from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
# Enable CORS for all domains on all routes
CORS(app)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

# We will load the model lazily or at startup if it exists
model = None
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    print("Warning: model.pkl not found. Please run train_model.py first.")

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        if os.path.exists(model_path):
            model = joblib.load(model_path)
        else:
            return jsonify({"error": "Model not trained yet."}), 500

    try:
        data = request.json
        age = float(data.get("age", 0))
        monthly_charges = float(data.get("monthly_charges", 0))

        # The model expects a 2D array
        user_input = np.array([[age, monthly_charges]])
        prediction = model.predict(user_input)

        result = int(prediction[0])
        message = "The customer is likely to stay." if result == 0 else "The customer is at risk of churning."
        
        return jsonify({
            "prediction": result,
            "message": message
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Backend is running!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
