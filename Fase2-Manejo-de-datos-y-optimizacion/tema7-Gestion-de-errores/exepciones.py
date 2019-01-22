try:
    numero = float(input('agregue un numero: '))
    numero2 = 4
    print("{}/{}={}".format(numero,numero2,numero/numero2))
except:
    print('Ha ocurrido un error, agregue un numero')


while(True):
    try:
        numero = float(input('agregue un numero: '))
        numero2 = 4
        print("{}/{}={}".format(numero,numero2,numero/numero2))

    except:
        print('Ha ocurrido un error, agregue un numero')
    else:
        print('Todo ha funcionando correctamente')
        break # romper la el while si sale bn
