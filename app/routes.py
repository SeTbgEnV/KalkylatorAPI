from flask import request
from flask_restx import Resource
from .controller import CalculatorService
from .routes import api, calculation_model, result_model

@api.route("/calculate")
class Calculate(Resource):
    @api.expect(calculation_model)
    @api.marshal_with(result_model)
    def post(self):
        payload = request.get_json()
        a = payload.get("a")
        b = payload.get("b")
        op = payload.get("operation")

        if a is None or b is None or op is None:
            return {"error": "Missing required fields"}, 400

        try:
            return CalculatorService.calculate(a, b, op)
        except ZeroDivisionError as e:
            return {"error": str(e)}, 400
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception:
            return {"error": "Server error"}, 500