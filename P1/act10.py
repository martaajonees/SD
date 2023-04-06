"""
Implemente una función en Python que realice la intersección de dos listas.
Tenga en cuenta que no puede haber elementos repetidos.
"""

def intersection(list1, list2):
    list = []
    rep = False
    for i in list1:
        rep = False
        for j in list2:
            if i == j and not rep:
                list.append(i)
                rep = True
    return list


if __name__ == "__main__":
    l = intersection([1, 2, 3], [1, 3 ,6])
    for k in l:
        print(k)