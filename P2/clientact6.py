import socket

#Crear socket

HOST = 'localhost'

PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (HOST, PORT)
s.sendto("Soy el cliente".encode('utf-8'), addr)

#Enviar el comando


while True:
    # Enviar el comando
    comando = str(input("Indique un comando: "))
    s.sendto(comando.encode('utf-8'), addr)

    #Recibir contenido
    contenido, addrv = s.recvfrom(1024)
    print(contenido.decode('utf-8'))
    #Correctamente
    if comando != 'ls':
        res, addr = s.recvfrom(1024)
        print(res.decode('utf-8'))
    if comando == 'exit':
        break

s.close()
exit()