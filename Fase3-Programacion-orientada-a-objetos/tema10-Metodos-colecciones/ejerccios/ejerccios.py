# ejerccios 1 string
texto = "un dia que el viedo soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viendo -respondio otro monje#ni las banderolas ni el viento lo que se mueve son vuestras mente -dijo el maestro"

lineas = texto.split("#")

for i,linea in enumerate(lineas):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else:
        lineas[i] = "- " +lineas[i] + "."

for linea in lineas:
    print(linea)

print("======================================")

# ejerccios 2 lista

lista = [29,-5,-12,17,5,24,5,12,23,16,12,5,-15,17]

def modificar(numeros):
    numeros = list(set(numeros)) # conjuntos
    numeros.sort(reverse=True)
    for i, numero in enumerate(numeros):
        if numero%2 != 0:
            del(numeros[i])
    suma = sum(numeros)
    numeros.insert(0,suma)
    return numeros

nueva_lista = modificar(lista)
print("nueva lista:",nueva_lista)
print("La suma de la nueva lista es igual a la posicion 0 es igual a {} :".format(nueva_lista[0]), nueva_lista[0] == sum(nueva_lista[1:]))
print("lista original",lista)
