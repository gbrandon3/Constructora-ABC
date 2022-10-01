from flask_restful import Resource
<<<<<<< HEAD
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
=======
from flask_jwt_extended import create_access_token, jwt_required


>>>>>>> 48483d9131037c273af012833db732c556a2de00
class VistaAutorizador(Resource):

    def post(self):
        token_de_acceso = create_access_token(identity="1090356984")
<<<<<<< HEAD
        return {"token":token_de_acceso}
    
    @jwt_required()
    def get(self):
        request_identity = get_jwt_identity()
        return { "Autorizado": request_identity == "1090356984" }, 200
=======
        return {"token": token_de_acceso}

    @jwt_required()
    def get(self):
        return {"Autorizado": True}
>>>>>>> 48483d9131037c273af012833db732c556a2de00
