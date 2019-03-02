# Ejerccios 2
from io import open
import sys

fichero = open('contador.txt', 'a+')
fichero.seek(0)
contenido = fichero.readline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)

fichero.close()

# Transformar texto a numero

try:
    contador = int(contenido)

    # en funcion de lo que el  usuario quiera
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -=1

    print(contador)

    # Escribir cambios en fichero
    fichero = open("contador.txt", "W")
    fichero.write( str(contador) )
    ficher.close()
except:
    print("Error: Fichero corrupto.")
