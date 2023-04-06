#SERVIDOR

import socket
import os

# Crear socket

HOST = 'localhost'
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print("El servidor está escuchando")

while True:
    # Espera la solicitud del cliente
    s_cliente, addr = s.accept()

    # Recibir nombre del fichero
    filename = s_cliente.recv(1024).decode('utf-8')
    # Comprueba si ya existe en el fichero
    if os.path.isfile(filename):
        s_cliente.send("EXISTE".encode('utf-8'))
        response = s_cliente.recv(1024).decode('utf-8')
        if response == 'S':
            os.remove(filename)
        else:
            s_cliente.close()
            exit()
    s_cliente.send("NO_EXISTE".encode('utf-8'))

#Recibe fichero
    with open(filename,'w') as file:
        while True:
            data = s_cliente.recv(1024)
            if not data:
                break
            file.write(data)

    s_cliente.send("El archivo se ha enviado correctamente".encode('utf-8'))
    s_cliente.close()


