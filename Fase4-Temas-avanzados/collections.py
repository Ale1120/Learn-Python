# importando collections
from collections import Counter

# usando Counter para contar elementos de una lista
lista = [1,2,3,4,1,23,1,2,1]
print("Mostrando un contador de numeros en la lista con counter",Counter(lista))

palabra = 'palabra'
print("Mostrando un contador de los caracteres en la lista con counter",Counter(palabra))

# ejemplo de uso de Counter con cadenas
animales = "gato perros canarios perros canarios perro"
c = Counter(animales.split())
print ("Mostrando contador de string con Counter",c)

# elementos mas comunes con most_common(valor)
c.most_common()
