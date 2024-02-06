import tkinter

ventana = tkinter.Tk()
ventana.title("Máquina expendedora de frutas")

def elegir_fruta(fruta):
    e_texto.insert(0, fruta)
    print("La fruta elegida es: " + fruta)

etiqueta = tkinter.Label(ventana, text = "Elige una fruta:", bg = "pink")
etiqueta.grid(row = 0, column = 0, columnspan = 4)

boton_banana = tkinter.Button(ventana, text = "Banana", width = 10, height = 3, bg = "yellow", command = lambda: elegir_fruta("Banana"))
boton_manzana = tkinter.Button(ventana, text = "Manzana", width = 10, height = 3, bg = "red", command = lambda: elegir_fruta("Manzana"))
boton_naranja = tkinter.Button(ventana, text = "Naranja", width = 10, height = 3, bg = "orange", command = lambda: elegir_fruta("Naranja"))
boton_pera = tkinter.Button(ventana, text = "Pera", width = 10, height = 3, bg = "green", command = lambda: elegir_fruta("Pera"))

boton_banana.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_manzana.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_naranja.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_pera.grid(row = 1, column = 3, padx = 5, pady = 5)

etiqueta1 = tkinter.Label(ventana, text = "La fruta elegida es:")
etiqueta1.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)
e_texto = tkinter.Entry(ventana)
e_texto.grid(row = 2, column = 2, columnspan = 2, padx = 5, pady = 5)

ventana.mainloop()