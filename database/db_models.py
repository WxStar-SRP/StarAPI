import uuid
from datetime import datetime, timezone
from typing import Annotated,List
from sqlmodel import Field,Session,SQLModel,Column,ARRAY,Text,UUID


class WXStar(SQLModel, table=True):
    __tablename__ = "wxstars"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str | None = Field(default="PENDING")
    model: str | None = Field(default="PENDING")
    locations: List[str] = Field(sa_column=Column(ARRAY(Text)))
    zones: List[str] = Field(sa_column=Column(ARRAY(Text)))
    gfxpkg_lf: str | None = Field(default=None, nullable=True)
    gfxpkg_ldl: str | None = Field(default=None, nullable=True)
    ip_addr: str = Field(default="127.0.0.1", nullable=False)   # This can also be updated automatically
    data_port: str = Field(default="7777", nullable=False)
    data_port_pri: str = Field(default="7788", nullable=False)
    #msocode: int | None = Field(default=None, nullable=True)    # Reported by receivers
    online: bool = Field(default=False)     # Reported by receivers
    
    
# class AdCrawl(SQLModel, table=True):
#     __tablename__ = "adcrawls"
#     id: uuid.UUID = Field(default_factory=uuid.uuid3, primary_key=True)
#     stars: List[uuid.UUID] = Field(sa_column=Column(ARRAY(UUID)))
#     start_date: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
#     end_date: datetime = Field(default=None, nullable=True)
#     crawl: str = Field(nullable=False)
    
    
class SystemService(SQLModel, table=True):
    __tablename__ = "systemservices"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    host: str = Field(default="127.0.0.1", nullable=False)
    pid: int | None = Field(default=0, nullable=False)
    name: str = Field(nullable=False)
    started: datetime = Field(default=datetime.now(timezone.utc))
    last_update: datetime | None = Field(default=None, nullable=True)
    json_stats: str | None = Field(default=None, nullable=True)
    online: bool = Field(default=False)
    