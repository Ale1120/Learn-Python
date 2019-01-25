lista = [1,2,3,4,5]
# agregando un elemento a la lista
lista.append(6)
print(lista)

# agregar un elemento en la posicion desea
l = [5,10,15,25]
l.insert(-1,20)
print(l)

# borrar toda la lista
lista.clear()

# sacar el ultimo
l = [10,20,30,40]
l.pop()
print(l)

# borrar el elemento a como desea por posicion
l.pop(0)
print(l)

# borrar un elemento por su elemento
l.remove(30)
print(l)

# si se repite un elemento borrar el primer elemento
l = [20,40,40,30,40]
l.remove(40)
print(l)

# expandiendo una lista
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)
# contar cuanta veces esta un elemento
["Hola","mundo","mundo"].count("mundo")

# devolver la posicion de una caracter (solo busca el primero en esta en la lista )
["Hola","mundo","mundo"].index("Hola")

# dar la vuelta a una lista
l = [40,30,20,10,0]
l.reverse()
print(l)


# ejemplo de como darle la vuelta a un string

lista = list("Hola Mundo ")
lista.reverse()
cadena = "".join(lista)
print("Esta es una cadena volteada: ",cadena)

# ordenar una lista de menor a mayor
lista = [5,-10,35,0,-65,100]
lista.sort()
print(lista)

# ordenar de mayor a menor
lista = [5,-10,35,0,-65,100]
lista.sort(reverse=True)
print(lista)
