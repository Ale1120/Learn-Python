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

# Creando fecha manual
print("!!!Creando fecha manual!!!")
time = datetime.datetime(2000,1,1,0,0)
print("Fecha manual:",time)

# formateo con iso
dt = datetime.datetime.now()
print("Mostrado el fecha con isoformat(): ", dt.isoformat())

# formateo manual a nuestra propia hora
# %A dia
# %d fecha (1-31)
# %B Meses en letras
# %Y año
# %I hora en formato 12
# %H hora en foramto 24
# %M minutos
print("!!! Formateando manual mente!!")
print("Mi Datetime formateado es :", dt.strftime("%A %d %B %Y %I:%M"))

# importando locale
import locale
locale.setlocale(locale.LC_ALL,'')
print("Mi Datetime formateado es con localete :", dt.strftime("%A %d %B %Y %H:%M"))
print("================================")

# ejemplo de uso de Datetime
print("Sumando nuestro dia actual + dos semanas")
dt = datetime.datetime.now()
t = datetime.timedelta(days=14, hours=4, seconds=10000)
semanas = dt + t
print("La fecha dentro de dos semanas es : ", semanas.strftime("%A %d %B %Y %H:%M"))
hace_dos_semanas = dt - t
print("Hace dos semanas : ", hace_dos_semanas.strftime("%A %d %B %Y %H:%M"))

# importando modulo de zonas horarias (pip3 install pytz)
import pytz
print(" ver zonas horarias del mundo",pytz.all_timezones)
dt = datetime.datetime.now(pytz.timezones('Asia/Tokio'))
print("Ver la hora de Tokio usando pytz.timeszones",dt.strftime("%A %d %B %Y %H:%M")))
