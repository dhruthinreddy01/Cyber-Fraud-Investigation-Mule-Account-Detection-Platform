"""
SOC Dashboard Module
Security Operations Center metrics and analytics
"""
import os
import json
from glob import glob


def get_dashboard_data():
    """
    Fetch SOC dashboard data from evidence cases.
    
    Returns:
        dict: Dashboard metrics
    """
    cases_path = "evidence/cases"
    
    if not os.path.exists(cases_path):
        return {
            "total_cases": 0,
            "phishing_cases": 0,
            "apk_cases": 0,
            "transaction_cases": 0,
            "url_cases": 0,
            "cases": []
        }
    
    case_dirs = glob(os.path.join(cases_path, "CASE_*"))
    
    phishing_count = 0
    apk_count = 0
    transaction_count = 0
    url_count = 0
    cases_list = []
    
    for case_dir in case_dirs:
        case_id = os.path.basename(case_dir)
        metadata_file = os.path.join(case_dir, "case_metadata.json")
        
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)
                cases_list.append({
                    "case_id": case_id,
                    "created_at": metadata.get("created_at"),
                    "status": metadata.get("status")
                })
        
        # Check evidence types
        if os.path.exists(os.path.join(case_dir, "evidence_URL.json")):
            phishing_count += 1
            url_count += 1
        if os.path.exists(os.path.join(case_dir, "evidence_APK.json")):
            apk_count += 1
        if os.path.exists(os.path.join(case_dir, "evidence_TRANSACTION.json")):
            transaction_count += 1
    
    return {
        "total_cases": len(case_dirs),
        "phishing_cases": phishing_count,
        "apk_cases": apk_count,
        "transaction_cases": transaction_count,
        "url_cases": url_count,
        "cases": cases_list
    }


def get_case_statistics():
    """Get statistical summary of all cases."""
    dashboard = get_dashboard_data()
    
    stats = {
        "total": dashboard["total_cases"],
        "phishing": dashboard["phishing_cases"],
        "apk": dashboard["apk_cases"],
        "transaction": dashboard["transaction_cases"]
    }
    
    return stats


# High-risk alerts
    high_risk_cases = [case for case in cases_list if case.get("risk_level") == "HIGH"]

    # Add high-risk alerts and recent cases
    return {
        "total_cases": len(case_dirs),
        "phishing_cases": phishing_count,
        "apk_cases": apk_count,
        "transaction_cases": transaction_count,
        "url_cases": url_count,
        "cases": cases_list,
        "high_risk_alerts": high_risk_cases,
        "recent_cases": sorted(cases_list, key=lambda x: x.get("created_at", ""), reverse=True)[:5]
    }
