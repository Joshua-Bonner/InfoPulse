import hashlib

import requests
from bs4 import BeautifulSoup
from common.data_handlers.user_handler import UserHandler
from models.user import UserSearchPref

user_handler = UserHandler()


def url_to_unique_int(url: str) -> int:
    hash_object = hashlib.sha256(url.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig[:10], 16)


def get_article_text(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join([p.text for p in paragraphs[1:-1]])


def construct_query(search_query: str):
    search_pref: UserSearchPref = user_handler.get_user_search_prefs("test")
    return {
        "q": search_query,
        "from_param": search_pref.search_from.strftime("%Y-%m-%d"),
        "to": search_pref.search_to.strftime("%Y-%m-%d"),
        "language": "en",
        "sort_by": search_pref.sort_by,
    }
