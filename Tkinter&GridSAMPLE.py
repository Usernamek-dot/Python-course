import tkinter # Librería para la interfaz gráfica
from tkinter import messagebox
import sqlite3
import datetime
import pytz


def validar():
    if entry_producto.get() == "" or entry_precio.get() == "" or entry_cantidad.get() == "" :
        messagebox.showinfo(message="Todos los campos deben tener datos ", title="Error")
    else:  
       label_mensaje['text'] = entry_producto.get()
       guardardatos()

def guardardatos():

    producto = entry_producto.get()
    precio = float(entry_precio.get())
    cantidad = int(entry_cantidad.get())
    fecha = datetime.datetime.now(pytz.timezone('America/Bogota'))

    con = sqlite3.connect('DatabaseVentas.db') # Conexión a la DB y se abre
    con.execute(f"insert into ventas(producto, precio, cantidad, fecha) values ('{producto}', {precio}, {cantidad}, '{fecha}' )")
    con.commit() # Commit actualiza los datos en la tabla
    con.close()

    #cur = con.cursor()
    


ventana = tkinter.Tk()
ventana.geometry('1000x600') # Tamaño de la ventana
ventana.title("VENTAS")
# ventana.configure(background='#9C89B8') # Cambiar el color del fondo


label_titulo = tkinter.Label(ventana, text="Control de ventas", font=('Arial', 25, 'bold'), bg='#5FA8D3')
label_titulo.grid(row=0, column=1, pady=20)


label_producto = tkinter.Label(ventana, text="Escriba el nombre producto", font=('Arial', 20, 'bold'), fg='#5FA8D3')
label_producto.grid(row=1, column=0)

entry_producto = tkinter.Entry(ventana, font=('Arial', 20, 'bold'))
entry_producto.grid(row=1, column=1)


label_precio = tkinter.Label(ventana, text="Escriba el precio del producto", font=('Arial', 20, 'bold'), fg='#5FA8D3')
label_precio.grid(row=2, column=0)

entry_precio = tkinter.Entry(ventana, font=('Arial', 20, 'bold'))
entry_precio.grid(row=2, column=1, pady=20)

label_cantidad = tkinter.Label(ventana, text="Escriba la cantidad del producto", font=('Arial', 20, 'bold'), fg='#5FA8D3')
label_cantidad.grid(row=3, column=0)

entry_cantidad = tkinter.Entry(ventana, font=('Arial', 20, 'bold'))
entry_cantidad.grid(row=3, column=1)

boton_guardar = tkinter.Button(ventana, text="Guardar", font=('Arial', 20, 'bold'), bg='#1B4965', fg='#FFFFFF', command=validar)
boton_guardar.grid(row=4, column=1, pady=20)

label_mensaje = tkinter.Label(ventana, text="", font=('Arial', 20, 'bold'))
label_mensaje.grid(row=5, column=1)


ventana.mainloop() # Simpre esta línea va al final