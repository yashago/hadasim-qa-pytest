import pytest
from ..ProjectB.tests import product_service


def test_returns_title_when_dependency_succeeds(monkeypatch):
    # def moked_fetch_product(product_id):
    #     return {"id": product_id, "title": "Keyboard"}
    
    monkeypatch.setattr(
        product_service, "fetch_product", lambda product_id: {"id": product_id, "title": "Keyboard"}
    )
    # OR
    # monkeypatch.setattr(product_service, "fetch_product", moked_fetch_product)
    assert product_service.get_product_name(1) == "Keyboard"


@pytest.mark.parametrize(
    "product",
    [
        pytest.param({"id": 1}, id="no-title-key"),
        pytest.param({"id": 1, "title": ""}, id="empty-title"),
        pytest.param({"id": 1, "title": None}, id="none-title"),
    ],
)
def test_missing_title_raises_value_error(monkeypatch, product):
    monkeypatch.setattr(product_service, "fetch_product", lambda product_id: product)
    with pytest.raises(ValueError, match="Product title is missing"):
        product_service.get_product_name(1)


def test_dependency_timeout_is_propagated(monkeypatch):
    def fake_fetch(product_id):
        raise TimeoutError("Request timed out")

    monkeypatch.setattr(product_service, "fetch_product", fake_fetch)
    with pytest.raises(TimeoutError, match="Request timed out"):
        product_service.get_product_name(1)


def test_dependency_called_with_requested_id(monkeypatch):
    calls = []

    def fake_fetch(product_id):
        calls.append(product_id)
        return {"id": product_id, "title": "Keyboard"}

    monkeypatch.setattr(product_service, "fetch_product", fake_fetch)
    product_service.get_product_name(42)
    assert calls == [42]
