from tkinter import *
from tkinter import messagebox as MessageBox # cambiar el nombre de

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

# configuracion de la raiz
root = Tk()

Button(root, text="Clicame", command=test).pack()

# Finalmente bucle de la aplicacion
root.mainloop()
