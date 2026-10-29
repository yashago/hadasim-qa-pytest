import pytest

@pytest.fixture(autouse=False)
def myfixture():
    print("This fixture is running")

def test_test1():
    print(f"Test 1 got fixture")

def test_test2():
    print(f"Test 2 is running")