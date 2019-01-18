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
