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
