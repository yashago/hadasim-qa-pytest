import pytest
 
@pytest.mark.smoke3
def test_one(shared_value):
    print(f"Shared value fixture: {shared_value}")
    shared_value.append("three")
    assert "three" in shared_value
 
@pytest.mark.smoke3
def test_two(shared_value):
    print(f"Shared value fixture: {shared_value}")
    assert "two" in shared_value
