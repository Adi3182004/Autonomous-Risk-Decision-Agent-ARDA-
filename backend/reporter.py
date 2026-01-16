import hashlib
from datetime import datetime
from agent import decide_action

def generate_incident_id(user, timestamp):
    raw = f"{user}-{timestamp}".encode()
    return "INC-" + hashlib.md5(raw).hexdigest()[:10]

def enrich_with_decision(report):
    action, message = decide_action(report["user"], report["confidence"])
    report["decision"] = action
    report["system_action"] = message
    return report

def build_report(alert):
    user = alert.get("user", "unknown")
    severity = alert.get("severity", "low")
    threat_type = alert.get("threat_type", "unknown")
    attack_phases = alert.get("attack_phases", [])
    confidence = alert.get("confidence", 0.0)

    summary = (
        alert.get("executive_summary")
        or alert.get("summary")
        or "No executive summary available"
    )

    timestamp = (
        alert.get("start_time")
        or alert.get("timestamp")
        or datetime.utcnow().isoformat()
    )

    incident_id = generate_incident_id(user, timestamp)
    action, message = decide_action(user, confidence)

    return {
        "incident_id": incident_id,
        "user": user,
        "severity": severity,
        "threat_type": threat_type,
        "attack_phases": attack_phases,
        "summary": summary,
        "confidence": confidence,
        "time_window": {
            "start": timestamp,
            "end": timestamp
        },
        "decision": action,
        "system_action": message
    }
