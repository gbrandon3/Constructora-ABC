import json
from flask import request
from flask_restful import Resource
import requests


class VistaGateway(Resource):
    def post(self): 
      
        try:
            autorizacion=requests.get("https://autorizadorexp.azurewebsites.net/autorizacion",headers={"Authorization":request.headers["Authorization"]})
            print(autorizacion.json()["Autorizado"])
            if(autorizacion.json()["Autorizado"] and autorizacion.status_code==200):
            
                peticion = requests.get(
            "https://experimientoi-apimanagement.azure-api.net/servicio/ubicacion/ubicacion")
       
        
                if(peticion.status_code == 200):
             
                    peticion2 = requests.post(
                "https://experimientoi-apimanagement.azure-api.net/servicio/regla/regla",json=request.json,headers={"Authorization":request.headers["Authorization"]})
            
                    if(peticion2.status_code!=200):
                
                        return {"mensaje":"No tienes privilegios para crear la regla"},403
                    else:
                        return {"mensaje":"se creo la regla"},200 
            else:
                return {"mensaje":"No tienes permiso para realizar esta accion"},403
        except Exception as e:
               return {"mensaje":"No tienes permiso para realizar esta accion"},403
        else:
            return {"mensaje":"No tienes permiso para realizar esta accion"},403

class VistaGatewayAutorizador(Resource):
    def post(self): 
        requestAuth=requests.post("https://autorizadorexp.azurewebsites.net/autorizacion",json=request.json)
        return requestAuth.json(),401 if requestAuth.status_code==401 else 200