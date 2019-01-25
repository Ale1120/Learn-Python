# ejerccios 1
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
