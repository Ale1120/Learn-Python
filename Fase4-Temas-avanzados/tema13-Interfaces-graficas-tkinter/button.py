from tkinter import *

def hola():
    print("Hola Mundo")

def crear_label():
    Label(root, text="Label Creada Dinamicamente").pack()

# configuracion de la raiz
root = Tk()

Button(root, text="Clicame", command=crear_label).pack()
# Finalmente bucle de la aplicacion
root.mainloop()
