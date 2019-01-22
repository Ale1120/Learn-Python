try:
    n = input('Introdusca un numero: ')
    5/n
except TypeError:
    print('no se puede dividir un numeor con un string')
except Exception as e:
    print(type(e).__name__ )
