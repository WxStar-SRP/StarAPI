from typing import Annotated
from fastapi import FastAPI,Depends
import database.db
from database import db_models
from routers import wxstar, service
from service_routers import moon, cuer

app = FastAPI(
    title="WXStar Management API",
    version="0.1.0a",
    redoc_url=None,
    docs_url = "/apidoc"
)


# Basic operational routers
app.include_router(wxstar.router)
app.include_router(service.router)


# System Service Routers
app.include_router(moon.router)
app.include_router(cuer.router)


@app.get("/")
async def get_root():
    return {"Hello!"}

@app.on_event("startup")
def on_startup():
    database.db.init_database()