from pydantic import BaseModel
from typing import Optional, List
from models import enums
from datetime import datetime,timezone

class ServiceUptimeReport(BaseModel):
    online: bool = False
    update_timestamp: datetime = datetime.now(timezone.utc)
    json_stats: Optional[str] = None
    

class WxStarLocationUpdate(BaseModel):
    locations: List[str]
    zones: Optional[List[str]] = None