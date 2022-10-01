from multiprocessing import reduction
from urllib import request
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class VistaReglas(Resource):
    @jwt_required()
    def post(self):
 
            return 'Se creo la regla',200
        