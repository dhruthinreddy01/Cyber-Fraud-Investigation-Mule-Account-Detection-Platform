import sqlite3

def init_db(db_path="database/cyberfraud.db"):
    """
    Initialize the SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create cases table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT UNIQUE,
            case_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create evidence table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evidence (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT,
            file_name TEXT,
            sha256_hash TEXT,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

def log_case(case_id, case_type, db_path="database/cyberfraud.db"):
    """
    Log a new case in the database.

    Args:
        case_id (str): Unique identifier for the case.
        case_type (str): Type of the case.
        db_path (str): Path to the SQLite database file.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cases (case_id, case_type) VALUES (?, ?)', (case_id, case_type))
    conn.commit()
    conn.close()

def log_evidence(case_id, file_name, hash_value, db_path="database/cyberfraud.db"):
    """
    Log evidence in the database.

    Args:
        case_id (str): Unique identifier for the case.
        file_name (str): Name of the evidence file.
        hash_value (str): SHA256 hash of the file.
        db_path (str): Path to the SQLite database file.
    """
    import sqlite3
    from datetime import datetime

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ensure evidence table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evidence (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT,
            file_name TEXT,
            sha256_hash TEXT,
            timestamp TEXT
        )
    ''')
    print("[DEBUG] Ensured evidence table exists.")

    # Insert evidence record
    cursor.execute(
        'INSERT INTO evidence (case_id, file_name, sha256_hash, timestamp) VALUES (?, ?, ?, ?)',
        (case_id, file_name, hash_value, datetime.now().isoformat())
    )
    print(f"[DEBUG] Logged evidence for case_id: {case_id}")

    conn.commit()
    conn.close()