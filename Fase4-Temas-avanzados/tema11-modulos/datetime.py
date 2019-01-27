# importando datetime
import datetime

dt = datetime.datetime.now() # ahora
print("Mostrando tiempo con datetime.now :",dt)
print("Mostrando año: ",dt.year)
print("Mostrando mes: ",dt.month)
print("Mostrando dia",dt.day)
print("Mostrar hora: ",dt.hour)
print("Mostrar minuto: ",dt.minute)
print("Mostrar segundo: ",dt.second)
print("Mostrar microsegundos: ",dt.microsecond)
print("Mostrar zona horaria: ",dt.tzinfo)
print("Imprimiendo la hora {}:{}:{}".format(dt.hour, dt.minut, dt.second))
print("Imprimiendo la fecha {}/{}/{}".format(dt.day, dt.month, dt.year))
print("================================")
print("!!!Creando fecha manual!!!")
time = datetime.datetime(2000,1,1,0,0)
print("Fecha manual:",time)
