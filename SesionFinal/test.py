"""""
EJERCICIO: LOGIN

-Nombre
-Apellido
-dni
-edad
-sexo(M,F)

"""
import tkinter


ventana=tkinter.Tk()
ventana.geometry("400x300")

cajaTexto=tkinter.Entry(ventana)
cajaTexto.pack()

etiqueta=tkinter.Label(ventana)
etiqueta.pack()

def textoDeLaCaja():
    text20=cajaTexto.get()
    etiqueta["text"]=text20
    

ventana.mainloop()

