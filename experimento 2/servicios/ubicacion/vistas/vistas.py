from flask_restful import Resource
from flask_jwt_extended import jwt_required
class VistaUbicacion(Resource):
    @jwt_required()
    def get(self):
        return{"ubicacion":{"id":1}}