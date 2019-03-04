from tkinter import *
from tkinter import messagebox as MessageBox # cambiar el nombre de

def test():
    # creando ventana emergente
    MessageBox.showwarning("Alerta!", "Seccion solo para administradores.")

# configuracion de la raiz
root = Tk()

Button(root, text="Clicame", command=test).pack()

# Finalmente bucle de la aplicacion
root.mainloop()
