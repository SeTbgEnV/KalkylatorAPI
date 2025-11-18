from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    # Extract input values
    a = data.get("a")
    b = data.get("b")
    operation = data.get("operation")

    # Validate input
    if a is None or b is None or operation not in ["+", "-", "*", "/"]:
        return jsonify({"message": "Invalid input"}), 400

    # Perform calculation
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            return jsonify({"message": "Division by zero"}), 400
        result = a / b

    # Return result
    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(debug=True)
