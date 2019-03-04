from tkinter import *
from tkinter import messagebox as MessageBox # cambiar el nombre de la funcion
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

def test():
    # creando ventana emergente
    # MessageBox.showwinfo("Hola!", "Hola Mundo.")
    # MessageBox.showwarning("Alerta!", "Seccion solo para administradores.")
    # MessageBox.showerror("Erro!", "Ha ocurrido un error inesperado")

    # ventana de eleccion
    # resultado = MessageBox.askquestion("Salir","¿Estas seguro si desea salir sin guardar")
    # if resultado == "yes":
    #     root.destroy()

    # ventana de aceptar o cancelar
    # resultado = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual")
    # if resultado:
    #     root.destroy()

    # ventana de leccion que retorna un true o false
    # resultado = MessageBox.askyesno("Salir","¿Estas seguro si desea salir sin guardar")
    # if resultado:
    #     root.destroy()

    # ventana de reintentar
    # resultado = MessageBox.askretrycancel("reintentar","No se puede conectar")
    # if resultado:
    #     root.destroy()

    # ventana de seleccionar color
    #color = ColorChooser.askcolor(title="Elige un Color!!!")
    #print(color)

    # ventana de abrir un archivo
    # ruta = FileDialog.askopenfilename(title="Abrir Un fichero", initialdir="/home",
    #      filetypes=(("Fichero de texto", "*.txt"),
    #          ("Fichero de python", "*.py"),
    #          ("Todos los ficheros","*.*")) )
    #
    # print(ruta)

    # ventana de guardar archivo
    # equivale a open('ruta','w')
    fichero = FileDialog.asksaveasfile(title="Guardar un Fichero", mode="w", defaultextension=".txt")
    print(fichero)
    if fichero is not None:
        fichero.write("Hola voy a escribir otra cosa!")
        fichero.close()

# configuracion de la raiz
root = Tk()

Button(root, text="Clicame", command=test).pack()

# Finalmente bucle de la aplicacion
root.mainloop()
