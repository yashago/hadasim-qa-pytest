
import pytest
import requests

BASE_URL = "https://dummyjson.com/products"


@pytest.mark.parametrize(
    "product_id",
    [
        pytest.param(1, id="first-product"),
        pytest.param(2, id="second-product"),
        pytest.param(3, id="third-product"),
    ],
)
def test_get_product_by_id(product_id):
    # TODO 1: Send a GET request to /products/{product_id}
    response = requests.get(f"{BASE_URL}/{product_id}")
    # TODO 2: Assert that the status code is 200
    assert response.status_code == 200
    # TODO 3: Parse the JSON response
    data = response.json()
    # TODO 4: Assert that the returned ID matches product_id
    assert data.get("id") == product_id
    # TODO 5: Assert that the response contains a title and price
    assert data.get("title")
    assert data.get("price")


@pytest.mark.parametrize(
    "search_term",
    [
        pytest.param("phone", id="search-phone"),
        pytest.param("laptop", id="search-laptop"),
    ],
)
def test_search_products(search_term):
    # TODO: Send GET /products/search with q=search_term
    response = requests.get(f"{BASE_URL}/search?q={search_term}")
    # TODO: Assert status code and response structure
    assert response.status_code is 200
    data = response.json()
    assert isinstance(data.get("products"), list)
    assert isinstance(data.get("products")[0], dict)
    assert data.get("total")
    assert data.get("skip") == 0
    assert data.get("limit")
    # TODO: Verify the search behavior against the API's documented contract
    productsWithSearchTerm = data.get("products")
    for item in productsWithSearchTerm:
        searchable_text = f"{item}".lower()
        assert search_term.lower() in searchable_text, (
            f"'{search_term}' not found in product {item.get('id')}: {item.get('title')}"
        )



@pytest.mark.parametrize(
    "limit, skip",
    [
        pytest.param(1, 0),
        pytest.param(5, 5),
        pytest.param(5, 50)
    ], ids=["one-result", "five-results", "bad-situation"]
)
def test_product_limit(limit, skip):
    # TODO: Send GET /products with the limit query parameter
    response = requests.get(f"{BASE_URL}?limit={limit}&skip={skip}")
    responseData = response.json()
    # TODO: Assert status code
    assert response.status_code == 200
    # TODO: Assert len(response["products"]) <= limit
    assert len(responseData.get("products")) <= limit
    # TODO: Check the response pagination metadata
    assert responseData.get("limit") == limit
    assert responseData.get("skip") == skip
