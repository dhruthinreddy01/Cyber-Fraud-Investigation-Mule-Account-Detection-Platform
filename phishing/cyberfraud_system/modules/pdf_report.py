"""
PDF Report Generation Module
FIR-style investigation reports
"""
import os
import json
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY


def generate_pdf_report(case_id, case_path, evidence_summary, it_act_sections):
    """
    Generate a comprehensive PDF FIR-style investigation report.
    
    Args:
        case_id: Case identifier
        case_path: Path to case folder
        evidence_summary: Dictionary with evidence details
        it_act_sections: List of applicable IT Act sections
    
    Returns:
        str: Path to generated PDF
    """
    report_path = os.path.join(case_path, f"{case_id}_INVESTIGATION_REPORT.pdf")
    
    # Create PDF document
    doc = SimpleDocTemplate(report_path, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    story.append(Paragraph("CYBER FRAUD INVESTIGATION REPORT", title_style))
    story.append(Paragraph(f"Case ID: {case_id}", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Case Header
    header_data = [
        ["CASE ID:", case_id],
        ["DATE:", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        ["INVESTIGATING OFFICER:", "SOC_ANALYST"],
        ["STATUS:", "UNDER_INVESTIGATION"]
    ]
    
    header_table = Table(header_data, colWidths=[2*inch, 4*inch])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E8E8E8')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Evidence Summary
    story.append(Paragraph("EVIDENCE SUMMARY", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))
    
    evidence_text = f"""
    <b>Evidence Type:</b> {evidence_summary.get('type', 'N/A')}<br/>
    <b>SHA256 Hash:</b> {evidence_summary.get('sha256', 'N/A')}<br/>
    <b>Collection Date:</b> {evidence_summary.get('collected_at', 'N/A')}<br/>
    <b>Source:</b> {evidence_summary.get('source', 'N/A')}<br/>
    """
    
    story.append(Paragraph(evidence_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # IT Act Sections
    story.append(Paragraph("APPLICABLE LEGAL PROVISIONS", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))
    
    sections_text = "<br/>".join([f"• {section}" for section in it_act_sections['sections']])
    story.append(Paragraph(f"<b>Sections:</b><br/>{sections_text}", styles['Normal']))
    story.append(Paragraph(f"<b>Offense:</b> {it_act_sections['description']}", styles['Normal']))
    story.append(Paragraph(f"<b>Penalties:</b> {it_act_sections['penalties']}", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # IOC Section
    story.append(Paragraph("INDICATORS OF COMPROMISE (IOCs)", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))

    ioc_data = evidence_summary.get("iocs", [])
    ioc_text = "<br/>".join([
        f"• IP: {ioc.get('ip_address', 'N/A')}, Domain: {ioc.get('domain', 'N/A')}, Hash: {ioc.get('sha256', 'N/A')}, Cluster ID: {ioc.get('cluster_id', 'N/A')}"
        for ioc in ioc_data
    ])

    story.append(Paragraph(ioc_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Investigator Notes
    story.append(Paragraph("INVESTIGATOR REMARKS", styles['Heading2']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "This case has been registered based on evidence collection and analysis in accordance with "
        "the Information Technology Act, 2000. Further investigation is ongoing.",
        styles['Normal']
    ))
    
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        f"<b>Generated on:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>"
        f"<b>Investigator:</b> SOC_ANALYST<br/>"
        f"<b>Department:</b> Cybercrime Investigation Cell",
        styles['Normal']
    ))
    
    # Build PDF
    doc.build(story)
    print(f"[PDF_REPORT] Generated: {report_path}")
    
    return report_path


def generate_pdf_report_simple(case_id, case_path, evidence_summary, it_act_sections):
    """Simplified PDF generation without complex formatting."""
    report_path = os.path.join(case_path, f"{case_id}_INVESTIGATION_REPORT.pdf")
    
    from reportlab.pdfgen import canvas
    
    c = canvas.Canvas(report_path, pagesize=letter)
    width, height = letter
    
    y = height - 0.5 * inch
    
    # Title
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1 * inch, y, "CYBER FRAUD INVESTIGATION REPORT")
    y -= 0.3 * inch
    
    # Case Details
    c.setFont("Helvetica", 10)
    c.drawString(1 * inch, y, f"Case ID: {case_id}")
    y -= 0.2 * inch
    c.drawString(1 * inch, y, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 0.2 * inch
    c.drawString(1 * inch, y, f"Officer: SOC_ANALYST")
    y -= 0.3 * inch
    
    # Evidence
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1 * inch, y, "EVIDENCE SUMMARY")
    y -= 0.2 * inch
    
    c.setFont("Helvetica", 10)
    c.drawString(1 * inch, y, f"Type: {evidence_summary.get('type', 'N/A')}")
    y -= 0.2 * inch
    c.drawString(1 * inch, y, f"Hash: {evidence_summary.get('sha256', 'N/A')[:40]}")
    y -= 0.3 * inch
    
    # IT Act Sections
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1 * inch, y, "APPLICABLE SECTIONS")
    y -= 0.2 * inch
    
    c.setFont("Helvetica", 10)
    for section in it_act_sections.get('sections', []):
        c.drawString(1.2 * inch, y, f"• {section}")
        y -= 0.15 * inch
    
    y -= 0.1 * inch
    c.drawString(1 * inch, y, f"Offense: {it_act_sections.get('description')}")
    y -= 0.2 * inch
    c.drawString(1 * inch, y, f"Penalties: {it_act_sections.get('penalties')}")
    
    c.save()
    print(f"[PDF_REPORT] Generated: {report_path}")
    
    return report_path
