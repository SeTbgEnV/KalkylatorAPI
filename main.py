from flask import Flask, request, jsonify
from app.service.calculate_service.calculate_service import calculate

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate_endpoint():
    data = request.get_json()

    # Extract input values
    a = data.get("a")
    b = data.get("b")
    operation = data.get("operation")

    try:
        result = calculate(a, b, operation)
        return jsonify(result), 200
    except ZeroDivisionError as e:
        return jsonify({"error": str(e)}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except TypeError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
