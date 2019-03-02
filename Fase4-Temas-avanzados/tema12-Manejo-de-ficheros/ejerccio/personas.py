# ejerccios 1
from io import open

fichero = open("personas.txt", "r" ,encoding="utf8")
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas:
    campos = linea.replace("\n", "").split(";")
    persona = { "id":campos[0], "nombre":campos[1], "apellido":campos[2], "nacimiento":campos[3] }
    personas.append(persona)

for persona in personas:
    print("(id={}) {} {} => {}".format(persona['id'], persona['nombre'], persona['apellido'], persona['nacimiento']))
