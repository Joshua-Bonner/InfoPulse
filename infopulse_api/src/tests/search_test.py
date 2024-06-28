from common.helpers.search_helper import get_article_text, url_to_unique_int


def test_url_to_unique_int():
    url = "https://www.google.com"
    result = url_to_unique_int(url)
    assert isinstance(result, int)


def test_get_article_text():
    url = "https://www.google.com"
    result = get_article_text(url)
    assert isinstance(result, str)
