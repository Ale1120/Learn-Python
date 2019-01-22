# ejerccio 1
try:
    resultado = 10/0
except ZeroDivisionError:
    print('no se puede dividir por cero')

# ejerccio 2
try:
    lista = [1,2,3,4,5]
    lista[10]
except IndexError:
    print('Error el index supera la longuitud de la lista',len(lista))
