import uuid

def generate_explanation(session, reasons, risk_score, severity):
    if severity == "Critical":
        threat_type = "Privilege Abuse"
        confidence = 95
    else:
        threat_type = "Anomalous Behavior"
        confidence = 75

    summary = (
        f"User {session[0].user_id} exhibited suspicious behavior between "
        f"{session[0].timestamp} and {session[-1].timestamp}. "
        f"The user escalated privileges during this period."
    )

    if "Off-hours activity" in reasons:
        summary += " Actions occurred outside the user’s normal activity window."

    if severity == "Critical":
        summary += " Potential data misuse or unauthorized access to sensitive systems."
    else:
        summary += " Suspicious behavior requiring further monitoring."

    return {
        "incident_id": f"INC-{uuid.uuid4().hex[:10]}",
        "threat_type": threat_type,
        "executive_summary": summary,
        "confidence": confidence
    }
