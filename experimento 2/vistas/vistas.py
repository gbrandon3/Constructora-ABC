<<<<<<< HEAD

from multiprocessing import reduction
=======
from urllib import request
>>>>>>> 48483d9131037c273af012833db732c556a2de00
from flask import request
from flask_restful import Resource
import requests


class VistaGateway(Resource):
    def post(self): 
      
        
        autorizacion=requests.get("https://autorizadorexp.azurewebsites.net/autorizacion",headers={"Authorization":request.headers["Authorization"]})
        print(autorizacion.json()["Autorizado"])
        if(autorizacion.json()["Autorizado"] and autorizacion.status_code==200):
            
            peticion = requests.get(
            "https://experimientoi-apimanagement.azure-api.net/servicio/ubicacion/ubicacion")
       
        
            if(peticion.status_code == 200):
             
                peticion2 = requests.post(
                "https://experimientoi-apimanagement.azure-api.net/servicio/regla/reglas",json=request.json)
            
                if(peticion2.status_code!=200):
                
                    return {"mensaje":"No se creo la regla"},'500'
                else:
                    return {"mensaje":"se creo la regla"},'200'
        else:
            return {"mensaje":"No tienes permiso para realizar esta accion"},'403'
   

