lista = [1,2,3,4,5]
# agregando un elemento a la lista
lista.append(6)
print("Agregando el ultimo elemento con append(6) ",lista)

# agregar un elemento en la posicion desea
l = [5,10,15,25]
l.insert(-1,20)
print("Agregando un elemento con insert(-1,20) ",l)

# borrar toda la lista
lista.clear()

# sacar el ultimo
l = [10,20,30,40]
l.pop()
print("Sacando de la lista al ultimo elemento con pop() ",l)

# borrar el elemento a como desea por posicion
l.pop(0)
print("Sacando de la lista un elemento con pop(0) ",l)

# borrar un elemento por su elemento
l.remove(30)
print("Borrando un elemento por el elemento con remove(30)",l)

# si se repite un elemento borrar el primer elemento
l = [20,40,40,30,40]
l.remove(40)
print("""Borrando un elemento por el elemento con remove(40)
pero borra el primero de todos los repetidos """,l)

# expandiendo una lista
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print("Agrenando la lista l1 a la l2 :",l1)

# contar cuanta veces esta un elemento
string = ["Hola","mundo","mundo"].count("mundo")
print("Contar la vesces de un elemento en una lista : ",string)

# devolver la posicion de una caracter (solo busca el primero en esta en la lista )
string=["Hola","mundo","mundo"].index("Hola")
print("Devolver la posicion de un elemento (solo el primero si se repite)", string)

# dar la vuelta a una lista
l = [40,30,20,10,0]
l.reverse()
print("Dando la vuelta a la lista ",l)


# ejemplo de como darle la vuelta a un string
lista = list("Hola Mundo ")
lista.reverse()
cadena = "".join(lista)
print("Esta es una cadena volteada: ",cadena)

# ordenar una lista de menor a mayor
lista = [5,-10,35,0,-65,100]
lista.sort()
print("Ordenando de mayor a menor ",lista)

# ordenar de mayor a menor
lista = [5,-10,35,0,-65,100]
lista.sort(reverse=True)
print("Ordenando de menor a mayor ",lista)
