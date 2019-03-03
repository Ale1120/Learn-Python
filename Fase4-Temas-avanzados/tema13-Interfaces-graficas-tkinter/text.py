from tkinter import *

# configuracion de la raiz
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12), padx=5, pady=5) # lee caracteres no tamñano
# Finalmente bucle de la aplicacion
root.mainloop()
