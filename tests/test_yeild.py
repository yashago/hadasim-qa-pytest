import json
import urllib.error
import urllib.request

import pytest

from src.car_api import create_api_server, remove_api_server


def get_json(url):
    with urllib.request.urlopen(url) as response:
        return json.load(response)


@pytest.fixture(scope="module")
def api_server():
    print("\nSETUP: Creating API server")
    server_url = create_api_server()
    print(f"SETUP: API server running at {server_url}")
    yield server_url
    remove_api_server(server_url)
    print("\nTEARDOWN: Removing API server")


def test_get_all_cars(api_server):
    cars = get_json(f"{api_server}/cars")
    print(f"GET /cars returned: {cars}")
    assert len(cars) == 3


def test_get_car_by_license_id(api_server):
    car = get_json(f"{api_server}/cars/ABC123")
    assert car == {"licenseId": "ABC123", "manufacturer": "Toyota", "modelYear": 2020}


def test_get_unknown_car_returns_404(api_server):
    with pytest.raises(urllib.error.HTTPError) as exc_info:
        get_json(f"{api_server}/cars/122345")
    assert exc_info.value.code == 404
