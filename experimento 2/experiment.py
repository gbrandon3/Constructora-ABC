import re
import time
import requests
import random

request = 10
fallos = 0
ataques=[{"usuario":"usuarioPrueba","password":"pass","ip":"141.250.247.54"},{"usuario":"usuarioPrueba2","password":"pass","ip":"141.250.247.54"},{"usuario":"usuarioPrueba","password":"pass","ip":"141.250.247.50"}]
with open('resultado.txt', 'w') as f:
    for i in range(request):
        ataque=random.choice(ataques)
        print(ataque)
        requestAutorizador=requests.post("http://127.0.0.1:5000/gateway/autorizar",json=ataque)
        print(requestAutorizador.json())
        if(requestAutorizador.status_code==200):
            requestCrearRegla=requests.post("http://127.0.0.1:5000/gateway/crear",headers={"Authorization":"Bearer "+requestAutorizador.json()["token"]})
            print(requestCrearRegla.json()["mensaje"])
        elif requestAutorizador.status_code==401:
            print("Acceso denegado")
        else:
            print(requestCrearRegla.json()["mensaje"])

        time.sleep(1)
        
        