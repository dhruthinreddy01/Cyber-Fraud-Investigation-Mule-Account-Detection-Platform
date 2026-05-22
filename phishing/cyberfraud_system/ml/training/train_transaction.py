"""
Training Script for Transaction Fraud Detection Model
"""
from transaction_model import train_transaction_model

if __name__ == "__main__":
    DATA_PATH = "cyberfraud_system/ml/transaction_fraud/transaction_dataset.csv"
    train_transaction_model(DATA_PATH)