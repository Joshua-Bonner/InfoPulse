from sqlmodel import SQLModel


class Token(SQLModel, table=False):
    token: str | None = None
    token_type: str | None = None
    username: str
