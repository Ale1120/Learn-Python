# ejerccios 3
import random
import math

def leer_numeros(ini, fin, mensajes):

    while True:
        try:
            valor = int( input(mensajes))
        except:
            print("Error: numero no valido")
        else:
            if valor >= ini and valor <= fin:
                break
    return valor

def generador():
    numeros = leer_numeros(1, 20, "Cuantos numeros quieres generar [1-20]: ")
    modo = leer_numeros(1, 3, "Como quieres redondear los numeros [1] al Alza [2] a la baja [3] Normal: ")

    lista = []

    for decimal in range(numeros):
        numero = random.uniform(0,101)
        if modo == 1:
            print("{} => {}".format(numero, math.ceil(numero)))
            numero = math.ceil(numero)
        elif modo == 2:
            print("{} => {}".format(numero, math.floor(numero)))
            numero = math.floor(numero)
        elif modo == 3:
            print("{} => {}".format(numero, round(numero)))
            numero = round(numero)

        lista.append(numero)

    return lista

generador()
