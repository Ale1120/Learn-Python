from tkinter import *

# configuracion de la raiz
root = Tk()

# creando un entry

label = Label(root, text="Usuario")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="disabled") # configuracion del imput

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*") # show para poner contraseñas



# Finalemente bucle de la aplicacion
root.mainloop()
