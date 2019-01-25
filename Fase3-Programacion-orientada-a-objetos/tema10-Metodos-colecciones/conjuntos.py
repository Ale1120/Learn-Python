# creando conjunto vacio
conjunto = set()

# agregando un elemento
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
print("agregandos elementos con add: ",conjunto)

# sacar un elemento del conjunto
conjunto.discard(1)
print("sacando elemento 1 del conjunto:"conjunto)

# copiar un conjunto en otro
c2 = conjunto.copy()

# borrar todo los elementos
c2.clear()

# comparaciones
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

# para saber si un conjunto es disnto a otro conjunto (elementos)
c1.isdisjoint(c3)

# subconjutos
c1.issubset(c4)

# es un super conjunto o contenedor
c4.issuperset(c1)

# union de dos conjuntos
print("union de c1 con c2",c1.union(c2))
# actualizando el conjuto con union
c1.update(c2)
