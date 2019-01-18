import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print('error sobrepaso el maximo de argumento permitidos')
    print("ejemplo script.py 'hola' 5")
