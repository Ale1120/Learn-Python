# para poder abrir ficheros  con io desde un script
from io import open

texto = "Una linea con texto\nOrtra linea con texto"

#creando ficheros open(nombre, tipo)
fichero = open('fichero.txt','w')

# escribiendo dentro de un fichero
fichero.write(texto)
