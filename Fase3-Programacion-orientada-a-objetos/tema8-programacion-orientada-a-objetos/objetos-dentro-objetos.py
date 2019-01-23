class Pelicula:
    # Constructor de la classe
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

    def __str__(self):
        return "{} ({})".format(self.titulo,self.lanzamiento)

class Catalogo:
     peliculas = []

    def __init__(self,peliculas[]):
        self.peiculas = peliculas

    def agregar(self,pelicula):
        self.peliculas.append(peliculas)

    def mostrar(self):
        for pelicula in self.peliculas:
            print(pelicula)


padrino = Pelicula("El padrino", 175,1972)
accion = Catalogo([padrino])
accion.mostrar()
