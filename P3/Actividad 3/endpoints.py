"""
Desarrolle un servicio web de gestión de habitaciones de un hotel. El servicio debe poseer una lista de habitaciones y cada habitación poseerá, mínimo, los siguientes atributos:
■ Identificador.
■ Número de plazas.
■ Lista de equipamiento (por ejemplo: armario, aire acondicionado, caja fuerte, escritorio, etc.).
■ Ocupada (sí/no).
Se deben implementar los siguientes endpoints:
a) Dardealtaunanuevahabitación.
b) Modificarlosdatosdeunahabitación.
c) Consultarlalistacompletadehabitaciones.
d) Consultarunahabitaciónmedianteidentificador.
e) Consultarlalistadehabitacionesocupadasodesocupadas.
Queda a juicio del estudiante identi car qué tipo de operaciones HTTP debe implementar cada endpoint (PUT, POST o GET).

"""
from bottle import request, post, run, get, put  # Librerías para crear el servidor
import json #Librería para procesar JSON


API_ENDPOINT = "https://pastebin.com/api/api_post.php"
API_KEY = "wpIRiX1wGI5wAvVsr5YzZ_1AORY6znFU"

database = dict()
class Habitaciones :
    def __init__(self, id, numPlazas, Equipamiento, Ocupada):
        self.id = id
        self.numPlazas = numPlazas
        self.Equipamiento = Equipamiento
        self.Ocupada = Ocupada

@post('/addroom')
def addroom():
    data = request.json

    id = data.get('Identificador')
    numPlazas = data.get('Numero de plazas')
    Equipamiento = data.get('Equipamiento')
    Ocupada = data.get('Ocupada')

    #Creacion de la habitación
    Habitacion = Habitaciones(id, numPlazas, Equipamiento, Ocupada)

    #Añadimos a la base de datos
    database[id] = Habitacion

    #Devolvemos json
    dict_json = {'Identificador': id, 'Numero de plazas': numPlazas, 'Equipamiento': Equipamiento, 'Ocupada': Ocupada}

    return json.dumps(dict_json)

@put('/mod_room/<room_id>')
def mod_room(room_id):
    room_id = int(room_id)
    """
    if room_id in database:
        habitacion = database[room_id]
    else:
        raise ValueError
    """
    habitacion = database[room_id]

    if habitacion is None:
        raise ValueError

    new_numPlazas = request.json.get('Numero de plazas')
    habitacion.numPlazas = new_numPlazas
    new_equipamiento = request.json.get('Equipamiento')
    habitacion.Equipamiento = new_equipamiento
    new_Ocupada = request.json.get('Ocupada')
    habitacion.Ocupada = new_Ocupada

    # Devolvemos json
    dict_json = {'Identificador': room_id, 'Numero de plazas': habitacion.numPlazas, 'Equipamiento': habitacion.Equipamiento,
                 'Ocupada': habitacion.Ocupada}

    return json.dumps(dict_json)

@get('/listrooms')
def listrooms():
    habitacion = []
    for iden, value in database.items():
        habitacion.append({'Identificador': iden, 'Numero de plazas': value.numPlazas, 'Equipamiento': value.Equipamiento,
                           'Ocupada': value.Ocupada})
    return json.dumps(habitacion)

@get('/listroom/<room_id>')
def listroom(room_id):
    room_id = int(room_id)
    if room_id in database:
        habitacion = database[room_id]
    else:
        raise ValueError
    dict_json = {'Identificador': room_id, 'Numero de Plazas': habitacion.numPlazas, 'Equipamiento': habitacion.Equipamiento,
                 'Ocupada': habitacion.Ocupada}
    return json.dumps(dict_json)

@get('/liststate/<state>')
def liststate(state):
    habitacion = []
    for ident, value in database.items():
        if value.Ocupada == state:
            habitacion.append({'Identificador': ident, 'Numero de Plazas': value.numPlazas, 'Equipamiento': value.Equipamiento,
                           'Ocupada': value.Ocupada})
    return json.dumps(habitacion)


if __name__ == '__main__':
   run(host='localhost', port=8089, debug=True)
