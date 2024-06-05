from common.helpers.db_client import DatabaseClient
from models.user import User
from sqlmodel import select


class UserHandler:
    def __init__(self):
        self.db_client = DatabaseClient()

    def create_user(self, user: User):
        with self.db_client.get_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def get_user_by_id(self, id: int):
        with self.db_client.get_session() as session:
            user = session.get(User, id)
            return user

    def get_user_by_username(self, username: str):
        with self.db_client.get_session() as session:
            statement = select(User).where(User.username == username)
            user = session.exec(statement).first()
            return user

    def update_user(self, id: int, user: User):
        with self.db_client.get_session() as session:
            user = session.get(user, id)
            if user is None:
                return None
            user_data = user.model_dump()
            for key, value in user_data.items():
                setattr(user, key, value)
            session.commit()
            session.refresh(user)
            return user

    def delete_user(self, id: int):
        with self.db_client.get_session() as session:
            user = session.get(User, id)
            if user is None:
                return None
            session.delete(user)
            session.commit()
            return user
