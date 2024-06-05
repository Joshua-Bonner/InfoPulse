import logging
import sys
from contextlib import asynccontextmanager
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))

from app.routers.auth_router import router as auth_router
from fastapi import FastAPI

logger = logging.getLogger("uvicorn.error")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting InfoPulse API")
    try:
        app.include_router(auth_router, prefix="/auth")
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


@app.get("/")
def read_root():
    return {"Hello": "World"}
