# ejerccios 1 Punto

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x,self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} permenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} permenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} permenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} permenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self,punto):
        print("El vector entre {} y {} es ({},{})".format(self,punto, punto.x - self.x, punto.y - self.y))

    def distancia(self,punto):
        # sqrt es la raiz cuadrada
        distancia = math.sqrt( (punto.x - self.z)**2 + (punto.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(self,punto,distancia))




A = Punto (2,3)
B = Punto (5,5)
C = Punto (-3,-1)
D = Punto (0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)
