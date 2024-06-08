from typing import List

from article import Article
from pydantic import BaseModel


class NewsApiResponse(BaseModel):
    status: str
    totalResults: int
    articles: List[Article]
