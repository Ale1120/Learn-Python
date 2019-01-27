import random

# numero aleatorio flotante >= 0 y < 1.0
print("Utilizando random.random() nos regresa numero random flotante>= 0 y < 1.0 ",random.random())

# numero aleatorio flotante entre dos numeros >= n1 y < n2.0
print("Utilizando random.uniform() nos regresa numero random flotante>= n1 y < n2.0 ",random.uniform(1,10))

# aleatorio-rango con numeros enteros >= 0 y < 10
print("Utilizando random.randrange(10) nos regresa numero random entero >= 0 y < 10 ",random.randrange(10))

# aleatorio-rango con numeros enteros >= n1 y < n2
print("Utilizando random.randrange(0,101) nos regresa numero random entero >= n1 y < n2 ",random.randrange(0,101))

# ejemplo de uso
print("Utilizando random.randrange(0,101,2) nos regresa numero random entero pares >= n1 y < n2 ",random.randrange(0,101,2))
