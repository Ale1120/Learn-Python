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
for clave,valor in colores.items():
    print(clave,valor)

#ejemplo de uso de diccionario
personajes = []
p = {'nombre':'gandalf','clase':'Mago','raza':'humano'}
personajes.append(p)
p = {'nombre':'legolas','clase':'picaro','raza':'elfo'}
personajes.append(p)
p = {'nombre':'gimli','clase':'guerrero','raza':'enano'}
personajes.append(p)
personajes

for p in personajes:
    print(p['nombre'],p['clase'],p['raza'])
