import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(4, 8) == 12
    assert Calculator.add(15, 10) == 25
    assert Calculator.add(0.0, 0.1) == 0.1
    assert Calculator.add("2", "9") == "29"
    assert Calculator.add(-15, -4) == -19
    assert Calculator.add(10, 10) != 22


def test_add_negative():
    with pytest.raises(TypeError):
        Calculator.add(6, None)
        Calculator.add([], 48)
        Calculator.add("15", 7)


def test_subtract():
    assert Calculator.subtract(12, 8) == 4
    assert Calculator.subtract(5, 14) == -9
    assert Calculator.subtract(-15, -10) == -5
    assert Calculator.subtract(5.75, 1.75) == 4.00
    assert Calculator.subtract(4, 2) != 3


def test_subtract_negative():
    with pytest.raises(TypeError):
        Calculator.subtract(6, "2")
        Calculator.subtract("7", "15")
        Calculator.subtract(6, None)
        Calculator.subtract([], 48)


def test_multiply():
    assert Calculator.multiply(3, 3) == 9
    assert Calculator.multiply(-9, 2) == -18
    assert Calculator.multiply(0.15, 0) == 0
    assert Calculator.multiply("6", 3) == "666"
    assert Calculator.multiply(0.7, 0.5) == 0.35
    assert Calculator.multiply(5, 5) != 52


def test_multiply_negative():
    with pytest.raises(TypeError):
        Calculator.multiply(None, 15)
        Calculator.multiply([15], [2])


def test_divide():
    assert Calculator.divide(9, 3) == 3
    assert Calculator.divide(-12, -2) == 6
    assert Calculator.divide(-15, 3) == -5
    assert Calculator.divide(0.35, 0.7) == 0.5
    assert Calculator.divide(9, 3) != 4


def test_divide_negative():
    with pytest.raises(ValueError):
        Calculator.divide(15, 0)
        Calculator.divide(-15, 0)
        Calculator.divide(0.15, 0)
        Calculator.divide(15, 0.0)

    with pytest.raises(TypeError):
        Calculator.divide(15, None)
        Calculator.divide("15", "3")
        Calculator.divide(15, "3")
        Calculator.divide(15, "z")


if __name__ == '__main__':
    pytest.main()
