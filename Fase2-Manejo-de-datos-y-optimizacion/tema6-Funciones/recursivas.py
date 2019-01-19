# funcion recursivas sin retorno

def cuenta_atras(num):
    num -=1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print('Booom!')
cuenta_atras(5)
