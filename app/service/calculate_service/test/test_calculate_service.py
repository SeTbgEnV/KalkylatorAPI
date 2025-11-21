import pytest
from app.service.calculate_service.calculate_service import calculate
import app.service.calculate_service.test.mock as mock

"""correct error test example"""
def test_fail_calculate():
    with pytest.raises(TypeError):
        calculate(mock.num12, mock.num13, "+")

def test_calculate():
    """Test the calculate function with various operations and edge cases."""
    result = calculate(mock.num1, mock.num2, "+")
    assert result["result"] == mock.result_1_2
    assert result["expression"] == mock.result_1_2_expression
    assert isinstance(result["expression"], str) == True

def test_subtraction():
    """Test subtraction operation."""
    result = calculate(mock.num3, mock.num4, "-")
    assert result["result"] == mock.result_3_4_subtraction
    assert result["expression"] == mock.result_3_4_subtraction_expression
    assert isinstance(result["expression"], str) == True

def test_multiplication():
    """Test multiplication operation."""
    result = calculate(mock.num5, mock.num6, "*")
    assert result["result"] == mock.result_5_6_multiplication
    assert result["expression"] == mock.result_5_6_multiplication_expression
    assert isinstance(result["expression"], str) == True

def test_division():
    """Test division operation."""
    result = calculate(mock.num7, mock.num8, "/")
    assert result["result"] == mock.result_7_8_division
    assert result["expression"] == mock.result_7_8_division_expression
    assert isinstance(result["expression"], str) == True

def test_divide_by_zero():
    """Test division by zero error."""
    with pytest.raises(ZeroDivisionError):
        calculate(mock.num1, 0, "/")
    
def test_invalid_operator():
    """Test invalid operator error."""
    with pytest.raises(ValueError):
        calculate(mock.num1, mock.num2, "%")

def test_valid_operators():
    """Test that all valid operators work without raising errors."""
    valid_operators = ["+", "-", "*", "/"]
    
    for operator in valid_operators:
        result = calculate(mock.num1, mock.num2, operator)
        assert "error" not in result
        assert "result" in result
        assert isinstance(result["expression"], str) == True