from multiprocessing import reduction
from urllib import request
from flask import request
from flask_restful import Resource
import requests
import json
import time
import random
class VistaGateway(Resource):
    def post(self):
    
        
        peticion = requests.get(
            "https://experimientoi-apimanagement.azure-api.net/servicio/ubicacion/ubicacion")
       
        
        if(peticion.status_code == 200):
             
            peticion2 = requests.post(
                "https://experimientoi-apimanagement.azure-api.net/servicio/regla/reglas",json=request.json)
            
        return {"mensaje":"se creo la regla"},'200'
            
             
          

                
        

        
