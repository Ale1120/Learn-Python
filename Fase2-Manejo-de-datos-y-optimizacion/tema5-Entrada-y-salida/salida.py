v = 'otro texto'
n = 10
print('un Texto',v,'y un numero', n)

# manera de hacerlo mas eficiente de mostrar informacion
c = 'un Texto {} y un numero  {}'.format(v,n)

print('un Texto {0} y un numero  {1}'.format(v,n))

print('un Texto {texto} y un numero  {numero}'.format(texto=v,numero=n))
print('un Texto {v} y un numero  {n}'.format(v,n))
