import pytest
from app.controller import CalculatorService

def test_addition():
    result = CalculatorService.calculate(2, 3, "+")
    assert result["result"] == 5
    assert result["expression"] == "2 + 3"

def test_subtraction():
    result = CalculatorService.calculate(5, 2, "-")
    assert result["result"] == 3

def test_multiplication():
    result = CalculatorService.calculate(4, 3, "*")
    assert result["result"] == 12

def test_division():
    result = CalculatorService.calculate(10, 2, "/")
    assert result["result"] == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        CalculatorService.calculate(5, 0, "/")

def test_invalid_operator():
    with pytest.raises(ValueError):
        CalculatorService.calculate(5, 3, "%")