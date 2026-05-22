"""
Transaction Fraud Detection Model
"""
import joblib
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "cyberfraud_system/ml/transaction_fraud/transaction_model.pkl"


def train_transaction_model(data_path):
    """
    Train a transaction fraud detection model.
    
    Args:
        data_path: Path to the training dataset (CSV file).
    
    Returns:
        str: Path to the saved model.
    """
    data = pd.read_csv(data_path)
    X = data.drop(columns=['label'])
    y = data['label']

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print(f"[ML] Transaction fraud model trained and saved at {MODEL_PATH}")
    return MODEL_PATH


def predict_transaction_fraud(transaction_data):
    """
    Predict if a transaction is fraudulent or legitimate.
    
    Args:
        transaction_data: Features of the transaction.
    
    Returns:
        tuple: (prediction, confidence, risk_level)
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Transaction fraud model not found. Train the model first.")

    model = joblib.load(MODEL_PATH)

    # Validate transaction data
    if not isinstance(transaction_data, list) or not all(isinstance(x, (int, float)) for x in transaction_data):
        raise ValueError("Invalid transaction data. Ensure all features are numeric and provided as a list.")

    prediction = model.predict([transaction_data])[0]
    confidence = max(model.predict_proba([transaction_data])[0])

    # Calculate risk level
    risk_level = "HIGH" if confidence > 0.8 else "MEDIUM" if confidence > 0.5 else "LOW"

    return prediction, confidence, risk_level