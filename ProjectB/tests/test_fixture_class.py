import pytest
import time

@pytest.fixture(scope="class")
def test_user():
    print("\nCreating test user...")
    time.sleep(2)  # Simulate an expensive operation
    return {"id": 101, "name": "Alice"}

class TestUserAPI:

    def test_user_id(self, test_user):
        assert test_user["id"] == 101

    def test_user_name(self, test_user):
        assert test_user["name"] == "Alice"

    def test_user_exists(self, test_user):
        assert test_user is not None