import contextlib
import os

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseClient(metaclass=SingletonMeta):
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)

    @contextlib.contextmanager
    def get_session(self):
        session = Session(bind=self.engine)
        try:
            yield session
        finally:
            session.close()

    def create_all(self):
        SQLModel.metadata.create_all(self.engine)
