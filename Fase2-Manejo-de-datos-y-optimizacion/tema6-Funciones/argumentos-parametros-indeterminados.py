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

# ejemplo
def super_funcion(*args, **kwargs):
    t=0
    for i in args:
        t+=i
    print('el total de indeterminados es:',t)
    for j in kwargs:
        print(j,'',kwargs[j])

super_funcion(10,50,-1,1.56,10,20,300,nombre='Alejandro',edad=23)
