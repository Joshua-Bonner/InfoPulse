from pydantic import BaseModel
from typing import List
from .article import Article


class NewsApiResponse(BaseModel):
    status: str
    totalResults: int
    articles: List[Article]
