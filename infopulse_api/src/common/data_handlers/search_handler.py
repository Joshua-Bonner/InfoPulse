import logging
import os
from datetime import date, timedelta

from common.helpers.search_helper import url_to_unique_int
from dotenv import load_dotenv
from models.search import Search
from newsapi import NewsApiClient

load_dotenv()

logger = logging.getLogger("uvicorn.error")
api_key = os.getenv("NEWS_API_KEY")

today = date.today()
yesterday = today - timedelta(days=1)
default_query: dict = {
    "q": "",
    ##"from_param": yesterday.strftime("%Y-%m-%d"),
    ##"to": today.strftime("%Y-%m-%d"),
    "language": "en",
    ##"sort_by": "popularity",
}


class SearchHandler:

    def __init__(self):
        logger.info("Initializing SearchHandler")
        self.news_api = NewsApiClient(api_key=api_key)

    def search(self, search_query: str):
        logger.info(f"Searching for {search_query}")
        default_query["q"] = search_query
        response = self.news_api.get_everything(**default_query)
        for article in response["articles"]:
            article["id"] = url_to_unique_int(article["url"])
        return Search(
            id=response["articles"][0]["id"],
            query=search_query,
            articles=response["articles"],
        )
