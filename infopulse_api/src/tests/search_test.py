from common.helpers.search_helper import get_article_text, url_to_unique_int


def test_url_to_unique_int():
    url = "https://example.com"
    expected_result = hash(url)
    assert url_to_unique_int(url) == expected_result


def test_get_article_text():
    pass
