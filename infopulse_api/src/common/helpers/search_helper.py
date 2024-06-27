import hashlib

import requests
from bs4 import BeautifulSoup


def url_to_unique_int(url: str) -> int:
    hash_object = hashlib.sha256(url.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig[:16], 16)


def get_article_text(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join([p.text for p in paragraphs[1:-1]])
