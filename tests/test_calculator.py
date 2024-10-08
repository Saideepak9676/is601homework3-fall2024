from calculator import Calculator
import pytest

def test_add():
    assert Calculator.add(3, 2) == 5

def test_subtract():
    assert Calculator.subtract(5, 2) == 3

def test_multiply():
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    assert Calculator.divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)