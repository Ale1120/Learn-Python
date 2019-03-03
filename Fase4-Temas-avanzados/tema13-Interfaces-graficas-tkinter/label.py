from tkinter import *

# configuracion de la raiz
root = Tk()

# variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")


Label(root, text="¡Hola Mundo!").pack(anchor="nw")
label = Label(root, text="¡Hola alejandro !")
label.pack(anchor="center")
Label(root, text="¡Adios!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("verdana", 24))
label.config(textvariable=texto)
# Finalmente bucle de la aplicacion
root.mainloop()
