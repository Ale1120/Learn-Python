try:
    n = input('Introdusca un numero: ')
    5/n
except Exception as e:
    print(type(e).__name__ )
