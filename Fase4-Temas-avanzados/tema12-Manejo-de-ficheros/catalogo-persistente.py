from io import open
import pickle

class Pelicula:

    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha Creado La Pelicula:", self.titulo)

        def __str__(self):
            retunr '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar(self):
        for pelicula in self.peliculas:
            print(pelicula)
