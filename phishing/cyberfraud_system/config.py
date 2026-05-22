import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    UPLOAD_FOLDER = 'cyberfraud_system/uploads'
    DATABASE_PATH = 'cyberfraud_system/database/cyberfraud.db'
    EVIDENCE_FOLDER = 'cyberfraud_system/evidence/cases'
    REPORTS_FOLDER = 'cyberfraud_system/reports'