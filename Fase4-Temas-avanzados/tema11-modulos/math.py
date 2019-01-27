import math

# redondeo
pi = 3.14159
print("Redondeo de pi con round(): ",round(pi))
print("Redondeo a la baja con math.floor(): ",math.floor(3.5))
print("Redondeo a la altta con math.ceil(): ",math.ceil(3.000001))

# valor absoluto
print("EL valor absoluto de -10 es :",abs(-10))

# sumatiorio
 n = [1,2,3]
 print("la suma de una lista 1,2,3 con math.fsum():",math.fsum(n))
#ejemplo de uso
n = [0.999999,2,3]
print( "La suma de una lista 0.999999,2,3 con fsum():",math.fsum(n))
