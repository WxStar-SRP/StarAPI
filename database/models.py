import uuid
from datetime import datetime
from typing import Annotated,List
from sqlmodel import Field,Session,SQLModel,Column,ARRAY,Text,UUID


class WXStar(SQLModel, table=True):
    __tablename__ = "wxstars"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(default="PENDING")
    model: str = Field(default="PENDING")
    locations: List[str] = Field(sa_column=Column(ARRAY(Text)))
    zones: List[str] = Field(sa_column=Column(ARRAY(Text)))
    gfxpkg_lf: str = Field(default=None, nullable=True)
    gfxpkg_ldl: str = Field(default=None, nullable=True)
    ip_addr: str = Field(default="127.0.0.1", nullable=False)   # This can also be updated automatically
    data_port: str = Field(default="7777", nullable=False)
    data_port_pri: str = Field(default="7788", nullable=False)
    
    
class AdCrawl(SQLModel, table=True):
    __tablename__ = "adcrawls"
    id: uuid.UUID = Field(default_factory=uuid.uuid3, primary_key=True)
    stars: List[uuid.UUID] = Field(sa_column=Column(ARRAY(UUID)))
    start_date: datetime
    end_date: datetime
    crawl: str
    

