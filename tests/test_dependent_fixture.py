import pytest

@pytest.fixture
def user():
    print("Creating user")
    return {"id": 7, "name": "Ari"}


@pytest.fixture
def authenticated_client(user):
    print("Creating authenticated client")
    return {
        "user": user,
        "token": "test-token",
    }


@pytest.fixture
def profile_page(user):
    print("Creating profile page")
    return {
        "username": user.get("name"),
        "url": f"/users/{user.get('id')}",
    }


def test_user_profile(authenticated_client, profile_page):
    assert authenticated_client["user"]["name"] == "Ari"
    assert profile_page.get("username") == "Ari"
    assert profile_page.get("url") == "/users/7"