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

# ejerccio 2

caballero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
guerrero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
arquero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}

caballero['vida'] = guerrero['vida']*2
caballero['defensa'] = guerrero['defensa']*2

guerrero['ataque'] = caballero['ataque']*2
guerrero['alcance'] = caballero['alcance']*2

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa']/2
arquero['alcance'] = guerrero['alcance']*2

print('Caballero:\t', caballero)
print('guerrero:\t', guerrero)
print('arquero:\t', arquero)
