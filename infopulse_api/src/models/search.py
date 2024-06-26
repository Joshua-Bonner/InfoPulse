from typing import List

from models.article import Article
from pydantic import BaseModel


class Search(BaseModel):
    id: int
    query: str
    articles: List[Article]
