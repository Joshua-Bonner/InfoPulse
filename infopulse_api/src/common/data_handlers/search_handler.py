import logging
import os
from datetime import date, timedelta

from common.helpers.es_client import ESClient
from common.helpers.search_helper import get_article_text, url_to_unique_int
from dotenv import load_dotenv
from models.search import Search
from newsapi import NewsApiClient

load_dotenv()

logger = logging.getLogger("uvicorn.error")
api_key = os.getenv("NEWS_API_KEY")
search_index = "search"

today = date.today()
yesterday = today - timedelta(days=1)
default_query: dict = {
    "q": "",
    "from_param": yesterday.strftime("%Y-%m-%d"),
    "to": today.strftime("%Y-%m-%d"),
    "language": "en",
    "sort_by": "popularity",
}


class SearchHandler:

    def __init__(self):
        logger.info("Initializing SearchHandler")
        self.news_api = NewsApiClient(api_key=api_key)
        self.es_client = ESClient()

    def search(self, search_query: str):
        logger.info(f"Searching for {search_query}")
        default_query["q"] = search_query
        response = self.news_api.get_everything(**default_query)
        articles = response["articles"][:10]
        for article in articles:
            article["id"] = url_to_unique_int(article["url"])
            article["content"] = get_article_text(article["url"])
        new_search: Search = Search(
            id=response["articles"][0]["id"],
            query=search_query,
            articles=articles,
        )
        self.es_client.insert_doc(
            search_index, id=new_search.id, doc=new_search.model_dump()
        )
        return new_search

    def get_search(self, search_id: int):
        search = self.es_client.get_doc(search_index, search_id)
        return Search(**search["_source"])

    def get_searches(self):
        logger.info("Getting all searches")
        searches = self.es_client.search(search_index, {"query": {"match_all": {}}})
        return [Search(**search["_source"]) for search in searches["hits"]["hits"]]

    def delete_search(self, search_id: int):
        return self.es_client.delete_doc(search_index, search_id)
