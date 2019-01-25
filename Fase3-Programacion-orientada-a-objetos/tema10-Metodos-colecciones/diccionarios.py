#creando diccionario
colores = {"amarillo":"yellow", "azul":"blue", "verde":"green"}
colores['amarillo']

# mostrar elemento
print("Mostrar elemento con get()",colores.get('amarillo',"no se encuentra"))

# ver si una keys se  encuentra en el diccionario
"amarillo" in colores

# mostrar keys
print("Mostanado las clave de un diccionario keys():",colores.keys())

# mostrar valores
print("Mostanado las valores de un diccionario values():",colores.values())

# mostrar keys y values
print("Mostando keys y values en tuplas con item(): ",colores.item())

# recorrer un diccionario
for clave, valor in colores.item():
    print("El keys {} y el values {} son del diccionario colores!!".format(clave,valor))

# borrar un elemento con su keys
colores.pop("amarillo","no se ha encontrado")
print("El keys que fue eliminado es el amarillo",colores)

# borrar todo el diccionarios
colores.clear()
print("El Diccionario colores esta vacio",colores)
