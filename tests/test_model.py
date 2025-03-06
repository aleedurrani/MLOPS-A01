# File: tests/test_model.py
from app.model import train_model
import os


def test_model_training():
    train_model()
    assert os.path.exists("model/premium_subscription_model.pkl")
# Add a newline here