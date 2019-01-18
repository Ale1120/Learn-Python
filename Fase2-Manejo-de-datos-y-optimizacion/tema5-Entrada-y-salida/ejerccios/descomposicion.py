# ejerccios 3

import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print('error numero incorrecto')
        print("ejemplo descomposicion.py [0-9999] ")

    else:
        caracteres = str(numero)
        long = len(caracteres)
        for i in range(long):
            caracter = int(caracteres[long-1-i]) * 10 ** i
            print('{:04d}'.format(caracter))

else:
    print('error sobrepaso el maximo de argumento permitidos')
    print("ejemplo descomposicion.py [0-9999] ")
