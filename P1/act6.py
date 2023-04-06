"""
Implemente la función list_del(mylist, e) para que elimine la primera
ocurrencia del elemento e de la lista mylist y devuelva la lista resultante.
Por ejemplo, la invocación list_del([5, 2, 4], 2)
deberá devolver como resultado [5, 4].
Se deberán generar las siguientes excepciones en caso de ser necesario:
■ TypeError si el elemento e es nulo (None) o la lista mylist está vacía.
"""

def list_del(mylist, e):
    borrar = False
    if e is None:
        raise ValueError('El elemento e es nulo')
    if not mylist:
        raise TypeError('La lista está vacía')

    for i in mylist:
        if i is e and borrar is False:
            mylist.remove(i)
            borrar = True
    return mylist

if __name__ == "__main__":
    lista = list_del([5, 4, 3], 4)
    for i in lista:
        print(i)