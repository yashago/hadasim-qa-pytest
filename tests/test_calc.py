import pytest

from src.calculator import add, divide, modulo, multiply, power, subtract

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 0.5, 3.0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
    (-2, -3, 1),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 100, 0),
    (1.5, 2, 3.0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (7, 2, 3.5),
    (-9, 3, -3),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_float_precision():
    assert divide(1, 3) == pytest.approx(0.3333333)


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)


@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -1, 0.5),
])
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 1),
    (9, 3, 0),
    (-7, 3, 2),
])
def test_modulo(a, b, expected):
    assert modulo(a, b) == expected


def test_modulo_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Cannot take modulo by zero"):
        modulo(5, 0)

def test_modulo_float_precision():
    assert modulo(5.5, 2) == pytest.approx(1.5)