
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
import random
class VistaAutorizador(Resource):
    def post(self):
        numbers = [1,2]
        token_de_acceso = create_access_token(random.choice(number))
        return {"token":token_de_acceso}
    
    @jwt_required()
    def get(self):
        try:
            return { "Autorizado": True }, 200
        except:
            return { "Autorizado": False }, 401
