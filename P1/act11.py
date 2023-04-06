"""
Implemente una función en Python que realice la unión de dos listas.
Tenga en cuenta que no puede haber elementos repetidos
"""

def union(list1, list2):
    lista = list1.copy()
    for j in list2:
        if j not in lista:
            lista.append(j)
    return lista

if __name__ == "__main__":
    l = union([1,2,4], [1,3,4])
    for i in l:
        print(i)