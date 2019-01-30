# para poder abrir ficheros  con io desde un script
from io import open

texto = "Una linea con texto\nOtra linea con texto"

# #creando ficheros open(nombre, tipo) de escritura
# fichero = open('fichero.txt','w')
#
# # escribiendo dentro de un fichero
# fichero.write(texto)

# crear un fichero de modo lectura
fichero = open('fichero.txt','r')

# pasando contenido al fichero de modo lectura
texto = fichero.read()
print(texto)
