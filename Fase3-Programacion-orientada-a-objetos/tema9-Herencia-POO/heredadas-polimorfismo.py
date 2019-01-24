# Herencias
# Super clase
class Producto:
    def __init__(self,referencia,nombre,precio,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}""".format(self.referencia,self.nombre,self.precio,self.descripcion)

# clases hijas
class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = ""
    distribuidor = ""
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia,self.nombre,self.precio,self.descripcion,
self.productor, self.distribuidor)

class Libro(Producto):
    codigo = ""
    autor = ""
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
CODIGO\t\t{}
AUTOR\t\t{}""".format(self.referencia,self.nombre,self.precio,self.descripcion,
self.codigo, self.autor)

adorno = Adorno(1245, 'Vaso Adornado',15,'Vaso de porcelana con dibujos')
alimento = Alimento(2035,"Botella de Aceite de Olivar",5,"250 Mil")
alimento.productor="La aceitera"
alimento.distribuidor="polar"
libro = Libro(2036,"Cocina",9,'Recetas sanas y buenas')
libro.codigo = "0-1489631-17-8"
libro.autor = 'Juana'

# agregando los productos a una lista

productos = [adorno,alimento]
productos.append(libro)

for producto in productos:
    if isinstance(producto,Adorno): # para ver si un objeto tiene una tipo ejemplo
        print(producto.referencia,producto.nombre)
    elif isinstance(producto,Alimento):
        print(producto.referencia,producto.nombre,producto.productor)
    elif isinstance(producto,Libro):
        print(producto.referencia,producto.nombre,producto.codigo)

def rebajar(producto,rebaja):
    """Devuelve un producto con una rebaja """
    producto.precio = producto.precio -(producto.precio/100 * rebaja)
    return producto

rebaja = rebajar(alimento,10)
print(rebaja)

# copia del objeto listas clases y diccionario
 import copy
 copia_adorno = copy.copy(ad)
 print(copia_ad)
