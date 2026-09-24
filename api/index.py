from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
# Enable CORS for all domains on all routes
CORS(app)

# The original training data
data = [
    {"age": 30, "charge": 50, "churn": 0},
    {"age": 25, "charge": 60, "churn": 1},
    {"age": 35, "charge": 80, "churn": 0},
    {"age": 20, "charge": 40, "churn": 1},
    {"age": 40, "charge": 100, "churn": 0},
    {"age": 55, "charge": 120, "churn": 1},
    {"age": 32, "charge": 70, "churn": 0},
    {"age": 28, "charge": 55, "churn": 1}
]

@app.route('/api/index', methods=['POST', 'GET'])
def predict():
    try:
        req_data = request.json or {}
        user_age = float(req_data.get("age", 0))
        user_charge = float(req_data.get("monthly_charges", 0))

        # Pure Python 1-Nearest Neighbor (matches the dataset perfectly)
        best_dist = float('inf')
        prediction = 0
        
        for row in data:
            dist = math.sqrt((user_age - row["age"])**2 + (user_charge - row["charge"])**2)
            if dist < best_dist:
                best_dist = dist
                prediction = row["churn"]

        message = "The customer is likely to stay." if prediction == 0 else "The customer is at risk of churning."
        
        return jsonify({
            "prediction": prediction,
            "message": message
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Backend is running!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
