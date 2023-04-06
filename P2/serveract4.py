import socket

#Crear socket

HOST = 'localhost'

PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("Me quedo a la espera")

while True:
    #Aceptar
    c, addr = s.accept()
    c.sendall("¡Bienvenido! ¿Cuál es su nombre para que pueda dirigirme a usted?".encode('utf-8'))
    #Recibe nombre
    name = c.recv(1024).decode('utf-8')
    print("Recibido")
    c.sendall(f"{name}, ¿en qué puedo ayudarle?".encode('utf-8'))
    print("Enviado")
    #Recibe respuesta

    respuesta = c.recv(1024).decode('utf-8')
    while respuesta != "exit":
        c.sendall("Debe ponerse en contacto con el servicio de atención de dudas cuya dirección es dudas@ejemplo.com".encode('utf-8'))
        respuesta = c.recv(1024).decode('utf-8')
    c.close()
    exit()
