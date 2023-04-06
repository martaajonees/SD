"""
Haga un script en Python que cree una copia de un fichero cualquiera.
Puede implementar una función propia o utilizar una existente.
A continuación, utilice la librería/módulo necesario para comprobar
que los ficheros anteriores son iguales.
"""
import filecmp

print("Introduzca el nombre del archivo: ")
fich = input()

with open(fich, "r") as file:
    with open("copia.txt", 'w') as copia:
        copia.write(file.read())

if filecmp.cmp(fich, "copia.txt"):
    print('Los ficheros son iguales')
else:
    print('Los ficheros no son iguales')