if True:
    print('se cumple')


a = 2
b = 5
if a == 2:
    print('vale ',a)
    if b == 5:
        print('vale',b)

b = 10
a = 5
if a == 5 and b == 10:
    print('a vale 5, b vale 10')


n = 11
if n % 2 == 0:
    print(n,'es par')
else:
    print(n,'es impar')

comando = 'SALIR'

if comando == 'ENTRAR':
    print('bienvenido al sistema')
elif comando == "SALUDAR":
    print('Hola')
elif comando == 'SALIR':
    print('Saliendo')
else:
    print('error')


nota = float(input("agregar nota: "))
if nota >= 9:
    print('exelente')
elif nota >= 5 and nota >=7
    print(regular)
elif nota < 5:
    print('raspao')
