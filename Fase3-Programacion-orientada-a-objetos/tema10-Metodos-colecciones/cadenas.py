# metodo mayuscula
"Hola Mundo".upper()

# Metodo minusculas
"HOLA MUNDO".lower()

# primer letra de un string en mayuscula
"hola mundo".capatalize()

# primer letra de cada palabra en mayuscula
"hola mundo".title()

# contar las veces que aparece un caracter
"Hola mundo".count('o')

# para ver en que posicion comienza un aplabra
"Hola mundo".find('mundo')

# contar al de atras hacia adelante
"Hola mundo mundo mundo".rfind('mundo')

c = '100'
# para ver si es un digito
c.isdigit()

# para saber si todo es alfanumerico
c2 = "ABC123f"
c2.isalnum()

# solo si tenemos letra (los espacio no cuenta)
c3 = "AAAAVVaaa"
c3.isalpha()

# es todo minusculas
"Hola mundo".islower()

# es todo mayuscula
"Hola mundo".isupper()

# es letra mayuscula en cada letra
"Hola mundo".istitle()

# es espacio
"  ". insspace()

# para ver si comiensa con una letra o cadena
"hola Mundo".startswith("hola")

# para ver si termina con una letra o cadena
"hola mundo".endswhith('mundo')

# separar una cadena de caracteres y crea una lista
"hola Mundo bn".split()

# para serparar con parametros
"hola,mundo,bn,j".split(,)

# unir cadenas ejemplo con (,)
",".join("hola munado")

# elminiar espacio por delante y por de tras
"   Hola mundo  ".strip()

# eliminar por parametros
"------Hola mundo---- ".strip('-')
