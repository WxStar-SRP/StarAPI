from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix = "/headend",
    tags = ["Headend Management"]
)