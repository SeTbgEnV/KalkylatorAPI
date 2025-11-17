class CalculatorService:

    @staticmethod
    def calculate(a: float, b: float, operator: str) -> dict:
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = a / b
        else:
            raise ValueError(f"Invalid operator '{operator}'")

        return {
            "result": result,
            "expression": f"{a} {operator} {b}"
        }