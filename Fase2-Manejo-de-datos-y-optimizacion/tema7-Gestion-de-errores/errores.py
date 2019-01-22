print('hola'

pint('hola')

# errores semanticos
lista = [1,2,3]
l.pop()
l.pop()
l.pop()
l.pop()

# comprovar
lista = [1,2,3]
if len(lista) > 0:
    lista.pop()

# error simanticos
numero = input('agregue un numero:')
numero2 = 4
print("{}/{}={}".format(numero,numero2,numero/numero2))


# solucion
numero = float(input('agregue un numero: '))
numero2 = 4
print("{}/{}={}".format(numero,numero2,numero/numero2))
