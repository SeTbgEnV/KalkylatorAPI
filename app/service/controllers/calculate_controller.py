from flask import Blueprint, request, jsonify
from app.service.calculate_service.calculate_service import calculate

# Create a Blueprint
calculate_bp = Blueprint("calculate", __name__)

@calculate_bp.route("/calculate", methods=["POST"])
def calculate_endpoint():
    data = request.get_json()

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