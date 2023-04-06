"""
Realice un script en Python que mueva al directorio actual, todos
los archivos contenidos en subdirectorios del mismo.
Tenga en cuenta que un directorio puede contener a su vez otros
directorios y que la longitud en la jerarquía del árbol no está
denida y por tanto, el script debe funcionar para todos los casos.
"""
import os
import shutil

current = os.getcwd() #Obtener directorio actual

for root, dirs, files in os.walk(current):
    for file in files:
        path = os.path.join(root, file) # Obtener ruta completa
        shutil.move(path, current)
