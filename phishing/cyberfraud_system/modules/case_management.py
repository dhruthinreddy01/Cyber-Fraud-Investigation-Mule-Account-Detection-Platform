"""
Case Management Module
FIR-style case creation and tracking
"""
import os
import json
from datetime import datetime
from .forensic_evidence import create_evidence_json


def create_case_folder(base_path="evidence/cases"):
    """
    Create a FIR-style case folder with metadata.
    
    Returns:
        tuple: (case_id, case_path, timestamp)
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    case_id = f"CASE_{timestamp}"
    case_path = os.path.join(base_path, case_id)
    
    os.makedirs(case_path, exist_ok=True)
    
    # Create case metadata file
    metadata = {
        "case_id": case_id,
        "created_at": datetime.now().isoformat(),
        "status": "OPEN",
        "evidence_count": 0,
        "investigator": "SOC_ANALYST"
    }
    
    metadata_file = os.path.join(case_path, "case_metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=4)
    
    print(f"[CASE_MGMT] Case created: {case_id}")
    return case_id, case_path, timestamp


def update_case_metadata(case_path, **kwargs):
    """Update case metadata."""
    metadata_file = os.path.join(case_path, "case_metadata.json")
    
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        
        metadata.update(kwargs)
        
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=4)


def get_case_metadata(case_path):
    """Retrieve case metadata."""
    metadata_file = os.path.join(case_path, "case_metadata.json")
    
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as f:
            return json.load(f)
    return None


def collect_evidence(case_id, evidence_data, case_path):
    """
    Collect evidence and create evidence.json.

    Args:
        case_id (str): Unique case identifier.
        evidence_data (dict): Evidence details (e.g., URL, APK, transaction).
        case_path (str): Path to the case folder.

    Returns:
        str: Path to the created evidence.json file.
    """
    evidence_file = create_evidence_json(case_id, evidence_data, case_path)

    # Update case metadata
    update_case_metadata(case_path, evidence_count=1)

    print(f"[CASE_MGMT] Evidence collected for case {case_id}")
    return evidence_file
