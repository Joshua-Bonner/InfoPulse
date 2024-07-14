import logging
import os
from datetime import timedelta
from typing import Annotated

from common.data_handlers.user_handler import UserHandler
from common.helpers.auth import authenticate_user, create_access_token, verify_pwd
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.token import Token
from models.user import User

load_dotenv()

router = APIRouter()
logger = logging.getLogger("uvicorn.error")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
user_handler = UserHandler()

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

EXPIRES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user: User = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise credentials_exception
    if not verify_pwd(form_data.password, user.password):
        raise credentials_exception
    token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=int(EXPIRES)),
    )
    return Token(token=token, token_type="bearer", username=user.username)
