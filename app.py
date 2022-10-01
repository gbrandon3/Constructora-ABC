
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from datetime import timedelta

from vistas.vistas import VistaAutorizador
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config['PROPAGATE_EXCEPTIONS'] = True


app_context = app.app_context()
app_context.push()
cors = CORS(app)

api = Api(app)

api.add_resource(VistaAutorizador,"/autorizacion")

jwt = JWTManager(app)
