"""Implemente la función get_file_info(filename) para que devuelva
una tupla con el tamaño en bytes del fichero, cuyo nombre se indica como
parámetro filename, en la primera posición, y una lista con las palabras
acabadas con el carácter 's' que contenga el fichero, en segunda posición.
Por ejemplo, la invocación get_file_info('mifichero.txt'), suponiendo que '
mifichero.txt' contiene el texto “`La casa está pintada en muchos colores'', d
evolverá la tupla (39, ['muchos', 'colores']).
Se deberán generar las siguientes excepciones en caso de ser necesario:
■ TypeError si el parámetro filename no es una cadena o es nulo (None).
■ OSError si el fichero indicado no existe."""

import os
def get_file_info(filename):
    list = []
    size = os.stat(filename).st_size #Tamaño
    if filename is None or not isinstance(filename, str):
        raise TypeError('No es una cadena o es nulo')
    try:
        with open(filename, "r") as file:
            for line in file: #reading each line
                for word in line.split(): #reading each word
                    if word.endswith('s'):
                        list.append(word)
    except FileNotFoundError:
        raise OSError(f'El fichero {filename} no existe')
    file.close()
    tuple = (size,list)

    return tuple



if __name__ == "__main__" :
    res = get_file_info('hola.txt')
    print(res)