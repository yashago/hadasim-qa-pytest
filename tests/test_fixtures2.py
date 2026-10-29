import pytest

@pytest.fixture(scope="module")
def product():
    return {"name": "Keyboard", "price": 50}
 
def test_product_price(product):
    assert product["price"] == 50
    product["price"] = 40

def test_product_price2(product):
    assert product["price"] == 40

