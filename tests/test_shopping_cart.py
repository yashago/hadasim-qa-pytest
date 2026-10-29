
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.shopping_cart import (
    add_to_cart, # type: ignore
    calculate_total, # pyright: ignore[reportUnknownVariableType]
    clear_cart, # pyright: ignore[reportUnknownVariableType]
)


def test_cart_starts_empty(cart):
    assert cart == []


def test_add_product_to_cart(cart, product_catalog):
    add_to_cart(cart, product_catalog["keyboard"])

    assert len(cart) == 1
    assert cart[0]["product"]["name"] == "Keyboard"
    assert cart[0]["quantity"] == 1


def test_add_product_with_quantity(cart, product_catalog):
    add_to_cart(cart, product_catalog["keyboard"], quantity=3)

    assert len(cart) == 1
    assert cart[0]["quantity"] == 3
    assert calculate_total(cart) == pytest.approx(300.0)


def test_calculate_total(populated_cart):
    assert calculate_total(populated_cart) == pytest.approx(250.0)


def test_clear_cart(populated_cart):
    assert len(populated_cart) == 2

    clear_cart(populated_cart)

    assert populated_cart == []


def test_cart_is_isolated(cart, product_catalog):
    # Each test receives a fresh cart.
    assert cart == []

    add_to_cart(cart, product_catalog["mouse"])

    assert calculate_total(cart) == pytest.approx(50.0)


def test_zero_quantity_is_rejected(cart, product_catalog):
    with pytest.raises(ValueError, match="Quantity must be positive"):
        add_to_cart(cart, product_catalog["keyboard"], quantity=0)


def test_negative_quantity_is_rejected(cart, product_catalog):
    with pytest.raises(ValueError, match="Quantity must be positive"):
        add_to_cart(cart, product_catalog["keyboard"], quantity=-1)


def test_currency_from_environment(monkeypatch):
    monkeypatch.setenv("CURRENCY", "EUR")

    from src.shopping_cart import get_currency  # pyright: ignore[reportAttributeAccessIssue, reportUnknownVariableType]

    assert get_currency() == "EUR"

@pytest.mark.skipif(sys.platform == "win32", reason="This test is skipped on Windows")
def test_save_cart_summary(tmp_path, populated_cart):
    summary_file = tmp_path / "cart_summary.txt"

    total = calculate_total(populated_cart)
    summary_file.write_text(
        f"Cart total: {total:.2f} ILS",
        encoding="utf-8",
    )

    assert summary_file.exists()
    assert summary_file.read_text(encoding="utf-8") == (
        "Cart total: 250.00 ILS"
    )
