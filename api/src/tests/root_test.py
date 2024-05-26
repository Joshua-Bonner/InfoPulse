import requests


def test_root():
    response = requests.get("http://localhost:8000")
    print(response.content)
    assert response.status_code == 200
