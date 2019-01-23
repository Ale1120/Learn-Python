class Ejemplo:
    __atributo_privado = "soy un atributo inalcanzable desde afuera"

    def __metodo_privado(self):
        print("soy un metodo inalcanzable desde afuera")

e = Ejemplo()
e.__atributo_privado
e.__metodo_privado()
