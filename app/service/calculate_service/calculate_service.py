def calculate(a: float, b: float, operator: str) -> dict:
    """
        Performs a calculation based on the given operator.
        
        @param a: First number
        @param b: Second number
        @param operator: A string representing the operation ("+", "-", "*", "/")
        @return: A dictionary with the result and the expression as a string
    """
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