"""
Implemente la función prime(a, b) para que devuelva una lista con los
números primos en el intervalo cerrado [a, b].
Por ejemplo, la invocación prime(2, 10) deberá devolver como
resultado [2, 3, 5, 7]. Se deberán generar las siguientes excepciones en
caso de ser necesario:
■ TypeError si los parámetros a o b no son enteros o son nulos(None).
"""
import math
def prime(a, b):
    i = a
    mylist = []
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("No son enteros")
    if a is None or b is None:
        print("Son nulos")
    while i <= b:
        if pr(i):
            mylist.append(i)
        i = i + 1
    return mylist
def pr(num):
    if num < 2:
        return False
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            return False
    return True

if __name__ == "__main__":
    lista = prime(1, 20)
    for n in lista:
        print(n)
