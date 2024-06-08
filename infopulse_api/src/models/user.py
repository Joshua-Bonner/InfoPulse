from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    username: str
    password: str
    security_question: str
    security_answer: str
    disabled: bool = False
