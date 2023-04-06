"""
Implemente un script en Python, utilizando el módulo os, que liste
todos los ficheros del directorio actual junto a su tamaño en bytes.
Por último, el script mostrará la suma total del tamaño de los ficheros
del directorio. Se deben incluir, además, los ficheros existentes en subdirectorios.
"""

import os

path = '.'
imagenes = os.listdir(path)
size = 0
for imagen in imagenes:
    size = os.stat(imagen).st_size + size
    tuple = (imagen, os.stat(imagen).st_size)
    print(tuple)
print(f'El tamaño total es {size}')
