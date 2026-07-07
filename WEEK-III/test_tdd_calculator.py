import pytest

from tdd_calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5


def test_subtract(calc):
    assert calc.subtract(5, 2) == 3


def test_multiply(calc):
    assert calc.multiply(4, 3) == 12


def test_divide(calc):
    assert calc.divide(10, 2) == 5


def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)


def test_add_negative(calc):
    assert calc.add(-1, -4) == -5


def test_subtract_negative(calc):
    assert calc.subtract(-5, 3) == -8


def test_multiply_zero(calc):
    assert calc.multiply(5, 0) == 0


def test_divide_fraction(calc):
    assert calc.divide(1, 4) == 0.25


def test_multiple_operations(calc):
    assert calc.add(calc.multiply(2, 3), calc.subtract(5, 1)) == 11
