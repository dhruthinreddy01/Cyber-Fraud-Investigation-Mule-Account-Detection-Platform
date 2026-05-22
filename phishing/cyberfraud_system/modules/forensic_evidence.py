"""
Forensic Evidence Collection Module
APK + URL evidence intake and analysis
"""
import os
import json
import hashlib
import re
import socket
import subprocess
from datetime import datetime


def hash_file(file_path):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def hash_string(text):
    """Calculate SHA256 hash of a string."""
    return hashlib.sha256(text.encode()).hexdigest()


def perform_whois_lookup(domain):
    """
    Perform WHOIS lookup on a domain.
    """
    try:
        import whois
        w = whois.whois(domain)
        return {
            "domain": domain,
            "registrant": str(w.registrant),
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date)
        }
    except Exception as e:
        print(f"[WHOIS] Lookup failed for {domain}: {e}")
        return {"domain": domain, "error": str(e)}


def resolve_dns(domain):
    """Resolve DNS records for a domain."""
    try:
        ip = socket.gethostbyname(domain)
        return {
            "domain": domain,
            "ip_address": ip,
            "resolved_at": datetime.now().isoformat()
        }
    except Exception as e:
        print(f"[DNS] Resolution failed for {domain}: {e}")
        return {"domain": domain, "error": str(e)}


def take_screenshot(url, output_path):
    """
    Capture screenshot of webpage using Selenium.
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.save_screenshot(output_path)
        driver.quit()
        print(f"[SCREENSHOT] Saved to {output_path}")
        return True
    except Exception as e:
        print(f"[SCREENSHOT] Failed for {url}: {e}")
        return False


def extract_apk_metadata(apk_path):
    """
    Extract metadata from APK file.
    """
    try:
        from androguard.core.apk import APK
        
        apk = APK(apk_path)
        sha256 = hash_file(apk_path)
        
        metadata = {
            "sha256": sha256,
            "package_name": apk.get_package(),
            "version": apk.get_androidversion_code(),
            "permissions": apk.get_permissions(),
            "activities": apk.get_activities(),
            "analyzed_at": datetime.now().isoformat()
        }
        print(f"[APK_ANALYSIS] Extracted metadata from {apk_path}")
        return metadata
    except Exception as e:
        print(f"[APK_ANALYSIS] Failed: {e}")
        return {"error": str(e)}


def collect_evidence(case_path, evidence_type, evidence_data):
    """
    Collect and store evidence in a case folder.
    
    Args:
        case_path: Path to the case folder
        evidence_type: Type of evidence (APK, URL, PHONE)
        evidence_data: Dictionary with evidence details
    """
    evidence_file = os.path.join(case_path, f"evidence_{evidence_type}.json")
    
    evidence_record = {
        "type": evidence_type,
        "collected_at": datetime.now().isoformat(),
        "data": evidence_data
    }
    
    with open(evidence_file, 'w') as f:
        json.dump(evidence_record, f, indent=4)
    
    print(f"[EVIDENCE] Collected {evidence_type} evidence")
    return evidence_file


def save_whois_data(domain, case_path):
    """Save WHOIS data to case folder."""
    whois_data = perform_whois_lookup(domain)
    whois_file = os.path.join(case_path, "whois.json")
    
    with open(whois_file, 'w') as f:
        json.dump(whois_data, f, indent=4)
    
    print(f"[FORENSIC] WHOIS data saved")
    return whois_file


def save_dns_data(domain, case_path):
    """Save DNS resolution data to case folder."""
    dns_data = resolve_dns(domain)
    dns_file = os.path.join(case_path, "dns.json")
    
    with open(dns_file, 'w') as f:
        json.dump(dns_data, f, indent=4)
    
    print(f"[FORENSIC] DNS data saved")
    return dns_file


def save_screenshot(url, case_path):
    """Save webpage screenshot to case folder."""
    screenshot_path = os.path.join(case_path, "screenshot.png")
    take_screenshot(url, screenshot_path)
    return screenshot_path


def save_apk_metadata(apk_path, case_path):
    """Save APK metadata to case folder."""
    metadata = extract_apk_metadata(apk_path)
    apk_file = os.path.join(case_path, "apk_metadata.json")
    
    with open(apk_file, 'w') as f:
        json.dump(metadata, f, indent=4)
    
    print(f"[FORENSIC] APK metadata saved")
    return apk_file


def create_evidence_json(case_id, evidence_data, case_path):
    """
    Create evidence.json file for a case.

    Args:
        case_id (str): Unique case identifier.
        evidence_data (dict): Evidence details (e.g., URL, APK, transaction).
        case_path (str): Path to the case folder.

    Returns:
        str: Path to the created evidence.json file.
    """
    evidence_file = os.path.join(case_path, "evidence.json")
    evidence = {
        "case_id": case_id,
        "timestamp": datetime.now().isoformat(),
        "input_data": evidence_data.get("input"),
        "sha256": evidence_data.get("sha256"),
        "ip_address": evidence_data.get("ip_address"),
        "whois_data": evidence_data.get("whois_data"),
        "dns_data": evidence_data.get("dns_data"),
        "collected_by": "SOC_ANALYST"
    }

    with open(evidence_file, 'w') as f:
        json.dump(evidence, f, indent=4)

    print(f"[EVIDENCE] evidence.json created at {evidence_file}")
    return evidence_file
