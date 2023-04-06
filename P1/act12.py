"""
Implemente una función copiar(origen,destino) que copie el contenido
del fichero origen, en el fichero destino (usando open()).
"""

def copiar(origin, dest):
    with open(origin, "r") as file:
        contenido = file.read() #Contenido a copiar
    with open(dest, "w") as destin:
        destin.write(contenido)
    file.close()
    destin.close()

if __name__ == "__main__":
    copiar('hola.txt', 'destino.txt')