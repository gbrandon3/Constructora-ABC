from multiprocessing import reduction
from urllib import request
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity


class VistaReglas(Resource):
    
    @jwt_required()
    def post(self):
        request_identity = get_jwt_identity()
        print(request.json)
        if(request_identity == 1):
            return 'Se creo la regla', 200
        else:
            return 'No tiene privilegios para modificar este recurso', 403
        #3
