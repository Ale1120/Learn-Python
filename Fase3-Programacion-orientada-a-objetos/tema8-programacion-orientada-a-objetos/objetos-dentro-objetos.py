class Pelicula(object):
    # Constructor de la classe
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

    def __str__(self):
        return "{} ({})".format(self.titulo,self.lanzamiento)
