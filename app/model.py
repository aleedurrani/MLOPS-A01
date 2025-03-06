# File: app/model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib


def train_model():
    # Load data
    df = pd.read_csv("data/premium_subscription_data.csv")

    # Features and target
    X = df[["age", "weekly_usage_hrs", "avg_session_duration"]]
    y = df["premium_subscribed"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, "model/premium_subscription_model.pkl")
    print("Model trained and saved!")


if __name__ == "__main__":
    train_model()
# Add a newline here