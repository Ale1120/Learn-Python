# ejerccio 1
usuario = {'marta','david','elvira', 'juan', 'marcos'}
admin = {'juan', 'marta'}
# para sacar un elemento de una coleccion
admin.discard('juan')
admin.add('marcos')

for i in usuario:
    if i in admin:
        print(i, 'es admin')
    else:
        print(i,'no es admin')
