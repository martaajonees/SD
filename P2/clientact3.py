import socket

# Crear socket

HOST = 'localhost'
PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#Pregunto al usuario el nombre
data = str(input("¿Cuál es el nombre del archivo? "))

with open(data, "r") as file:
    data = file.read()
    file.close()

s.sendall(data.encode('utf-8'))
print("Archivo enviado")

#Recibe cadena invertida y tamaño
cad = s.recv(1024).decode('utf-8')
size = s.recv(1024).decode('utf-8')

print(f"La cadena invertida es: {cad}")
print(f"El tamaño es: {size}")

#Cierra conexión
s.close()
