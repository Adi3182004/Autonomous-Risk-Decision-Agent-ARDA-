from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
    user_id: str
    risk_score: int
    reason: str
    timestamp: datetime
