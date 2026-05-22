"""
Phishing URL Detection Model
"""
import joblib
import os
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "cyberfraud_system/ml/phishing/phishing_model.pkl"


def train_phishing_model(data_path):
    """
    Train a phishing URL detection model.
    
    Args:
        data_path: Path to the training dataset (CSV file).
    
    Returns:
        str: Path to the saved model.
    """
    data = pd.read_csv(data_path)
    X = data['url']
    y = data['label']

    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)

    model = RandomForestClassifier()
    model.fit(X_vectorized, y)

    joblib.dump((model, vectorizer), MODEL_PATH)
    print(f"[ML] Phishing model trained and saved at {MODEL_PATH}")
    return MODEL_PATH


def predict_phishing_url(url):
    """
    Predict if a URL is phishing or safe.
    
    Args:
        url: The URL to classify.
    
    Returns:
        tuple: (prediction, confidence, risk_level)
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Phishing model not found. Train the model first.")

    model, vectorizer = joblib.load(MODEL_PATH)
    # Validate URL
    if not isinstance(url, str) or not re.match(r'^(http|https)://', url):
        raise ValueError("Invalid URL format. Please provide a valid URL.")
    X_vectorized = vectorizer.transform([url])
    prediction = model.predict(X_vectorized)[0]
    confidence = max(model.predict_proba(X_vectorized)[0])

    # Calculate risk level
    risk_level = "HIGH" if confidence > 0.8 else "MEDIUM" if confidence > 0.5 else "LOW"

    return prediction, confidence, risk_level