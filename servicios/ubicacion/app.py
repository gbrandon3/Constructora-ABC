from flask import Flask
from flask_cors import CORS

from flask_restful import Api
from vistas import VistaUbicacion
app = Flask('ubicacion')


app_context=app.app_context()
app_context.push()
cors = CORS(app)
api=Api(app)
api.add_resource(VistaUbicacion,"/ubicacion")