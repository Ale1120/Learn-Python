from tkinter import *

root = Tk()

root.title("Hola Mundo")
root.resizable(1,1)
root.iconbitmap('@ironman.xbm') # forma de mostrar un icono

frame = Frame(root, width=480, height=320) # creando marco
frame.pack(fill='both', expand='1')
#frame.pack(side="bottom",  ancher ='w') # parametros buttom, etc.
#frame.config(width=480, height=320) # tamaño del frame
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief='sunken')

# en root
root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief='ridge')


# Abajo del todo
root.mainloop()
