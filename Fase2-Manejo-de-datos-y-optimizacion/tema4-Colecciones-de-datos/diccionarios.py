# dicionario color{clave:valor}
colores = {'amarillo':'yellow', 'azul':'blue', 'verde':'green' }

color['amarillo']

# modificando un elemento
colores['amarillo']= 'white'

# borrar un elemento clave:valor
del(colores['amarillo'])

# recorrer un diccionario completo
for clave in colores:
    print(clave,colores[clave])

# recorriendo un diccionario de manera optima
for clave,valor in edades.items():
    print(clave,valor)
