
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

class VistaAutorizador(Resource):
    def post(self):
        token_de_acceso = create_access_token(identity="UsuarioPrueba", additional_claims={"tipo": 2})
        return {"token":token_de_acceso}
        