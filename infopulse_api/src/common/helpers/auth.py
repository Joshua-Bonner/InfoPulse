import os
from datetime import datetime, timedelta, timezone

import jwt
from common.data_handlers.user_handler import UserHandler
from dotenv import load_dotenv
from jwt.exceptions import InvalidTokenError
from models.user import User
from passlib.context import CryptContext

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_pwd(pwd, pwd_hash):
    return pwd_context.verify(pwd, pwd_hash)


def get_pwd_hash(pwd):
    return pwd_context.hash(pwd)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except InvalidTokenError:
        return None


async def authenticate_user(username: str, password: str) -> User | bool:
    user: User = await UserHandler.get_user_by_username(username)
    if not user:
        return False
    if not verify_pwd(password, user.password):
        return False
    return user
