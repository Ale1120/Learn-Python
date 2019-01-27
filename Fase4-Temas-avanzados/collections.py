# importando collections
from collections import Counter

# usando Counter para contar elementos de una lista
lista = [1,2,3,4,1,23,1,2,1]
print(lista)
print("Mostrando un contador de numeros en la lista con counter",Counter(lista))

palabra = 'palabra'
print("Mostrando un contador de los caracteres en la lista con counter",Counter(palabra))

# ejemplo de uso de Counter con cadenas
animales = "gato perros canarios perros canarios perro"
c = Counter(animales.split())
print ("Mostrando contador de string con Counter",c)

# elementos mas comunes con most_common(valor)
print("Los elementos mas comues de {} son : ".format(animales),c.most_common())
print("==================================================================================")
# ejemplo de uso
l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)
print(l)
print("El counter nos devuelve un Diccionario (podemos usar sus metodo ) items(): ",c.items())
print("El counter nos devuelve un Diccionario (podemos usar sus metodo ) keys(): ",c.keys())
print("El counter nos devuelve un Diccionario (podemos usar sus metodo ) values(): ",c.values())
print("Sumando la cantidad de elementos : ",sum(c.values()))
print("Transformamos a lista:" ,list(c))
