"""
Training Script for Phishing URL Detection Model
"""
from phishing_model import train_phishing_model

if __name__ == "__main__":
    DATA_PATH = "cyberfraud_system/ml/phishing/phishing_dataset.csv"
    train_phishing_model(DATA_PATH)