import pytest;

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def test_add_two_positive_numbers():
    result = add(2, 3)
    print("You don't see me, but I'm here")
    assert result == 5

def test_subtract_two_positive_numbers():
    result = subtract(5, 3)
    print("You don't see me, but I'm here")
    assert result == 2

def test_my_function():
    result = add(10, 5)
    print("You don't see me, but I'm here")
    assert result == 15

def test_my_function_with_negative_numbers():
    result = subtract(-5, -3)
    print("You don't see me, but I'm here")
    assert result == -2

@pytest.mark.fire
def test_abc():
    result = add(1, 1)
    print("You don't see me, but I'm here")
    assert result == 2

@pytest.mark.smoke
def test_def():
    result = subtract(10, 5)
    print("You don't see me, but I'm here")
    assert result == 5