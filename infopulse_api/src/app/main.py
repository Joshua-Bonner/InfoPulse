from fastapi import FastAPI
import logging
from contextlib import asynccontextmanager

logger = logging.getLogger("uvicorn.error")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting InfoPulse API")
    try:
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
