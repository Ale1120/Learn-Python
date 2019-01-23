class Producto:
    def __init__(self,referencia,tipo,nombre,precio,descripcion,
    productor=None, distribuidor=None,codigo=None,autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.precio = precio
        self.descripcion = descripcion
        self.productor = productor
        self.codigo = codigo
        self.autor = autor

adorno = Producto('00A','ADORNO', 'Vaso Adornado',15,'Vaso de porcelana con dibujos')
