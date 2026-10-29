def test_user_name(user):
    assert user.get("name") == "Alice"


def test_user_is_admin(user):
    assert user.get("role") == "admin"


def test_user_is_active(user):
    assert user.get("active") is True


def test_product_name(product):
    assert product["name"] == "Keyboard"


def test_product_price(product):
    assert product["price"] == 49.99


def test_product_is_in_stock(product):
    assert product["in_stock"] is True
