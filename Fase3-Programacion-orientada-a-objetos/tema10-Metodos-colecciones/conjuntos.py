# creando conjunto vacio
conjunto = set()

# agregando un elemento
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
print("agregandos elementos con add: ",conjunto)

# sacar un elemento del conjunto
conjunto.discard(1)
print("sacando elemento 1 del conjunto: ",conjunto)

# copiar un conjunto en otro
c2 = conjunto.copy()

# borrar todo los elementos
c2.clear()

# comparaciones
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
print("c1:",c1)
print("c2:",c2)
print("c3:",c3)
print("c4:",c4)
print("========================")
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
print("actualizando y union en c1 y c2 :",c1)

# diferencia elemento de conjutos
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
print("los elementos distinto del c1 y c2 son : ",c1.difference(c2))

# diferencia  y actualizar
c1.difference_update(c2)
print("los elementos distintos y actualizando de c1 del c1 y c2 son :",c1)

# elementos comunes devuelve otro conjuto
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
print("elementos comunes en c1 y c2",c1.intersection(c2))

# devuelve los elementos que no concuerda entre dos conjutos
print("Estos sos los elementos que no se repinten en c1 y c2 :"
,c1.symmetric_difference(c2))
