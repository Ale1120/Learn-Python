c = 0
while c < 5:
    c+=1
    print('c vale',c)
else:
    print('se termino c',c)


c = 0
while c < 5:
    c+=1
    if c==2:
        print('detenimos c con un break en ,',c)
        break
    print('c vale',c)
else:
    print('se termino c',c)



c = 0
while c < 5:
    c+=1
    if c==3:
        print('continuamos c con un continue en ,',c)
        continue
    print('c vale',c)
else:
    print('se termino c',c)



print('Bienvenido al menu interactivo')

while(True):
    print(""" Que quieres hacer?
    1) Saludar
    2) Sumar
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print('hola')
    elif opcion == '2':
        n1 = float(input("agrege n1: "))
        n2 = float(input("agrege n2: "))
        print("La suma es: ", n1+n2)
    elif opcion == '3':
        print('adios...')
        break
    else:
        print('comando erroneo')
