#argumentos por referencia (lista,coleciones tuplas, diccionarios)
# su valor general

def doble_valor(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns =[50,100,200]
doble_valor(ns)
ns

# truco para referencia lista[:] hacemso una copia

def doble_valor(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns =[50,100,200]
doble_valor(ns[:])
ns
