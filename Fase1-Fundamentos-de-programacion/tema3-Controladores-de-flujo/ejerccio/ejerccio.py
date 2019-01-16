n1 = float(input('agregar numero'))
n2 = float(input('agregar otro numero'))

print(""" Que quieres hacer?
1) sumar
2) Restar
3) Multiplicar""")
opcion = input()

if opcion == '1':
    print("La suma es: ", n1+n2)
elif opcion == '2':
    print("La resta es: ", n1-n2)
elif opcion == '3':
    print("El producto es: ", n1*n2)
else:
    print('comando erroneo')
