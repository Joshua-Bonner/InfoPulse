from pydantic import BaseModel


class Source(BaseModel):
    id: str | None
    name: str | None


class Article(BaseModel):
    id: int
    source: Source | None
    author: str | None
    title: str | None
    description: str | None
    url: str | None
    urlToImage: str | None
    publishedAt: str | None
    content: str | None
