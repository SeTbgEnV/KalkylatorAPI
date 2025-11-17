from app import create_app
import yaml
from flask import jsonify

app = create_app()

with open("contract/calculator-openapi.yaml") as f:
    openapi_spec = yaml.safe_load(f)

    @app.route("/openapi")
    def openapi():
     return jsonify(openapi_spec)
    
app.run(debug=True)