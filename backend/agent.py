from collections import defaultdict
from config import AUTO_ENFORCEMENT

USER_STATE = defaultdict(lambda: {
    "status": "ACTIVE",
    "risk_history": []
})

def decide_action(user, risk):
    USER_STATE[user]["risk_history"].append(risk)

    if risk >= 90:
        if AUTO_ENFORCEMENT:
            USER_STATE[user]["status"] = "LOCKED"
            return "LOCK", "User account locked due to critical risk"
        return "LOCK_RECOMMENDED", "Lock recommended – awaiting admin approval"

    if risk >= 75:
        if AUTO_ENFORCEMENT:
            USER_STATE[user]["status"] = "RESTRICTED"
            return "RESTRICT", "User access restricted automatically"
        return "RESTRICT_RECOMMENDED", "Restriction recommended"

    if risk >= 60:
        return "WARN", "User warned for suspicious behavior"

    return "ALLOW", "Normal behavior"
