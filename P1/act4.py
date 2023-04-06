"""
Implemente la función accum(x, y, z) para que devuelva la suma de aquellos
parámetros que incluyan un número par.
Por ejemplo, la invocación accum(5, 4, 2) deberá devolver como resultado 6.
Se deberán generar las siguientes excepciones en caso de ser necesario:
■ TypeError si alguno de los tres argumentos x, y,oznoesunvalor entero.
"""

def accum(x, y, z):
    num = [x, y, z]
    sum = 0
    for n in num:
        if isinstance(n, int):
            if n % 2 == 0:
                sum += n
        else:
            raise TypeError('No es un valor entero')

    return sum

if __name__ == "__main__":
    res = accum(2, 1, 6)
    print(f"La suma es {res}")