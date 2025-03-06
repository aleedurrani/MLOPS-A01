# File: app/api.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd


app = Flask(__name__)

# Load trained model
model = joblib.load("model/premium_subscription_model.pkl")


@app.route("/")
def home():
    return "Premium Subscription Prediction API"


# File: app/api.py
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Ensure feature order matches training data
    features = pd.DataFrame([data], columns=["age", "weekly_usage_hrs", "avg_session_duration"])
    prediction = model.predict(features)
    return jsonify({"prediction": int(prediction[0])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Add a newline here
