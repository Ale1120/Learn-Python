# funcionando
def numeros(numero=None):
    if numero is None:
        print("error! no se permite un valor nulo")

numeros()

# invocando a la excepcion
def numeros(numero=None):
    if numero is None:
        raise ValueError("error! no se permite un valor nulo")

numeros()
