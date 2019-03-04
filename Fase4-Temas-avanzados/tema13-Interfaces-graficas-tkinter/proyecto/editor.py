from tkinter import *

# configuracion de la raiz
root = Tk()
root.title("Stack-Edit")

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File")
filemenu.add_command(label="Open File")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Caja de texto Central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# monitor inferior

mensaje = StringVar()
mensaje.set("Welcome a Stack-Edit")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
# Finalmente bucle de la aplicacion
root.mainloop()
