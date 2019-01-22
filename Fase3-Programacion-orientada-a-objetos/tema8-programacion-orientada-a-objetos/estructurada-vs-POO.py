# estructurada
clientes = [
    {'Nombre':'Alejandro', 'Apellido':'Ortegano','ci':'1516628'},
    {'Nombre':'Anthony', 'Apellido':'Sanoja','ci':'2216628'}
]

def mostrar_cliente(clientes,ci):
    for cliente in clientes:
        if (ci == cliente['ci']):
            print('{} {}'.format(cliente['Nombre'],cliente['Apellido']))
            return
    print('Cliente no encontrado')

mostrar_cliente(clientes,'1516628')

def borrar_cliente(clientes,ci):
    for i,c in enumerate(clientes):
        if(ci == c['ci']):
            del(clientes[i])
            print(str(c), '> BORRADO')
            return
    print('Cliente no encontrado')

borrar_cliente(clientes,'2216628')

# POO

class Cliente:
    def __init__(self,ci,nombre,apellido):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)

class Empresa:
    def __init__(self,clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self,ci=None):
        for cliente in self.clientes:
            if cliente.ci == ci:
                print(cliente)
                return
        print('Cliente no encontrado')

    def borrar_cliente(self,ci=None):
        for i,c in enumerate(self.clientes):
            if c.ci == ci:
                del(self.clientes[i])
                print(str(c), '> BORRADO')
                return
        print('Cliente no encontrado')
