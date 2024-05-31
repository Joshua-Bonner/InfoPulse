from pydantic import BaseModel


class Source(BaseModel):
    id: str
    name: str


class Article(BaseModel):
    source: Source
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str
