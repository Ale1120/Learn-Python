def resta(a,b):
    return a-b

# por posicion
resta(1,2)

# por asignacion
resta(b=1,a=2)

# valor por defecto  a parametros
def resta(a=None,b=None):
    if a == None or b == None:
        print('argumentos vacio por favor agrege dos argumentos')
    else:
        return a-b

resta()
