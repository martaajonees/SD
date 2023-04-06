import socket
import os
# Crear socket

HOST = 'localhost'
PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

try:
    while True:
        c, addr = s.accept()
        #Recibe nombre archivo .jpg
        name = c.recv(1024).decode('utf-8')
        #Compruebo que exista
        if os.path.isfile(name):
            print("El archivo existe")
            #Enviar el fichero al cliente
            with open(name, "r") as file:
                contenido = file.read()
                file.close()
            c.sendall(contenido.encode('utf-8'))
except FileNotFoundError:
    print("El archivo no existe")

c.close()



