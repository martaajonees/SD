import socket

# Crear socket

HOST = 'localhost'
PORT = 1025

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))
s.listen(1)

#while True:
c, addr = s.accept()
# Recibo datos del fichero
data = str(c.recv(1024).decode('utf-8'))
print("Archivo entregado")

# Lo Invierto
inv = data[::-1]
size = str(len(inv))

c.sendall(inv.encode('utf-8'))
c.sendall(size.encode('utf-8'))

c.close()
s.close()
