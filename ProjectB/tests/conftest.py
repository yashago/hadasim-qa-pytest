import pytest

@pytest.fixture(scope="module")
def user():
    print("Env setup")
    data = {
        "name": "Alice",
        "role": "admin",
        "active": True
    }
    yield data
    print("Env teardown")

@pytest.fixture(scope="module")
def product():
    return {
        "name": "Keyboard",
        "price": 49.99,
        "in_stock": True
    }
 
@pytest.fixture
def product():
    return [
        {"name": "Keyboard", "price": 50}, 
        {"name": "Nice keyboard", "price": 30}
    ]
 
@pytest.fixture
def cart():
    return []