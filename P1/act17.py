"""
Realizar un script en Python que combine todos los cheros de texto (.txt)
existentes en el directorio de trabajo actual en un único chero de texto,
llamado “union.txt”.

Tanto los ficheros con una extensión distinta, como los que se encuentren
en subdirectorios, deberán ignorarse
"""

import os

path = '.'

content = os.listdir(path)

with open('union.txt', "w") as new:
    for file in content:
        if file.endswith('.txt'):
            with open(file) as f:
                for line in f:
                    new.write(line)
                new.write("\n")
