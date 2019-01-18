# ejerccio 1 coleccion
usuario = {'marta','david','elvira', 'juan', 'marcos'}
admin = {'juan', 'marta'}
# para sacar un elemento de una coleccion
admin.discard('juan')
admin.add('marcos')

for i in usuario:
    if i in admin:
        print(i, 'es admin')
    else:
        print(i,'no es admin')

# ejerccio 2 diccionario

caballero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
guerrero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
arquero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}

caballero['vida'] = guerrero['vida']*2
caballero['defensa'] = guerrero['defensa']*2

guerrero['ataque'] = caballero['ataque']*2
guerrero['alcance'] = caballero['alcance']*2

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa']/2
arquero['alcance'] = guerrero['alcance']*2

print('Caballero:\t', caballero)
print('guerrero:\t', guerrero)
print('arquero:\t', arquero)

# ejerccio 3 cola
from collections import deque

tareas = [
    [6,'Distribucion'],
    [2,'Diseño'],
    [1,'Concepcion'],
    [7,'Mantenimiento'],
    [4,'Produccion'],
    [3,'Planidicacion'],
    [5,'Prueba']
]
print("==Tareas desordenadas==")
for i in tareas:
    print(i[0],i[1])

# ordenar una lista
tareas.sort()
cola =duque()

for i in tareas:
    cola.append(i[1])

print("==Tareas Ordenadas==")
for i in tareas:
    print(i)
