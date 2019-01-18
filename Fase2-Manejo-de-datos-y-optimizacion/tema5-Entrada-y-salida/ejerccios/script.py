# ejerccios 2 crear una tabla
import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print('error Filas o columnas incorrecto')
        print("ejemplo script.py [1-9] [1-9]")
    else:
        for i in range(filas):
            print('')
            for j in range(columnas):
                print('*', end="")
else:
    print('error sobrepaso el maximo de argumento permitidos')
    print("ejemplo script.py [1-9] [1-9]")
