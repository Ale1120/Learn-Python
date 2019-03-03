from tkinter import *

# configuracion de la raiz
root = Tk()

opcion = IntVar()


Radiobutton(root, text="Opcion 1", variable=opcion, value=1).pack()
Radiobutton(root, text="Opcion 2", variable=opcion, value=2).pack()
Radiobutton(root, text="Opcion 3", variable=opcion, value=3).pack()

# Finalmente bucle de la aplicacion
root.mainloop()
