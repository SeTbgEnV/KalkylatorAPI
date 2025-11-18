from app.service.calculate_service.calculate_service import calculate
import app.service.calculate_service.test.mock as mock
def test_calculate():
    result = calculate(mock.num1, mock.num2, "+")
    assert result["result"] == mock.result_1_2
    assert result["expression"] == mock.result_1_2_expression
    assert isinstance(result["expression"], str) == True
    