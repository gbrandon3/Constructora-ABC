from multiprocessing import reduction
from urllib import request
from flask import request
from flask_restful import Resource


class VistaReglas(Resource):
    def post(self):
        print(request.json)
        if(request.json["accion"]=="error"):
            return 'Error',500
        else:
            return 'Se creo la regla',200
        #3