import socket

#Crear socket

HOST = 'localhost'
PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Enviar nombre archivo .jpg

name = str(input("¿Cuál es el nombre del archivo? "))
s.sendall(name.encode('utf-8'))

#Recibe contenido imagen

image = s.recv(1024).decode('utf-8')
print("Imagen recibida")

s.close()