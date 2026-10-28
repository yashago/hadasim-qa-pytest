
import math

import pytest


def add(a, b):
    return a + b


def test_positive_test_sum():
    result = add(0.1, 0.2)
    assert result == pytest.approx(0.3, abs=1e-6)

def test_sqrt():
    assert math.sqrt(4) == 2

@pytest.mark.jacob
@pytest.mark.negatives
def test_sqrt2():
    with pytest.raises(ValueError):
        math.sqrt(-9)