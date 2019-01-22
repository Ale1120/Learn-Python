class Galleta:
    pass

galleta = Galleta()

galleta.sabor = 'Salado'
galleta.color = 'Marron'

print('El sabor de una galleta es ', galleta.sabor)

class Galleta:
    chocolate = False

galleta = Galleta()
g.chocolate


class Galleta:
    chocolate = False

    def __init__ (self):
        print('Se acaba de crear una galleta')

galleta = Galleta()
galleta.chocolate

# ejemplo

class Galleta:
    chocolate = False

    def __init__ (self):
        print('Se acaba de crear una galleta')

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate:
            print('soy una galleta con chocolate')
        else:
            print('soy una galleta sin chocolate')
galleta = Galleta()
galleta.tiene_chocolate()
galleta.chocolatear()
galleta.tiene_chocolate()
galleta.chocolate

class Galleta:
    chocolate = False

    def __init__ (self,sabor,forma):
        self.sabor = sabor
        self.forma = forma
        print('Se acaba de crear una galleta {} {}'.format(sabor,forma))

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate:
            print('soy una galleta con chocolate')
        else:
            print('soy una galleta sin chocolate')

galleta('salada','redonda')

class Galleta:
    chocolate = False

    def __init__ (self,sabor=None, forma=None):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print('Se acaba de crear una galleta {} {}'.format(sabor,forma))

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate:
            print('soy una galleta con chocolate')
        else:
            print('soy una galleta sin chocolate')
