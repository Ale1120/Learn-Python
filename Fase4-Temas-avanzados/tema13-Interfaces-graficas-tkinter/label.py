from tkinter import *

# configuracion de la raiz
root = Tk()

# cofinguracion de un marco
frame = Frame(root, width=480, height=320)
frame.pack()

label = Label(frame, text="¡Hola Mundo!")
label.place(x=100, y=100)

# Finalmente bucle de la aplicacion
root.mainloop()
