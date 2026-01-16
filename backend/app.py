from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from detector import detect_anomalies
from reporter import build_report, enrich_with_decision
from path_analyzer import reconstruct_paths
from exporter import export_incident_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/agent")
def agent(simulate: str = None):
    if simulate == "attack":
        from seed import trigger_attack
        trigger_attack()
        return {"status": "attack simulated"}
    return {"status": "idle"}

@app.get("/alerts")
def get_alerts():
    return detect_anomalies()

@app.get("/report")
def get_reports():
    alerts = detect_anomalies()
    return [build_report(a) for a in alerts]

@app.get("/agent")
def agent_view():
    alerts = detect_anomalies()
    reports = [build_report(a) for a in alerts]
    return [enrich_with_decision(r) for r in reports]

from fastapi.responses import FileResponse
from exporter import export_incident_pdf

@app.get("/export/{incident_id}")
def export_pdf(incident_id: str):
    pdf_path = export_incident_pdf(incident_id)

    if not pdf_path:
        return {"error": "Incident not found"}

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"{incident_id}.pdf"
    )


@app.get("/timeline/{user}")
def get_timeline(user: str):
    paths = reconstruct_paths()
    timeline = []

    for session in paths:
        if session[0].user_id != user:
            continue

        for log in session:
            timeline.append({
                "timestamp": log.timestamp,
                "action": log.action_type,
                "resource": log.resource,
                "location": log.location
            })

    return sorted(timeline, key=lambda x: x["timestamp"])
from fastapi import Body
from models import ActivityLog
from database import SessionLocal
from datetime import datetime

@app.post("/simulate")
def simulate(data: dict = Body(...)):
    db = SessionLocal()
    log = ActivityLog(
        user_id=data["user"],
        action_type=data["action"],
        resource="SIMULATED",
        privilege_level="ADMIN" if data["action"] == "PRIV_ESC" else "USER",
        timestamp=datetime.now(),
        location="WEB"
    )
    db.add(log)
    db.commit()
    db.close()
    return {"status": "ok"}
