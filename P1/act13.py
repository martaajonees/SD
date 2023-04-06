"""
Imprima por pantalla el listado de directorios de inicio de los usuarios
que hay en el sistema (p. ej., /home/root , /home/osboxes, . . . ).
Pista: hay un fichero con esta información.
También existe una función muy interesante en Python llamada split,
que convierte de string a lista.
"""

with open('/etc/passwd', "r") as file:
    for line in file:
        l = line.split(':')
        if len(l)>=6:
            home = l[5]
            print(home)
