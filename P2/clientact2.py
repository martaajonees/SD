#CLIENTE
import os
import socket

#Establece conexión con el servidor

HOST = 'localhost'
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Enviar nombre
filename = input("Nombre del fichero a enviar")
s.send(filename.encode('utf-8'))

#Espera respuesta de si existe o no el archivo con ese nombre
response = s.recv(1024).decode('utf-8')
if response == 'EXISTE':
    overwrite = input('El archivo ya existe, ¿quiere sobreescribir?')
    if overwrite != 'S':
        s.close()
        exit()

#Enviar fichero

with open(filename, "r") as file:
    data = file.read()
    while data:
        s.send(data)
        data = file.read()

#Esperar a que se notifique la recepción

response = s.recv(1024).decode('utf-8')
print(response)

#Elimina el archivo del directorio
os.remove(filename)

#Cierra conexion
s.close()