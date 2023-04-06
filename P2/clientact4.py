import socket

#Crear socket

HOST = 'localhost'

PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Recibe mensaje inicial

bienvenido = s.recv(1024).decode('utf-8')
print(bienvenido)

#Enviar nombre

name = str(input())
s.send(name.encode('utf-8'))

#Recibe respuesta
mensaje = s.recv(1024).decode('utf-8')
print(mensaje)

#Envía respuesta
respuesta = str(input())
s.sendall(respuesta.encode('utf-8'))

#Recibe contacto
while respuesta != 'exit':
    contacto = s.recv(1024).decode('utf-8')
    print(contacto)
    print(mensaje)
    respuesta = str(input())
    s.sendall(respuesta.encode('utf-8'))

s.close()