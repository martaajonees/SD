"""
Escriba el código correspondiente a un endpoint de tipo POST con el
framework Bottle en Python.
El nombre del endpoint será /inserta. Como entrada tomará un JSON, en el que se encontrará un número entero cuya clave
será elemento.
El servidor buscará el número indicado en el JSON de entrada en un array denominado mis_elementos, si el elemento no
existe en el array lo insertará en la última posición, en caso contrario, no modificará el array.
Por último, devolverá al cliente, también en formato JSON, el array resultante con la clave mis_elementos.
Si la clave elemento no se encuentra en el JSON de entrada, el servicio deberá devolver un error al cliente.
"""

from bottle import request, post, run  # Librerías para crear el servidor
import json #Librería para procesar JSON


API_ENDPOINT = "https://pastebin.com/api/api_post.php"
API_KEY = "wpIRiX1wGI5wAvVsr5YzZ_1AORY6znFU"

mis_elementos = [1, 2, 3]
@post('/inserta') #Definimos endpoint
def inserta():
    print('Hola')
    try:
        data_json = request.json #Información del json
    except:
        raise ValueError

    elemento = data_json.get('elemento') #info del campo elemento que existe en el json

    if elemento is None: #si no hay elemento en el json devuelvo error
        return json.dumps('error')
    elif elemento in mis_elementos: #si el elemento ya está en mis_elementos devuelvo el vector
        return json.dumps({'mis_elementos': mis_elementos})
    elif elemento not in mis_elementos: #si no está devuelvo lo incluyo y lo devuelvo
        mis_elementos.append(elemento)
        return json.dumps({'mis_elementos': mis_elementos})

run(host='localhost', port=8091) #para que funcione
