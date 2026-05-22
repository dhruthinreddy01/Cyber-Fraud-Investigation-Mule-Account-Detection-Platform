"""
Legal Mapper Module
Indian IT Act and IPC section mapping
"""


def map_it_act(evidence_type):
    """
    Map evidence type to applicable Indian IT Act sections.
    
    Args:
        evidence_type: Type of evidence (APK, URL, PHONE, TRANSACTION)
    
    Returns:
        dict: IT Act sections and descriptions
    """
    mapping = {
        "URL": {
            "sections": ["IT Act 66D", "IT Act 43", "IPC 419"],
            "description": "Phishing / Identity Fraud",
            "penalties": "3 years imprisonment + Rs. 1,00,000 fine"
        },
        "APK": {
            "sections": ["IT Act 66C", "IT Act 66D", "IT Act 43"],
            "description": "Malware / Unauthorized Access",
            "penalties": "3 years imprisonment + Rs. 2,50,000 fine"
        },
        "TRANSACTION": {
            "sections": ["IT Act 43", "IT Act 66C", "IPC 420"],
            "description": "Financial Fraud",
            "penalties": "5 years imprisonment + Rs. 5,00,000 fine"
        },
        "PHONE": {
            "sections": ["IT Act 66D", "IT Act 43", "IPC 507"],
            "description": "Call/SMS Fraud",
            "penalties": "3 years imprisonment + Rs. 1,00,000 fine"
        },
        "DEFAULT": {
            "sections": ["IT Act 43"],
            "description": "Unauthorized Access",
            "penalties": "2 years imprisonment + Rs. 50,000 fine"
        }
    }
    
    return mapping.get(evidence_type, mapping["DEFAULT"])


def get_section_details(section_code):
    """Get detailed information about an IT Act section."""
    details = {
        "IT Act 43": "Punishment for misuse of computer system",
        "IT Act 66C": "Punishment for identity theft",
        "IT Act 66D": "Punishment for phishing and fraudulent solicitation",
        "IPC 419": "Punishment for cheating by impersonation",
        "IPC 420": "Punishment for cheating and dishonestly inducing delivery"
    }
    
    return details.get(section_code, "Unknown section")


def generate_legal_summary(evidence_type):
    """Generate a legal summary for case reporting."""
    mapping = map_it_act(evidence_type)
    
    summary = f"""
LEGAL FRAMEWORK
================
Evidence Type: {evidence_type}
Offence: {mapping['description']}

Applicable Sections:
{chr(10).join([f"  • {section}" for section in mapping['sections']])}

Penalties: {mapping['penalties']}

This case falls under the Information Technology Act, 2000 
and relevant sections of the Indian Penal Code.
    """
    
    return summary.strip()


def integrate_legal_mapping(evidence_type, ui_data, pdf_data, dashboard_data):
    """
    Integrate legal mapping into UI, PDF, and dashboard.

    Args:
        evidence_type (str): Type of evidence (e.g., URL, APK, TRANSACTION).
        ui_data (dict): Data to display in the UI.
        pdf_data (dict): Data to include in the PDF report.
        dashboard_data (dict): Data to display on the dashboard.

    Returns:
        dict: Updated data with legal mapping.
    """
    legal_mapping = map_it_act(evidence_type)

    # Update UI data
    ui_data["legal_mapping"] = legal_mapping

    # Update PDF data
    pdf_data["legal_sections"] = legal_mapping["sections"]
    pdf_data["legal_description"] = legal_mapping["description"]
    pdf_data["legal_penalties"] = legal_mapping["penalties"]

    # Update dashboard data
    dashboard_data["legal_mapping"] = legal_mapping

    return {
        "ui_data": ui_data,
        "pdf_data": pdf_data,
        "dashboard_data": dashboard_data
    }
