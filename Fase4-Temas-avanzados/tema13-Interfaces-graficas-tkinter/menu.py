from tkinter import *

# configuracion de la raiz
root = Tk()

# Creando menu
menubar= Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File")
filemenu.add_command(label="Open File")
filemenu.add_command(label="Save")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="View License")
filemenu.add_separator()
helpmenu.add_command(label="Welcome Guide")


menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)


# Finalmente bucle de la aplicacion
root.mainloop()
