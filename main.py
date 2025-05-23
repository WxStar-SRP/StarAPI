from typing import Annotated
from fastapi import FastAPI,Depends

app = FastAPI(
    title="WXStar Management API",
    version="0.1.0a",
    redoc_url=None,
    docs_url = "/apidoc"
)

@app.get("/")
async def get_root():
    return {"Hello!"}

@app.on_event("startup")
def on_startup():
    
    print("Hello world!")