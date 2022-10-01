
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token,jwt_required

class VistaAutorizador(Resource):
    def post(self):
        token_de_acceso = create_access_token(identity="1090356984")
        return {"token":token_de_acceso}
    
    @jwt_required()
    def get(self):
        request_identity = get_jwt_identity()
        return { "Autorizado": reques_identity == "1090356984" }, 200
