from flask import Flask
from app.service.controllers.calculate_controller import calculate_bp

app = Flask(__name__)

app.register_blueprint(calculate_bp)

if __name__ == "__main__":
    app.run(debug=True)