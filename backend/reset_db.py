from database import SessionLocal
from models import ActivityLog

db = SessionLocal()
db.query(ActivityLog).delete()
db.commit()
db.close()
from database import engine
from models import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Database reset complete")
