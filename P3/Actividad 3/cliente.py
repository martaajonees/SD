
# Importamos el módulo requests para hacer las solicitudes HTTP
import requests

URL = "http://localhost:8089"
res = 0
while res != 6:
    print('\nElige que opción deseas realizar:\n'
              '1. Dar de alta una nueva habitación\n'
              '2. Modificar los datos de una habitación\n'
              '3. Consultar la lista completa de habitaciones.\n'
              '4. Consultar una habitación mediante identicador.\n'
              '5. Consultar la lista de habitaciones ocupadas o desocupadas.\n'
              '6. Salir')
    res = int(input())
    if res == 1:
        id = int(input('Introduza el id: '))
        numPlaza = int(input('Numero de Plaza: '))
        Equipamiento = input('Lista de equipamiento: ').split(',')
        Ocupada = ' '
        while Ocupada != 'SI' and Ocupada != 'NO':
            Ocupada = input("Introduce si está ocupada o no: ")

        response = requests.post(URL + '/addroom', json={'Identificador': id, 'Numero de plazas': numPlaza, 'Equipamiento': Equipamiento,
                                      'Ocupada': Ocupada})

        print(response.text)
    elif res == 2:
        room_id = int(input('Introduza el id: '))
        numPlaza = int(input('Numero de Plaza: '))
        Equipamiento = input('Lista de equipamiento: ')
        Ocupada = input("Introduce si está ocupada o no: ")
        response = requests.put(URL + '/mod_room/' + str(room_id),
                                json={'identificador': room_id, 'Numero de plazas': numPlaza, 'Equipamiento': Equipamiento,
                                      'Ocupada': Ocupada})
        print(response.text)
    elif res == 3:
        response = requests.get(URL + '/listrooms')
        print(response.text)
    elif res == 4:
        room_id = int(input('Introduza el id: '))
        response = requests.get(URL + '/listroom/' + str(room_id), json={'identificador': room_id})
        print(response.text)
    elif res == 5:
        state = ' '
        while state != 'SI' and state != 'NO':
            state = input('Introduzca si está o no ocupada (SI/NO): ')
            if state != 'SI' and state != 'NO':
                print('Ponga SI o NO')
            else:
                response = requests.get(URL + '/liststate/' + state, json={'Ocupada': state})
                print(response.text)
exit()

if __name__ == '__main__':
    main()
