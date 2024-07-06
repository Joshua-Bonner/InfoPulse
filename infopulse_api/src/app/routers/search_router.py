import logging

from common.data_handlers.search_handler import SearchHandler
from fastapi import APIRouter, HTTPException
from models.search import Search

router = APIRouter()
logger = logging.getLogger("uvicorn.error")
search_handler = SearchHandler()


@router.get("", response_model=Search)
async def search(search_query: str):
    try:
        return search_handler.search(search_query)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail=f"Failed to search with error: {e}")


@router.get("/all", response_model=list[Search])
async def get_searches():
    try:
        return search_handler.get_searches()
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail=f"Failed to get searches with error: {e}"
        )


@router.get("/{search_id}", response_model=Search)
async def get_search(search_id: int):
    try:
        return search_handler.get_search(search_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail=f"Failed to get search with error: {e}"
        )


@router.delete("/{search_id}")
async def delete_search(search_id: int):
    try:
        return search_handler.delete_search(search_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail=f"Failed to delete search with error: {e}"
        )
