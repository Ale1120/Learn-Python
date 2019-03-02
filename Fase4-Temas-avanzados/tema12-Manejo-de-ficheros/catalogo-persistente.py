from io import open
import pickle

class Pelicula:

    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha Creado La Pelicula:", self.titulo)

        def __str__(self):
            return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    def __init__(self):
        self.cargar()

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print('El catalogo esta Vacio')
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl','ab+') # binario y lectura
        fichero.seek(0) # colocar el puntero en el inicio
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El Catalogo Esta Vacio")
        finally:
            fichero.close()
            print("Se han cargado {} peliculas".format( len(self.peliculas) ))

    def guardar(self):
        fichero = open('catalogo.pckl','wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()

    # Destructor
    def __del__(self):
        self.guardar() # guardado automatico
        print("Se ha guardado el Catalogo")


catalogo = Catalogo()
# catalogo.mostrar()
catalogo.agregar( Pelicula("El Padrino", 175, 1972))
catalogo.agregar( Pelicula("El Padrino: Parte II", 202, 1974))

del(catalogo)
c = Catalogo()
c.mostrar()
del(c)
