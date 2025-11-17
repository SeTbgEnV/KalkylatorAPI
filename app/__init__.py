from flask import Flask
from flask_restx import Api
from .routes import api as kalklykator_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='Kalkylator API')

    api.add_namespace(kalklykator_ns, path='/calculate')

    return app