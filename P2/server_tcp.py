import socket

HOST = 'localhost'
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)
print("Me quedo a la espera")

s_cliente, addr = s.accept()

mensaje = s_cliente.recv(1024)
print(f"Recibido [{mensaje.decode('utf-8')}] del cliente con la direccion {str(addr)}")

s_cliente.send("Hola, cliente soy el servidor".encode('utf-8'))
s_cliente.close()

s.close()