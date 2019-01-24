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

adorno = Adorno(1245, 'Vaso Adornado',15,'Vaso de porcelana con dibujos')
print(adorno)

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

alimento = Alimento(2035,"Botella de Aceite de Olivar",5,"250 Mil")
alimento.productor="La aceitera"
alimento.distribuidor="polar"
print(alimento)

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

libro = Libro(2036,"Cocina",9,'Recetas sanas y buenas')
libro.codigo = "0-1489631-17-8"
libro.autor = 'Juana'
print(libro)
