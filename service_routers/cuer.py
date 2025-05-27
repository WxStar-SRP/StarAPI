from fastapi import APIRouter, HTTPException, dependencies
from sqlmodel import select, or_
from dependencies import SessionDep
from models.enums import WxStarModel
from database.db_models import WXStar


router = APIRouter(
    prefix="/services/cuer",
    tags=["System Services", "Cuer"]
)


@router.get("/global_settings", status_code=200)
async def get_global_cue_settings(session: SessionDep):
    pass


@router.get("/star_cue_settings")
async def get_star_cue_settings(session: SessionDep,
                                star_type: WxStarModel):
    
    if star_type == WxStarModel.i2_generic:
        stars = session.exec(select(WXStar.id, WXStar.gfxpkg_ldl, WXStar.gfxpkg_lf)
                             .filter(or_(
                                WXStar.model == WxStarModel.i2xd,
                                WXStar.model == WxStarModel.i2hd,
                                WXStar.model == WxStarModel.i2jr))).all()
    
    cue_settings = []
        
    for star in stars:
        if star.gfxpkg_ldl is None or star.gfxpkg_lf is None:
            continue
        
        print(star)
        
        cue_settings.append({"id": star.id, "ldl": star.gfxpkg_ldl, "lf": star.gfxpkg_lf})
        
    if len(cue_settings) < 1:
        return HTTPException(
            204,
            detail = "The query requested returned no results."
        )
        
    return {"cue_settings": cue_settings}