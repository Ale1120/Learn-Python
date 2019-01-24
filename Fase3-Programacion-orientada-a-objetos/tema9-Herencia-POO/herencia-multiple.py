# herencia multiple tienen prioridad las herencia mas a la izquierda si tienen
# metodos iguales
class A:
    def __init__(self):
        print("soy clase A")

    def a(sefl):
        print("Este metodo lo heredo de A")

class B:
    def __init__(self):
        print("soy clase b")
    def b(sefl):
        print("Este metodo lo heredo de B")

class C(A,B):
    def c(sefl):
        print("Este metodo es de C")

c =C()
c.a()
c.b()
c.c()
