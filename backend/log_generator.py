import random
from datetime import datetime, timedelta
from database import SessionLocal, engine
from models import ActivityLog, Base

Base.metadata.create_all(bind=engine)

users = [
    {"id": "aditya", "risk": "high"},
    {"id": "aditi", "risk": "medium"},
    {"id": "om", "risk": "low"}
]

normal_actions = ["LOGIN", "FILE_READ"]
risky_actions = ["FILE_WRITE", "PRIV_ESC"]

resources = [
    "HR_SALARY.xlsx",
    "FINANCE.xlsx",
    "ENG_DOCS.pdf",
    "SOURCE_CODE.zip"
]

locations = ["Office", "Remote", "VPN"]

db = SessionLocal()

base_time = datetime.now() - timedelta(hours=24)

for user in users:
    current_time = base_time

    for _ in range(100):
        if user["risk"] == "high":
            action = random.choices(
                normal_actions + risky_actions,
                weights=[10, 10, 30, 50]
            )[0]
            privilege = "ADMIN" if action == "PRIV_ESC" else "USER"

        elif user["risk"] == "medium":
            action = random.choices(
                normal_actions + risky_actions,
                weights=[25, 25, 35, 15]
            )[0]
            privilege = "ADMIN" if action == "PRIV_ESC" else "USER"

        else:
            action = random.choice(normal_actions)
            privilege = "USER"

        log = ActivityLog(
            user_id=user["id"],
            action_type=action,
            resource=random.choice(resources),
            privilege_level=privilege,
            timestamp=current_time,
            location=random.choice(locations)
        )

        db.add(log)
        current_time += timedelta(minutes=random.randint(2, 15))

db.commit()
db.close()
