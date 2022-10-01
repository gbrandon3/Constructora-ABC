
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
class VistaAutorizador(Resource):
    def post(self):
        token_de_acceso = create_access_token(identity="1090356984")
        return {"token":token_de_acceso}
    
    @jwt_required()
    def get(self):
        try:
            request_identity = get_jwt_identity()
            return { "Autorizado": request_identity == "1090356984" }, 200
        except:
            return { "Autorizado": False }, 401
