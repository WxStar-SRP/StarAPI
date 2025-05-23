import uuid
from fastapi import APIRouter
from fastapi.responses import FileResponse
from sqlmodel import select, or_
from dependencies import SessionDep
from models import post, enums
from database.db_models import WXStar
import tempfile

router = APIRouter(
    prefix = "/services/moon",
    tags = ["System Services", "MOON"]
)

@router.get("/wxstar_locids")
async def get_wxstar_location_ids(star_model: enums.WxStarModel,
                                  session: SessionDep):
    
    if star_model == enums.WxStarModel.i2_generic:
        locations = session.exec(select(WXStar.locations).filter(or_(
                                WXStar.model == enums.WxStarModel.i2xd,
                                WXStar.model == enums.WxStarModel.i2hd,
                                WXStar.model == enums.WxStarModel.i2jr
                            ))).all()
        
        
    if star_model == enums.WxStarModel.i1_generic:
        locations = session.exec(select(WXStar.locations)
                                .where(WXStar.model == enums.WxStarModel.i1_generic)).all()
        
    
    location_ids = list()
    
    for location in locations:
        
        if location is None:
            continue
        
        for id in location:
            
            if id not in location_ids:
                location_ids.append(id)
                
    
    return {"locations": location_ids}
    
