# ejerccios Herencia

class Vehiculo():

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format(self.color,
        self.velocidad ,self.ruedas, self.cilindrada)

coche = Coche("azul",150,4,1200)
print(coche)

# llamando el metodo de la clase
class Vehiculo():

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ",km/h, {} ruedas, {} cc".
        format(self.velocidad,self.cilindrada)

coche = Coche("azul",150,4,1200)
print(coche)

# usando super() para ahorrar codigo
# llamando el metodo de la clase para no usar el self
class Vehiculo():

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ",km/h, {} ruedas, {} cc".
        format(self.velocidad,self.cilindrada)

coche = Coche("azul",150,4,1200)
print(coche)
