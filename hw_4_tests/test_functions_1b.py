import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(4, 8) == 12


def test_subtract():
    assert Calculator.subtract(12, 8) == 4


def test_multiply():
    assert Calculator.multiply(3, 3) == 9


def test_divide():
    assert Calculator.divide(9, 3) == 3
    with pytest.raises(ValueError):
        Calculator.divide(9, 0)


if __name__ == '__main__':
    pytest.main()
