import hashlib
import json
import os
import socket
from datetime import datetime
import whois

def collect_evidence(case_id, evidence_data, base_path="evidence/cases"):
    """
    Collect forensic evidence and save it as a JSON file.

    Args:
        case_id (str): Unique identifier for the case.
        evidence_data (dict): Evidence details.
        base_path (str): Base directory for storing cases.

    Returns:
        str: Path to the evidence JSON file.
    """
    case_folder = os.path.join(base_path, case_id)
    os.makedirs(case_folder, exist_ok=True)

    evidence_file = os.path.join(case_folder, "evidence.json")
    with open(evidence_file, "w") as f:
        json.dump(evidence_data, f, indent=4)

    return evidence_file

def calculate_sha256(file_path):
    """
    Calculate the SHA256 hash of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: SHA256 hash of the file.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_dns_and_whois(domain):
    """
    Retrieve DNS and WHOIS information for a domain.

    Args:
        domain (str): Domain name.

    Returns:
        dict: DNS and WHOIS information.
    """
    try:
        ip_address = socket.gethostbyname(domain)
        whois_info = whois.whois(domain)
        return {
            "ip_address": ip_address,
            "whois": whois_info
        }
    except Exception as e:
        return {"error": str(e)}

def save_evidence(case_id, file_path, metadata):
    """
    Save evidence metadata to a JSON file.

    Args:
        case_id (str): Unique identifier for the case.
        file_path (str): Path to the evidence file.
        metadata (dict): Metadata to save.

    Returns:
        str: Path to the evidence JSON file.
    """
    import os
    import json
    from datetime import datetime

    # Create case folder
    case_folder = os.path.join("evidence/cases", case_id)
    os.makedirs(case_folder, exist_ok=True)
    print(f"[DEBUG] Created case folder: {case_folder}")

    # Add timestamp to metadata
    metadata["timestamp"] = datetime.now().isoformat()

    # Save metadata to evidence.json
    evidence_file = os.path.join(case_folder, "evidence.json")
    with open(evidence_file, "w") as f:
        json.dump(metadata, f, indent=4)
    print(f"[DEBUG] Saved evidence.json: {evidence_file}")

    return evidence_file