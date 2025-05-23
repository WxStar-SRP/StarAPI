import uuid
import json
from fastapi import APIRouter, HTTPException
from models import post, put
from dependencies import SessionDep
from database.db_models import SystemService
from sqlmodel import select

router = APIRouter(
    prefix="/services",
    tags=["System Services"]
)

@router.post("/register")
async def register_system_service(service_info: post.SystemServiceIn,
                                  session: SessionDep):
    
    new_service = SystemService(
        name = service_info.name,
        host = service_info.host,
        pid = service_info.pid
    )
    
    session.add(new_service)
    session.commit()
    session.refresh(new_service)
    
    return new_service.id


@router.put("/report_up")
async def service_report_uptime(uptime_report: put.ServiceUptimeReport,
                                service_uuid: uuid.UUID,
                                session: SessionDep):
    
    try:
        service = session.exec(select(SystemService).where(SystemService.id == service_uuid)).one()
    except:
        raise HTTPException(
            status_code = 404,
            detail = "System service not found."
        )
        
    # Update the start time of the service if we just went from offline --> online
    if not service.online and uptime_report.online:
        service.started = uptime_report.update_timestamp
        
    service.online = uptime_report.online
    service.last_update = uptime_report.update_timestamp
    service.json_stats = uptime_report.json_stats
    
    session.add(service)
    session.commit()
    session.refresh(service)
    
    return {"Updated service status."}


@router.get("/{service_uuid}")
async def get_service_information(service_uuid: uuid.UUID,
                                  session: SessionDep):
    
    try:
        service = session.exec(select(SystemService).where(SystemService.id == service_uuid)).one()
    except:
        raise HTTPException(
            status_code=404,
            detail="System service not found."
        )
        
    return service

@router.get("/{service_uuid}/stats")
async def get_service_json_stats(service_uuid: uuid.UUID,
                                 session: SessionDep):
    try:
        json_info = session.exec(select(SystemService.json_stats)
                               .where(SystemService.id == service_uuid)).one()
    except:
        raise HTTPException(
            status_code=404,
            detail="System service not found."
        ) 
        
    if json_info is None:
        raise HTTPException(
            status_code=404,
            detail="This service has not reported any stats."
        )
        
    json_info_parsed = json.loads(json_info)
    
    return json_info_parsed