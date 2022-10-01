import time
import requests
import random

request = 100
fallos = 0
with open('resultado.txt', 'w') as f:
    for i in range(request):
        requestAutorizador=requests.post("http://127.0.0.1:5000/gateway/autorizar")
        print("Tiene acceso")
        
        