from baseline import build_baseline
from path_analyzer import reconstruct_paths
from explain import generate_explanation
from collections import defaultdict
from config import AUTO_ENFORCEMENT

SENSITIVE_FILES = {"HR_SALARY.xlsx", "FINANCE.xlsx"}

def detect_anomalies():
    baseline = build_baseline()
    paths = reconstruct_paths()
    grouped = defaultdict(list)

    for session in paths:
        user = session[0].user_id
        grouped[user].append(session)

    alerts = []

    for user, sessions in grouped.items():
        total_risk = 0
        reasons = []
        start_time = sessions[0][0].timestamp
        end_time = sessions[-1][-1].timestamp

        for session in sessions:
            for log in session:
                base = baseline[user]
                hour_diff = abs(log.timestamp.hour - base["avg_hour"])

                if hour_diff > 4:
                    total_risk += 10
                    reasons.append("Off-hours activity")

                if log.action_type == "PRIV_ESC":
                    total_risk += 25
                    reasons.append("Privilege escalation")

                if log.resource in SENSITIVE_FILES and log.resource not in base["resources"]:
                    total_risk += 30
                    reasons.append("New sensitive resource access")

        total_risk = min(total_risk, 100)

        if total_risk >= 60:
            severity = "Critical" if total_risk >= 90 else "High"

            explanation = generate_explanation(
                sessions[0],
                reasons,
                total_risk,
                severity
            )

            if total_risk >= 90:
                decision = "LOCK"
                system_action = (
                    "User account locked due to critical risk"
                    if AUTO_ENFORCEMENT
                    else "Lock recommended – awaiting admin approval"
                )

            elif total_risk >= 70:
                decision = "RESTRICT"
                system_action = (
                    "Access restricted"
                    if AUTO_ENFORCEMENT
                    else "Restriction recommended – awaiting admin approval"
                )

            else:
                decision = "WARN"
                system_action = "User warned"

            alerts.append({
                "incident_id": explanation["incident_id"],
                "user": user,
                "severity": severity,
                "threat_type": explanation["threat_type"],
                "attack_phases": list(set(
                    ["Privilege Escalation" if "Privilege escalation" in r else "Anomalous Access Pattern"
                     for r in reasons]
                )),
                "summary": explanation["executive_summary"],
                "confidence": explanation["confidence"],
                "time_window": {
                    "start": start_time,
                    "end": end_time
                },
                "decision": decision,
                "system_action": system_action
            })

    return alerts
