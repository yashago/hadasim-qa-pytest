from cart import total

def test_total(cart, product):
    cart.extend(product)
    assert total(cart) == 80