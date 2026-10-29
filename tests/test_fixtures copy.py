import pytest
 
@pytest.fixture(scope="module")
def shared_value():
    print("CREATING FIXTURE")
    return []
 
def test_one(shared_value):
    shared_value.append("one")
    assert "one" in shared_value
 
def test_two(shared_value):
    assert "one" in shared_value
