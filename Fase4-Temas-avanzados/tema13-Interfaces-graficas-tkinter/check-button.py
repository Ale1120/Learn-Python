from tkinter import *


# configuracion de la raiz
root = Tk()
root.title("Cafetería")
root.config(bd=15)

leche = IntVar()  # 1 si, 0 no
azucar = IntVar() # 1 si, 0 no


imagen = PhotoImage(file="gif.gif")
Label(root,image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="right")


Label(frame, text="¿ Cómo quieres el café?").pack()
Checkbutton(frame,text="Con leche", variable=leche, onvalue=1, offvalue=0).pack()
Checkbutton(frame,text="Con azúcar", variable=azucar, onvalue=1, offvalue=0).pack()


# Bucle de la aplicacion
root.mainloop()
