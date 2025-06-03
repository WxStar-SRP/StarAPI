from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/crawls",
    tags=["Ad Crawls"]
)

