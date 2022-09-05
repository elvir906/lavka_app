from fastapi import FastAPI, Request

from core.settings import settings
from core.routers import api_router
from core.db import SessionLocal


app = FastAPI(title=settings.PROJECT_NAME)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    # response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(api_router)
