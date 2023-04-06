"""
Realizar un script en Python que imprima por pantalla
el directorio de trabajo actual, junto a la lista de
ficheros existentes en dicho directorio.

Posteriormente, el mismo script permitirá al usuario renombrar un fichero.
Para ello solicitará al usuario el nombre del fichero que quiere
renombrar y el nuevo nombre que quiere darle.

Se deben gestionar correctamente las posibles excepciones que puedan
darse en la ejecución del script
"""
import os

try:
    #Imprimir información del directorio

    current = os.getcwd() #Obtener directorio actual
    print(f'Directorio Actual: {current}')

    directorios = os.listdir(current) #Obtener lista de directorios
    for directorio in directorios:
        print(f'-{directorio}')

    #Renombrar

    print('¿Cual es el fichero que quieres renombrar?')
    name = input()

    print(f'¿Cual es el nombre que le quieres poner al fichero {name}?')
    name2 = input()

    os.renames(name, name2)

except FileNotFoundError:
   print('Error: No se encuentra el archivo')

except OSError as e:
    print(f'Error: {e}')




