import os

def get_api_url():
    envApiUrl = os.getenv("API_URL", "http://localhost:8000")
    print(f"API_URL: {envApiUrl}")
    return envApiUrl

def test_get_default_api_url():
    assert get_api_url() == "http://localhost:8000"

def test_get_api_url(monkeypatch):
    monkeypatch.setenv("API_URL", "https://test.example.com")
    assert get_api_url() == "https://test.example.com"