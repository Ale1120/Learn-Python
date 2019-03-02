# importando pickle mejor libreria para manejar ficheros
import pickle

lista = [1,2,3,4,5]

# creando un fichero de forma binario con wb y extesion pckl
fichero = open('lista.pckl','wb')

pickle.dump(lista, fichero)

# recuperando el fichero binario
fichero = open('lista.pckl','rb')
lista = pickle.load(fichero)
print("Recuperando el Fichero binario:",lista)
del(lista)

# colocando el puntero en el inicio
fichero.seek(0)
lista = pickle.load(fichero)
print("Recuperando el Fichero binario, despues de borrar la lista:",lista)


# ejemplo con objeto
print("Ejemplo con Clases")
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

nombres = ["Alejandro","Anthony","Osvani"]
personas = []

for n in nombres:
    persona = Persona(n)
    personas.append(persona)

fichero = open('personas.pckl','wb')
pickle.dump(personas, fichero)


# recuperando infomarcion
fichero = open('personas.pckl', 'rb')
personas = pickle.load(fichero)

for persona in personas:
    print(persona)
