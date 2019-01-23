class Ejemplo:
    __atributo_privado = "soy un atributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("soy un metodo inalcanzable desde afuera")

e = Ejemplo()
e.__atributo_privado
e.__metodo_privado()

# ejemplo con puente para usar metod privados dentro de otro __metodo_privado

class Ejemplo:
    __atributo_privado = "soy un atributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("soy un metodo inalcanzable desde afuera")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()


e = Ejemplo()
e.atributo_publico
e.metodo_publico()
