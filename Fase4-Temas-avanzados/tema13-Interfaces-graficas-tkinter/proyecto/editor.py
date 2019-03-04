from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
# logica del editor

ruta = "" # guardar runta del fichero
def nuevo():
    global ruta
    mensaje.set("New File")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Stack-Edit ")


def abrir():
    global ruta
    mensaje.set("Open File")
    ruta = FileDialog.askopenfilename(initialdir='.',
         filetypes=(("Ficheros de Texto", "*.txt"),),
         title= "Abir un Fichero de Texto")

    if ruta != "":
         fichero = open(ruta, 'r')
         contenido = fichero.read()
         texto.delete(1.0, "end")
         texto.insert('insert', contenido)
         fichero.close()
         root.title(ruta + " - Stack-Edit ")

def guardar():
    mensaje.set("Save")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Saved File")
    else:
        guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Save As")
    fichero = FileDialog.asksaveasfile(title="Saved File", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Saved File")
    else:
        menaje.set("Saved Canceled")
        ruta=""


# configuracion de la raiz
root = Tk()
root.title("Stack-Edit")

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New File", command=nuevo)
filemenu.add_command(label="Open File", command=abrir)
filemenu.add_command(label="Save", command=guardar)
filemenu.add_command(label="Save As", command=guardar_como)
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
