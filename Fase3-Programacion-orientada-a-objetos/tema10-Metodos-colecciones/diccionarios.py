#creando diccionario
colores = {"amarillo":"yellow", "azul":"blue", "verde":"green"}
colores['amarillo']

# mostrar elemento
print("mostrar elemento con get()",colores.get('amarillo',"no se encuentra"))

# ver si una keys se  encuentra en el diccionario
"amarillo" in colores

# mostrar keys
print("mostanado las clave de un diccionario keys():",colores.keys())

# mostrar valores
print("mostanado las valores de un diccionario values():",colores.values())

# mostrar keys y values
print("Mostando keys y values en tuplas con item(): ",colores.item())
