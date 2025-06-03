import uuid
from fastapi import APIRouter, HTTPException
from dependencies import SessionDep
from sqlmodel import select
from database.db_models import Headend
from models.post import HeadendIn

router = APIRouter(
    prefix = "/headend",
    tags = ["Headend Management"]
)

@router.post("/register", status_code=201)
async def register_new_headend(headend: HeadendIn, session: SessionDep):
    new_headend = Headend(
        name = headend.name,
        msocode = headend.msocode
    )

    session.add(new_headend)
    session.commit()
    session.refresh(new_headend)

    return new_headend


@router.get("/{headend_uuid}", status_code=200)
async def get_headend_info(headend_uuid: uuid.UUID, session: SessionDep):
    try:
        headend = session.exec(select(Headend).where(Headend.id == headend_uuid)).one()

        return headend

    except: 
        raise HTTPException(
            status_code=404,
            detail="Headend not found"
        )