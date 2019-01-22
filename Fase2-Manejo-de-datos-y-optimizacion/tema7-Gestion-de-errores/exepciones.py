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
        break # romper la el while si sale bn
    except:
        print('Ha ocurrido un error, agregue un numero')
