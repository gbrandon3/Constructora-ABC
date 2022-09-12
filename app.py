from flask import Flask
from flask_cors import CORS

from flask_restful import Api

from vistas.vistas import VistaGateway
app = Flask('regla')


app_context=app.app_context()
app_context.push()
cors = CORS(app)
api=Api(app)
api.add_resource(VistaGateway,"/gateway/crear")

