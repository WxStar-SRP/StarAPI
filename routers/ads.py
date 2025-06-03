import uuid
from fastapi import APIRouter, HTTPException
from dependencies import SessionDep
from database.db_models import AdCrawl
from sqlmodel import select
from models.post import CrawlIn

router = APIRouter(
    prefix="/crawl",
    tags=["Ad Crawls"]
)

@router.post("/register", status_code=201)
async def register_new_adcrawl(crawl_info: CrawlIn, session: SessionDep):
    new_crawl = AdCrawl(
        msocode = crawl_info.msocode,
        start_date = crawl_info.start_date,
        end_date = crawl_info.end_date,
        crawl_txt = crawl_info.crawl_txt
    )

    session.add(new_crawl)
    session.commit()
    session.refresh(new_crawl)

    return new_crawl

@router.get("/headend/{msocode}")
async def get_headend_crawls(msocode: int, session: SessionDep):
    try:
        crawls = session.exec(select(AdCrawl).where(AdCrawl.msocode == msocode)).all()

        return {"crawls": crawls}
    except:
        raise HTTPException(
            status_code = 404, 
            detail = "No crawls found for this headend.")


@router.get("/{crawl_uuid}")
async def get_crawl_info(crawl_uuid: uuid.UUID, session: SessionDep):
    try:
        crawl = session.exec(select(AdCrawl).where(AdCrawl.id == crawl_uuid)).one()

        return crawl
    except:
        raise HTTPException(
            status_code = 404, 
            detail = "No crawl found"
        )