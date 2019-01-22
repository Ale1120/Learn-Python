try:
    n = float(input('Introdusca un numero: '))
    5/n
except TypeError:
    print('no se puede dividir un numeor con un string')
except ValueError:
    print('Solo se perminte numeros')
except ZeroDivisionError:
    print('no se puede dividir por cero')
except Exception as e:
    print(type(e).__name__ )
