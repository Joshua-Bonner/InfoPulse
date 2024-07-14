import logging
from typing import Optional

from common.data_handlers.user_handler import UserHandler
from common.helpers.auth import decode_access_token, get_pwd_hash
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models.user import User, UserSearchPref

router = APIRouter()
logger = logging.getLogger("uvicorn.error")
user_handler = UserHandler()


@router.post("")
async def create_user(user: User):
    try:
        user.password = get_pwd_hash(user.password)
        user_handler.create_user(user)
        return JSONResponse(status_code=200, content={"message": "User created"})
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to create user")


@router.get("/current_user", response_model=User)
async def get_current_user_endpoint(token: str):
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        user = user_handler.get_user_by_username(username)
        if user is None:
            return JSONResponse(status_code=404, content={"message": "User not found"})
        return user
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to get current user")


@router.get("/search_prefs/{username}", response_model=UserSearchPref)
async def get_user_search_prefs(username: str):
    try:
        user_search_prefs = user_handler.get_user_search_prefs(username)
        if user_search_prefs is None:
            return JSONResponse(status_code=404, content={"message": "User not found"})
        return user_search_prefs
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to get user search preferences"
        )


@router.post("/search_prefs")
async def create_user_search_prefs(user_search_pref: UserSearchPref):
    try:
        user_handler.create_user_search_pref(user_search_pref)
        return JSONResponse(
            status_code=200, content={"message": "User search preferences created"}
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to create user search preferences"
        )


@router.put("/search_prefs/{id}")
async def update_user_search_prefs(id: int, user_search_pref: UserSearchPref):
    try:
        user_search_pref = user_handler.update_user_search_pref(id, user_search_pref)
        if user_search_pref is None:
            return JSONResponse(
                status_code=404,
                content={"message": "User search preferences not found"},
            )
        return JSONResponse(
            status_code=200, content={"message": "User search preferences updated"}
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=400, detail="Failed to update user search preferences"
        )


@router.delete("/{id}")
async def delete_user(id: int):
    try:
        user_handler.delete_user(id)
        return JSONResponse(status_code=200, content={"message": "User deleted"})
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=400, detail="Failed to delete user")
