# ejerccios1

def area_rectangulo(b,a):
    return b*a
print(area_rectangulo(15,10))

# ejerccios 2
import math
def area_circulo(r):
    retrun (r**2)* math.pi

print(area_circulo(5))

# ejerccio 3

def relaccion(a,b):
    if a > b:
        return 1
    elif a < b :
        return -1
    else:
        return 0

print(relaccion(5,10))
print(relaccion(10,5))
print(relaccion(5,5))

# ejerccios 4

def intermedio(a,b):
    return (a+b)/2

print(intermedio(5,5))

#ejerccios 5
 def recortar(numero,minimo,maximo):
     if numero < minimo:
         return minimo
     elif numero > maximo:
        return maximo
     else:
        return numero

print(recortar(15,0,10))

# ejerccio 6
lista = [-12,84,13,20,-33,101,9]
def separar(numeros):
    numeros.sort()
    pares = []
    impares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

pares,impares =separar(lista)
print(pares)
print(impares)
