import socket
import os
import shutil

#Crear socket

HOST = 'localhost'

PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

dir, addr = s.recvfrom(1024)
print(dir.decode('utf-8'))



#Recibir un comando

comando = ""

while comando != 'exit':
    comando, addr = s.recvfrom(1024)
    comando = comando.decode('utf-8')

    if comando == 'ls':
        contenido = str(os.listdir())
        s.sendto(contenido.encode('utf-8'), addr)

    else:

        if comando.split(' ')[0] == 'rm':
            while True:
                archivo = comando.split(' ')[1]
                os.remove(archivo)
                s.sendto("¿Se ha hecho correctamente?".encode('utf-8'), addr)
                res, addr = s.recvfrom(1024)
                res = res.decode('utf-8')
                if res == 'si' or res == 'Si':
                    break

        elif comando.split(' ')[0] == 'write':
            while True:
                archivo = comando.split(' ')[1]
                mensaje = comando.split(' ')[2]
                with open(archivo, "w") as file:
                    file.write(mensaje)
                    file.close()
                s.sendto("¿Se ha hecho correctamente?".encode('utf-8'), addr)
                res, addr = s.recvfrom(1024)
                res = res.decode('utf-8')
                if res == 'si' or res == 'Si':
                    break

        elif comando.split(' ')[0] == 'cd':
            directorio = comando.split(' ')[1]
            os.chdir(directorio)
            s.sendto("¿Se ha hecho correctamente?".encode('utf-8'), addr)
            res, addr = s.recvfrom(1024)
            res = res.decode('utf-8')
            if res == 'si' or res == 'Si':
                break

        elif comando.split(' ')[0] == 'mv':
            origen = comando.split(' ')[1]
            destino = comando.split(' ')[2]
            shutil.move(origen, destino)
            s.sendto("¿Se ha hecho correctamente?".encode('utf-8'), addr)
            res, addr = s.recvfrom(1024)
            res = res.decode('utf-8')
            if res == 'si' or res == 'Si':
                break
s.close()