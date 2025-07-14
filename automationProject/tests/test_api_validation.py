import requests

def test_api_response():
    resp = requests.get("https://automationexercise.com/api/productsList")
    assert resp.status_code == 200
    assert "products" in resp.json()