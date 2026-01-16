from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    action_type = Column(String)
    resource = Column(String)
    privilege_level = Column(String)
    timestamp = Column(DateTime)
    location = Column(String)
