"""
Implemente la función dict_add(mydict, t) para que añada la tupla
(clave, valor) t pasada por parámetro al diccionario mydict.
Por ejemplo, la invocación dict_add({1: 'manzana'}, {2, 'fresa'})}
deberá devolver como resultado {1: 'manzana', 2: 'fresa'}.
Se deberán generar las siguientes excepciones en caso de ser necesario:
■ TypeError si el elemento t es nulo (None) o no es una tupla de dos elementos.
"""

def dict_add(mydict, t):
    if t is None:
        raise ValueError('El elemento t es Nulo')
    if not isinstance(t, tuple) or len(t) != 2:
        raise TypeError('El elemento t no es una tupla de dos elementos')
    key, value = t
    mydict[key] = value

if __name__ == "__main__":
    mydict = {1: 'manzana'}
    mytuple = (2, 'fresa')
    dict_add(mydict, mytuple)
    t = (3, 'melocotón')
    dict_add(mydict, t)
    print(mydict)