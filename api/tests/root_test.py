import requests


def test_root():
    response = requests.get("http://localhost:8000")
    assert response.status_code == 200
