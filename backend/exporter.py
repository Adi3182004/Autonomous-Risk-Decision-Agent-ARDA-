from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reporter import build_report
from detector import get_alerts

def export_incident_pdf(incident_id):
    alerts = get_alerts()

    for alert in alerts:
        report = build_report(alert)
        if report["incident_id"] == incident_id:
            return generate_pdf(report)

    return None


def generate_pdf(report):
    file_path = f"/tmp/{report['incident_id']}.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)

    text = c.beginText(40, 800)
    text.setFont("Helvetica", 10)

    for k, v in report.items():
        text.textLine(f"{k}: {v}")

    c.drawText(text)
    c.showPage()
    c.save()

    return file_path
