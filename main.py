from fastapi import FastAPI, Response, Request

from core.settings import EnvData
from core.routers import api_router
from core.db import SessionLocal


app = FastAPI(title=EnvData.project_title)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(api_router)
