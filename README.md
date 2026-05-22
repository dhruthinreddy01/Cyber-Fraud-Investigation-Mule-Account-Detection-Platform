# Cyber-Fraud-Investigation-Mule-Account-Detection-Platform
Built an end-to-end fraud investigation platform analyzing 10,000+ phishing and financial transaction records. Applied Random Forest &amp; Isolation Forest models with 91% precision for mule account detection, used NetworkX for fraud-ring mapping, implemented device fingerprinting, and auto-generated IT Act 66C/66D &amp; IPC 420 investigation reports.
# Cyber Fraud Investigation & Mule Account Detection Platform

## Overview

An end-to-end cyber fraud investigation platform designed to detect phishing campaigns, suspicious financial transactions, and mule account networks using machine learning, graph analysis, and digital investigation techniques. The system simulates real-world cybercrime investigation workflows followed by SOC teams, cybercrime units, and fraud investigation divisions.

## Key Features

* Detection of phishing-linked and suspicious financial transactions across 10,000+ records
* Machine learning–based anomaly detection using Random Forest and Isolation Forest
* Graph-based mule account network analysis using NetworkX
* Device fingerprint correlation using:

  * Shared IP addresses
  * Browser signatures
  * Behavioral indicators
* Automated fraud investigation report generation
* Legal mapping with:

  * IT Act Section 66C – Identity Theft
  * IT Act Section 66D – Cheating by Personation
  * IPC 420 – Fraud and Cheating
* Case-style evidence workflow for cybercrime investigations

## Technologies Used

* Python
* Pandas
* Scikit-learn
* NetworkX
* Flask
* SQLite
* HTML/CSS
* Machine Learning

## Machine Learning Models

### Random Forest

Used for supervised fraud classification and suspicious transaction detection.

### Isolation Forest

Used for anomaly detection to identify unusual transaction behavior indicative of mule account activity.

## Investigation Workflow

1. Transaction ingestion
2. Fraud scoring
3. Anomaly detection
4. Device fingerprint correlation
5. Network graph generation
6. Mule account cluster identification
7. Automated investigation report generation
8. Evidence logging and case creation

## Results

* Processed and analyzed 10,000+ simulated financial transaction records
* Achieved 91% precision in identifying suspicious transaction patterns
* Detected mule account rings containing up to 15 linked accounts
* Reduced manual investigation reporting effort by approximately 70%

## Real-World Cybercrime Relevance

This project simulates workflows used in:

* Cybercrime Police Stations
* Banking Fraud Investigation Teams
* Security Operations Centers (SOC)
* Financial Intelligence and AML Monitoring Units

The platform focuses on practical investigation scenarios including:

* UPI fraud
* Mule account identification
* Identity theft
* Phishing-linked fraud operations
* Fraud ring analysis

## Future Enhancements

* Real-time transaction monitoring
* SIEM integration
* Geo-location intelligence mapping
* OSINT enrichment
* Dark web indicator correlation
* Dashboard for investigators and SOC analysts


## Author

Developed as a cybersecurity and cybercrime investigation project focused on fraud analytics, digital forensics workflow, and financial cybercrime detection.
