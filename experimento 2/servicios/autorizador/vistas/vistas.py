from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
import random
class VistaAutorizador(Resource):

    def post(self):
        if(request.json["usuario"]=="usuarioPrueba"  or request.json["usuario"]=="usuarioPrueba2" and request.json["password"]=="pass"):
            if(request.json["usuario"]=="usuarioPrueba" and request.json["ip"]=="141.250.247.54"):
                token_de_acceso = create_access_token(1)
                return {"token":token_de_acceso}
            elif(request.json["usuario"]=="usuarioPrueba2" ):
                token_de_acceso = create_access_token(2)
                return {"token":token_de_acceso}
            else:
                return {"mensaje":"Acceso denegado"},401
        else:
            return {"mensaje":"Acceso denegado"},401
    @jwt_required()
    def get(self):
        try:
            return { "Autorizado": True }, 200
        except:
            return { "Autorizado": False }, 401