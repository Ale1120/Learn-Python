# ejerccios Herencia

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
        return super().__str__() + ", {} km/h ruedas, {} cc".format(self.velocidad,self.cilindrada)

class Camioneta(Coche):

    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de cargas".format(self.carga)

class Bicicleta(Vehiculo):

    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {} ".format(self.tipo)

class Motocicleta(Bicicleta):

    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h {} cc".format(self.velocidad,self.cilindrada)

vehiculos = [
    Coche("Azul",4,150,1200),
    Camioneta("Blanco",4,100,1300,1500),
    Bicicleta("Verde",2,"urbana"),
    Motocicleta("negro",2,"deportiva",180,900)
]

# def catalogar(vehiculos):
#     for vehiculo in vehiculos:
#         print("{} {}".format( type(vehiculo).__name__, vehiculo ))
#
# catalogar(vehiculos)

def catalogar(vehiculos, ruedas=None):
    if ruedas != None:
        contador = 0
        for vehiculo in vehiculos:
            contador += 1

        print("Se ha encontrado {} vehiculos con {} ruedas".format(contador,ruedas))
        print("=============================================")

    for vehiculo in vehiculos:
        if ruedas == None:
            print("{} {}".format( type(vehiculo).__name__, vehiculo ))
        elif vehiculo.ruedas == ruedas:
            print("{} {}".format( type(vehiculo).__name__, vehiculo ))

catalogar(vehiculos,2)
