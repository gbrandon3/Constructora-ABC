from flask import Flask
from flask_cors import CORS

from flask_restful import Api
from vistas import VistaReglas
app = Flask('regla')


app_context=app.app_context()
app_context.push()
cors = CORS(app)
api=Api(app)
api.add_resource(VistaReglas,"/reglas")

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)