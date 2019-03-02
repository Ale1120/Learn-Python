# ejerccios 3
from io import open
import pickle

class Personaje :

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return "{} => {} vida, {} ataque, {} defesa, {} alcance".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)



class Gestor:

    personajes = []

    def __init__(self):
        self.cargar()

    def agregar(self, personaje):
        for per in self.personajes:
            if per.nombre == personaje.nombre:
                return
        self.personajes.append(personaje)
        self.guardar()


    def borrar(self, nombre):
        for per in self.personajes:
            if per.nombre == nombre:
                self.personajes.remove(per)
                self.guardar()
                print("\n Personaje {} borrado".format(nombre))
                return

    def mostrar(self):
        if len(self.personajes) == 0:
            print('El Gestor esta Vacio')
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('personajes.pckl','ab+') # binario y lectura
        fichero.seek(0) # colocar el puntero en el inicio
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("El Gestor Esta Vacio")
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format( len(self.personajes) ))

    def guardar(self):
        fichero = open('personajes.pckl','wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()


gestor = Gestor()
gestor.mostrar()
print("\n")
gestor.agregar( Personaje ("Caballero",4,2,4,2))
gestor.agregar( Personaje ("Guerrero",2,4,2,4))
gestor.agregar( Personaje ("Arquero",2,4,1,8))
gestor.mostrar()
print("\n")
gestor.borrar("Arquero")
gestor.mostrar()
