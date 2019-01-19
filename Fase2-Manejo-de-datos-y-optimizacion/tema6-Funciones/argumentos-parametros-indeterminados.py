# *args se genera una tupla
def indeterminados_posicion(*args):
    for i in args:
        print(arg)

indeterminados_posicion(5,'hola',[1,2])

# **kwargs genera un diccionario
def indeterminados_posicion( **kwargs):
    for i in kwargs:
        print(kwargs,'',kwargs[i])

indeterminados_posicion(n=5,c='hola',l=[1,2])
