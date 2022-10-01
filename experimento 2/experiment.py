import time
import requests
import random

request = 100
fallos = 0
with open('resultado.txt', 'w') as f:
    for i in range(request):

        error = random.randint(0, 1) == 1
        data = {} if random.randint(0, 1) == 1 else {"accion": "crear"}
        start = time.time()
        request = requests.post("http://127.0.0.1:5000/gateway/crear", json=data)

        end = time.time()
        resul = " Se creo la regla " if request.status_code == 200 else "No se creo la regla"
        if end - start >= 5:
            fallos += 1
        print("Request " + str(i + 1) + resul + ' tiempo: ' + str(end - start) + "\n")
        f.write('tiempo:' + str(end - start) + "\n" + "del request " + str(i + 1) + resul + ' tiempo: ' + str(
            end - start) + "\n")
        time.sleep(1)
print("No cumplio " + str(fallos) + " veces")
