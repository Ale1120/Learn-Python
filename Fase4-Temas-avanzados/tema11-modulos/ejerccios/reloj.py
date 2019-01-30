#ejerccios 2
import datetime
import time
import os # ejecutando mandos de la terminal

while True:
    os.system("clear")
    dt = datetime.datetime.now()
    print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
    time.sleep(1)
