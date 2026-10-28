
import pytest


@pytest.fixture
def user():
    """Provide a sample user for tests."""
    return {
        "id": 101,
        "name": "Alice",
        "role": "admin",
        "active": True,
    }


@pytest.fixture
def product():
    """Provide a sample product for tests."""
    return {
        "id": 501,
        "name": "Keyboard",
        "price": 49.99,
        "in_stock": True,
    }


import pytest


@pytest.fixture(scope="session")
def shared_value():
    """One list shared by every test in the session."""
    print("CREATING FIXTURE")
    return []


@pytest.fixture
def product_catalog():
    """Provide reusable product data."""
    return {
        "keyboard": {
            "id": 1,
            "name": "Keyboard",
            "price": 100.0,
        },
        "mouse": {
            "id": 2,
            "name": "Mouse",
            "price": 50.0,
        },
        "monitor": {
            "id": 3,
            "name": "Monitor",
            "price": 500.0,
        },
    }


@pytest.fixture
def cart():
    """Create an empty cart for each test."""
    print("\nSetup: Creating an empty cart")

    shopping_cart = []

    yield shopping_cart

    print("Teardown: Clearing the cart")
    shopping_cart.clear()


@pytest.fixture
def populated_cart(cart, product_catalog):
    """Create a cart containing two keyboards and one mouse."""

    cart.append({
        "product": product_catalog["keyboard"],
        "quantity": 2,
    })

    cart.append({
        "product": product_catalog["mouse"],
        "quantity": 1,
    })

    return cart
