from datetime import timedelta
from database import SessionLocal
from models import ActivityLog

WINDOW_MINUTES = 30

def reconstruct_paths():
    db = SessionLocal()
    logs = db.query(ActivityLog).order_by(ActivityLog.timestamp).all()
    db.close()

    user_sessions = {}
    paths = []

    for log in logs:
        user = log.user_id
        if user not in user_sessions:
            user_sessions[user] = [log]
            continue

        last_log = user_sessions[user][-1]
        if log.timestamp - last_log.timestamp <= timedelta(minutes=WINDOW_MINUTES):
            user_sessions[user].append(log)
        else:
            paths.append(user_sessions[user])
            user_sessions[user] = [log]

    for session in user_sessions.values():
        if session:
            paths.append(session)

    return paths
