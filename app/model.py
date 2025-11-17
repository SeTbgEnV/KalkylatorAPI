def calculate(a, b, operator):
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/": return a / b
    raise ValueError("Unsupported operator")