class Pelicula(object):
    # Constructor de la classe
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

    # Destructor de la clase
    def __del__ (self):
        print('Se esta borrando la pelicula',self.titulo)

    # redefinimos el metodo string
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)

    # Redefinimos el Metodo length
    def __len__(self):
        return self.duracion

pelicula = Pelicula("El padrino", 175,1972)
str(pelicula) # usando string
len(pelicula) # usando length
