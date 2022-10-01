from multiprocessing import reduction
from urllib import request
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from flask_jwt_extended import get_jwt_identity


class VistaReglas(Resource):
    @jwt_required()
    def post(self):
        jwt = get_jwt_identity()

        print(jwt)
        
        return 'Se creo la regla',200
        