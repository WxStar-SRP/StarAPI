import uuid
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database.db_models import WXStar
from dependencies import SessionDep
from webhook import discord
import models.post
import models.put


router = APIRouter(
    prefix="/wxstar",
    tags=["WeatherStar Management"]
)

@router.post("/register", status_code=201)
async def register_wxstar_unit(star_info: models.post.WxStarIn,
                               session: SessionDep):
    
    db_wxstar = WXStar(
        name = star_info.name,
        model = star_info.model,
        ip_addr = star_info.ip_addr,
        data_port = star_info.data_port,
        data_port_pri = star_info.data_port_pri,
        gfxpkg_lf = star_info.gfxpkg_lf,
        gfxpkg_ldl = star_info.gfxpkg_ldl
    )
    
    session.add(db_wxstar)
    session.commit()
    session.refresh(db_wxstar)

    await discord.log_unit_creation(db_wxstar)
    
    return db_wxstar


@router.delete("/unregister", status_code=200)
async def unregister_wxstar_unit(star_uuid: uuid.UUID,
                                 session: SessionDep):
    
    # See if the unit exists in the database
    try:
        wxstar = session.exec(select(WXStar).where(WXStar.id == star_uuid)).one()
    except:
        raise HTTPException(
            status_code = 404,
            detail = "WeatherStar not found"
        )
        
    session.delete(wxstar)
    session.commit()


@router.get("/{star_uuid}", status_code=200)
async def get_wxstar_by_uuid(star_uuid: uuid.UUID,
                             session: SessionDep):
    
    star_info = session.exec(select(WXStar).where(WXStar.id == star_uuid)).one()
    
    return star_info


@router.put("/{star_uuid}/set_locations", status_code=200)
async def update_wxstar_locations(star_uuid: uuid.UUID, session: SessionDep, locations: models.put.WxStarLocationUpdate):
    try:
        wxstar = session.exec(select(WXStar).where(WXStar.id == star_uuid)).one()
    except:
        raise HTTPException(
            status_code = 404,
            detail = "WeatherStar not found"
        )

    wxstar.locations = locations.locations

    if locations.zones is not None:
        wxstar.zones = locations.zones
    
    session.add(wxstar)
    session.commit()
    session.refresh(wxstar)

    return {"Updated locations and/or zones."}
    