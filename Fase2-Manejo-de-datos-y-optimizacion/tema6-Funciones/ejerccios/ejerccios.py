# ejerccios1

def area_rectangulo(b,a):
    return b*a
print(area_rectangulo(15,10))

# ejerccios 2
import math
def area_circulo(r):
    retrun (r**2)* math.pi

print(area_circulo(5))

# ejerccio 3

def relaccion(a,b):
    if a > b:
        return 1
    elif a < b :
        return -1
    else:
        return 0
relaccion(5,10)
relaccion(10,5)
relaccion(5,5)
