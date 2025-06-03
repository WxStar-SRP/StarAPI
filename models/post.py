from pydantic import BaseModel
from typing import Optional,List
from models import enums
from datetime import datetime, timezone


class WxStarIn(BaseModel):
    name: Optional[str] = None
    model: Optional[enums.WxStarModel] = None
    ip_addr: str = "127.0.0.1"
    data_port: str = "7777"
    data_port_pri: str = "7788"
    gfxpkg_lf: Optional[str] = None
    gfxpkg_ldl: Optional[str] = None
    
    
class HeadendIn(BaseModel):
    name: str
    msocode: int


class CrawlIn(BaseModel):
    msocode: int
    start_date: datetime = datetime.now(timezone.utc)
    end_date: datetime
    crawl_txt: str


class SystemServiceIn(BaseModel):
    name: str
    host: str = "127.0.0.1"
    pid: Optional[int] = None
        