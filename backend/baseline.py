from database import SessionLocal
from models import ActivityLog
from collections import defaultdict

def build_baseline():
    db = SessionLocal()
    data = db.query(ActivityLog).all()
    db.close()

    baseline = defaultdict(lambda: {
        "hours": [],
        "resources": set(),
        "actions": defaultdict(int)
    })

    for log in data:
        hour = log.timestamp.hour
        baseline[log.user_id]["hours"].append(hour)
        baseline[log.user_id]["resources"].add(log.resource)
        baseline[log.user_id]["actions"][log.action_type] += 1

    for user in baseline:
        hours = baseline[user]["hours"]
        baseline[user]["avg_hour"] = sum(hours) / len(hours)
        baseline[user]["resource_count"] = len(baseline[user]["resources"])

    return baseline
