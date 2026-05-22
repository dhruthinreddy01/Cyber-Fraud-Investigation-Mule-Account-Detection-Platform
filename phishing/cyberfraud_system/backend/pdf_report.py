from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf_report(case_id, case_path, evidence_summary, it_act_sections):
    """
    Generate a PDF report for a case.

    Args:
        case_id (str): Unique identifier for the case.
        case_path (str): Path to the case folder.
        evidence_summary (dict): Summary of evidence.
        it_act_sections (list): List of IT Act sections.

    Returns:
        str: Path to the generated PDF report.
    """
    report_path = os.path.join(case_path, f"{case_id}_report.pdf")
    c = canvas.Canvas(report_path, pagesize=letter)

    c.drawString(100, 750, f"Case ID: {case_id}")
    c.drawString(100, 730, "Evidence Summary:")
    y = 710
    for key, value in evidence_summary.items():
        c.drawString(120, y, f"{key}: {value}")
        y -= 20

    c.drawString(100, y, "IT Act Sections:")
    y -= 20
    for section in it_act_sections:
        c.drawString(120, y, section)
        y -= 20

    c.save()
    return report_path