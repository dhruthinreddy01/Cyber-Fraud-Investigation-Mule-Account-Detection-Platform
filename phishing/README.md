# CyberFraud Investigation System

## Overview
The CyberFraud Investigation System is a SOC-grade platform designed for real-world cybercrime investigations. It supports phishing detection, APK analysis, transaction fraud detection, and evidence management, aligned with Indian cyber law.

## Features
- **End-to-End Investigation Workflow**: Input → Detection → Case Management → Evidence Collection → Legal Mapping → Report Generation → Dashboard Visualization.
- **Phishing Detection**: URL analysis with risk scoring.
- **APK Analysis**: Metadata extraction and malware detection.
- **Transaction Fraud Detection**: Graph-based mule detection and risk analysis.
- **Device/Identity Correlation**: Detect linked accounts based on shared devices or IPs.
- **Legal Mapping**: IT Act compliance for phishing, APK fraud, and transaction fraud.
- **PDF Reports**: FIR-style reports with IOCs and legal sections.
- **SOC Dashboard**: High-risk alerts, recent cases, and fraud type breakdown.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/cyberfraud-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cyberfraud-system
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   python -c "from backend.database import init_db; init_db()"
   ```
5. Start the application:
   ```bash
   python app.py
   ```

## Architecture
- **Backend**: Flask-based API for detection, case management, and evidence handling.
- **Frontend**: HTML templates with a dark SOC theme.
- **Database**: SQLite for case and evidence tracking.
- **Machine Learning**: Scikit-learn models for phishing and fraud detection.

## Investigation Workflow
1. Submit evidence (URL, APK, or transaction data).
2. System performs detection and generates risk scores.
3. Case is created with unique ID and evidence.json.
4. Legal mapping is applied and visible in the UI, PDF, and dashboard.
5. Generate PDF reports for court submission.

## How to Run
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Access the dashboard at:
   ```
   http://127.0.0.1:5000/dashboard
   ```

## Legal Compliance
- **Phishing**: IT Act 66D
- **Fake APK**: IT Act 66C + 66D
- **Transaction Fraud**: IT Act 43 + IPC 420

## Screenshots
![Dashboard](screenshots/dashboard.png)
![PDF Report](screenshots/pdf_report.png)

## Contributors
- Your Name
- Team Members

## License
MIT License