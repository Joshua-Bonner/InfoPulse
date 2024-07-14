import logging
import sys
from contextlib import asynccontextmanager
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))

from app.routers.auth_router import router as auth_router
from app.routers.search_router import router as search_router
from app.routers.user_router import router as user_router
from common.helpers.db_client import DatabaseClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger("uvicorn.error")
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting InfoPulse API")
    try:
        app.include_router(auth_router, tags=["auth"], prefix="/auth")
        app.include_router(user_router, tags=["user"], prefix="/user")
        app.include_router(search_router, tags=["search"], prefix="/search")
        DatabaseClient().create_all()
        yield
    finally:
        logger.info("Stopping InfoPulse API")


app = FastAPI(
    title="InfoPulse API",
    description="API for InfoPulse",
    version="1.0",
    contact={"name": "Joshua Bonner", "email": "jbb5882@psu.edu"},
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
