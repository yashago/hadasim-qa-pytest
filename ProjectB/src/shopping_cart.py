import os

def add_to_cart(cart, product, quantity=1):
    """Add a product to the cart with the specified quantity."""
    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    cart.append({
        "product": product,
        "quantity": quantity,
    })

def get_currency():
    return os.getenv("CURRENCY", "ILS")


def calculate_total(cart):
    """Calculate the total price of all items in the cart."""
    return sum(
        item["product"]["price"] * item["quantity"]
        for item in cart
    )


def clear_cart(cart):
    """Remove all items from the cart."""
    cart.clear()
