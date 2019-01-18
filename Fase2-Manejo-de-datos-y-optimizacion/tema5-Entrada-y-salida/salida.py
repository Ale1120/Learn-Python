v = 'otro texto'
n = 10
print('un Texto',v,'y un numero', n)

# manera de hacerlo mas eficiente de mostrar informacion
c = 'un Texto {} y un numero  {}'.format(v,n)

print('un Texto {0} y un numero  {1}'.format(v,n))

print('un Texto {texto} y un numero  {numero}'.format(texto=v,numero=n))

print('{texto},{texto},{texto}'.format(texto=v))

# Alineamiento
# dereccha
print('{:>30}'.format('Hola'))
# izquierda
print('{:30}'.format('Hola'))
# centrado
print('{:^30}'.format('Hola'))


# truncamiento
print('{:.3}'.format('Alejandro'))

# truncamiento y Alineamiento
print('{:>30.3}'.format('Alejandro'))

# formateo de numeros enteros, rellenados con espacios
print('{:4d}'.format(10))
print('{:4d}'.format(100))
print('{:4d}'.format(1000))

# formateo de numeros enteros, rellenados con 0
print('{:04d}'.format(10))
print('{:04d}'.format(100))
print('{:04d}'.format(1000))

# formateo de numeros flotantes, relleandos con espacio
print('{:.3f}'.format(3.14.15929))
print('{:.3f}'.format(153.21))

# formateo de numeros decimales(caracteres) con espacio
print('{:7.3f}'.format(3.14.15929))
print('{:7.3f}'.format(153.21))

# formateo de numeros decimales(caracteres) con 0
print('{:07.3f}'.format(3.14.15929))
print('{:07.3f}'.format(153.21))
