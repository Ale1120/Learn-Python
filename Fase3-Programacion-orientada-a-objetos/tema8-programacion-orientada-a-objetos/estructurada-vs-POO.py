# estructurada
clientes = [
    {'Nombre':'Alejandro', 'Apellido':'Ortegano','CI':'1516628'},
    {'Nombre':'Anthony', 'Apellido':'Sanoja','CI':'2216628'}
]

def mostrar_cliente(clientes,ci):
    for cliente in clientes:
        if (ci == cliente['CI']):
            print('{}{}'.formact(cliente['Nombre'],cliente['Apellido']))
            return
    print('Cliente no encontrado')

mostrar_cliente(clientes,'1516628')

def borrar_cliente(clientes,ci):
    for i,c in enumerate(clientes):
        if(ci == c['ci']):
            del(clientes[i])
            print(str()), '> BORRADO'
            return
    print('Cliente no encontrado')
 
