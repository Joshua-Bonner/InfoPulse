from datetime import date
from typing import List, Optional

from sqlalchemy.sql.schema import Column
from sqlmodel import ARRAY, Field, Relationship, SQLModel, String, UniqueConstraint


class User(SQLModel, table=True):
    __tablename__ = "user"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    username: str
    password: str
    security_question: str
    security_answer: str
    search_pref: Optional["UserSearchPref"] = Relationship(back_populates="user")
    disabled: bool = False


class UserSearchPref(SQLModel, table=True):
    __tablename__ = "user_search_pref"
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id", unique=True)
    search_in: Optional[List[str]] = Field(sa_column=Column(ARRAY(String)))
    search_from: Optional[date] | None = Field(sa_column_kwargs={"nullable": True})
    search_to: Optional[date] | None = Field(sa_column_kwargs={"nullable": True})
    sort_by: Optional[str] | None = Field(sa_column_kwargs={"nullable": True})
    user: Optional[User] = Relationship(back_populates="search_pref")

    __table_args__ = (UniqueConstraint("user_id"),)
