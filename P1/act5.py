"""
Implemente la función list_add(mylist, e) para que añada el elemento e
a la lista mylist y devuelva la lista resultante. Por ejemplo,
la invocación de list_add([5, 2], 4) deberá devolver como resultado [5, 2, 4].
Se deberán generar las siguientes excepciones en caso de ser necesario:
■ TypeError si el elemento e es nulo(None)
"""

def list_add(mylist, e):
    mylist.append(e)
    if e is None:
        raise ValueError("El elemento es nulo")
    return mylist

if __name__ == "__main__":
    mylist = [2, 1, 3]
    e = 9
    mylist = list_add(mylist, e)
    for el in mylist:
        print(el)