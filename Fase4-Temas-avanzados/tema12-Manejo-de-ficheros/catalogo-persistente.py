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
        for pelicula in self.peliculas:
            print(pelicula)

    def cargar(self):
        fichero = open('catalogo.pckl','ab+') # binario y lectura
        fichero.seek(0) # colocar el puntero en el inicio
        try:
            sefl.peliculas = pickle.load(fichero)
        except:
            print("El Catalogo Esta Vacio")
        finally:
            fichero.close()
            print("Se han cargado {} peliculas".format( len(self.peliculas) ))

    def guardar(self):
        fichero = open('catalogo.pckl','wb')
        pickle.dump(self.peliculas,fichero)
        fichero.close()

    # Destructor
    def __del__(self):
        self.guardar() # guardado automatico


c = Catalogo()
