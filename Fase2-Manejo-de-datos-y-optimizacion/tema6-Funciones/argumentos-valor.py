# arugmentos por valor (string numeros) no modifica al global
def doble_valor(numero):
    numero*=2

n= 10
doble_valor(n)
n

# trucos por valor
def doble_valor(numero):
    numero*=2

n= 10
n= doble_valor(n)
n
