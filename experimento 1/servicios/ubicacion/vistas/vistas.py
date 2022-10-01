from flask_restful import Resource

class VistaUbicacion(Resource):
    def get(self):
        return{"ubicacion":{"id":1}}