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
    print('Error el index supera la longuitud de la lista. su longuitud es ',len(lista))

# ejerccio 3
try:
    colores = {'rojo':'red','verde':'green','negro':'black'}
    color['blanco']
except KeyError:
    print("Error:la key no se encuntra en el diccionario")

# ejerccio 4
try:
    r = 15 + '20'
except: TypeError:
    print("Error: Solo se puede sumar datos del mismo tipo, por favor transformar a numeros o string")

# ejerccio 5
elementos = [1,5,-2]

def agregar(lista,elem):
    try:
        if elem in lista:
            raise ValueError
        else:
            lista.append(elem)
    except ValueError:
        print("Error: imposible anadir elementos duplicados => {}".format(elem))

agregar(elementos,10)
agregar(elementos,-2)
agregar(elementos,"hola")
