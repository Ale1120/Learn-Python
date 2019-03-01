# importando pickle mejor libreria para manejar ficheros
import pickle

lista = [1,2,3,4,5]

# creando un fichero de forma binario con wb y extesion pckl
fichero = open('lista.pckl','wb')

pickle.dump(lista, fichero)
