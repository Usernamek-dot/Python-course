import sqlite3
# En este ejemplo usamos TKINTER con el método PACK
import tkinter  # Librería de interfaz gráfica
from tkinter import messagebox
import datetime
import pytz


def validardatos():
    if entrada_producto.get() == "" or not entrada_precio.get().isdigit() or not entrada_cantidad.get().isdigit():
        messagebox.showinfo(
            message="Los campos son inválidos, por favor corríjalos", title="Error")
    else:
        guardardatos()


def guardardatos(): # Guarda los datos en la base de datos
    producto = entrada_producto.get()
    precio = entrada_precio.get()
    cantidad = entrada_cantidad.get()
    fecha = datetime.datetime.now(pytz.timezone('America/Bogota'))

    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect("Database.db")
    con.execute(
        f"insert into ventas(producto,precio, cantidad, fecha) values ('{producto}', {precio}, {cantidad}, '{fecha}')")
    con.commit()  # 'commit' para que se actualicen los datos en la tabla de la base de datos
    con.close() # Cierra la conexión
    leerdatos() # Se va a la función leerdatos
    messagebox.showinfo(message="Los datos han sido guardados exitosamente", title="Datos almacenados")


def leerdatos():
    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect("Database.db")
    # Con la conexión, crea un objeto cursor
    cur = con.cursor()

    # El resultado de "cursor.execute" puede ser iterado por fila
    for row in cur.execute('SELECT * FROM ventas;'):
        print(row)

    # No te olvides de cerrar la conexión
    con.close()


# En esta función si la base de datos no existe automaticamente python la crea.
def crear_database():
    # Crea un objeto de conexión a la base de datos SQLite
    con = sqlite3.connect("Database.db")
    # Con la conexión, crea un objeto cursor
    cur = con.cursor()
    cur.execute('''
          CREATE TABLE IF NOT EXISTS ventas
          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
          producto TEXT, 
          precio NUMERIC,
          cantidad NUMERIC,
          fecha TEXT
          )
          ''')


def buscardatos():
    # Verifica primero que la entrada sea numérica
    if not entrada_buscar.get().isdigit():
        label_mensaje['text'] = "🙄Debe ingresar solo números, que correspondan al id !"
        entrada_buscar.delete(0, tkinter.END) # Borra la entrada de buscar
    else:
        # Crea un objeto de conexión a la base de datos SQLite
        con = sqlite3.connect("Database.db")
        # Con la conexión, crea un objeto cursor
        cur = con.cursor()

        # Using a while loop
        cur.execute(f"SELECT * FROM ventas WHERE id = {entrada_buscar.get()}")
        row = cur.fetchone()
        if row != None:
            messagebox.showinfo(message=f"id: {row[0]},  Producto: {row[1]}, Precio: {row[2]}, Cantidad: {row[3]}, Fecha: {row[4]}", title="Dato encontrado")
            label_mensaje['text'] = ""
        
        else:
            label_mensaje['text'] = "🙄Este id no existe en la base de datos"                

        # No te olvides de cerrar la conexión
        con.close()


crear_database()
ventana = tkinter.Tk()
ventana.geometry("800x600")  # Dimensión de la ventana
ventana.title("VENTANA")  # Título de la ventana
# ventana.configure(background='#9C89B8')
# root.resizable(0,0) # Si deseo que la ventana no cambie de tamaño

# Label producto
label_producto = tkinter.Label(ventana, text="Producto:", font=('Arial', 20, 'bold'))  # Asignamos a esta variable la etiqueta LABEL de tkinter
# Cuando usamos grid, se pueden alinear los elementos con sticky
# Estos se posicionan como NORTE, SUR, ESTE, OESTE y se escriben en inglés: N, S, W, E
label_producto.grid(row=1, column=0, pady=20, padx=10, sticky="E")

# Caja de producto
entrada_producto = tkinter.Entry(ventana, font=('Arial', 25, 'bold'))
entrada_producto.grid(row=1, column=1, padx=20)

# PRECIO
# Asignamos a esta variable la etiqueta LABEL de tkinter
label_precio = tkinter.Label(ventana, text="Precio:", font=('Arial', 20, 'bold'))
label_precio.grid(row=2, column=0, pady=20, padx=10, sticky="E")

# Entrada de datos del PRECIO
entrada_precio = tkinter.Entry(ventana, font=('Arial', 25, 'bold'))
entrada_precio.grid(row=2, column=1, padx=20)

# Label CANTIDAD
label_cantidad = tkinter.Label(ventana, text="Cantidad:", font=('Arial', 20, 'bold'))  
label_cantidad.grid(row=3, column=0, pady=20, padx=10, sticky="E")

# Entrada de CANTIDAD
entrada_cantidad = tkinter.Entry(ventana, font=('Arial', 25, 'bold'))
entrada_cantidad.grid(row=3, column=1, padx=20)

# Botón Guardar
boton_guardar = tkinter.Button(ventana, text="📥 GUARDAR DATOS", font=('Arial', 14), bg='#F0E6EF', padx=20, command=validardatos)
boton_guardar.grid(row=4, column=1, pady=20)

# Label BUSCAR
label_buscar = tkinter.Label(ventana, text="Buscar:", font=('Arial', 20, 'bold'))  # Asignamos a esta variable la etiqueta LABEL de tkinter
label_buscar.grid(row=5, column=0)

# ENTRADA de BUSCAR
entrada_buscar = tkinter.Entry(ventana, font=('Arial', 25, 'bold'))
entrada_buscar.grid(row=5, column=1)

# Botón BUSCAR
boton_buscar = tkinter.Button(ventana, text="🔎BUSCAR", font=('Arial', 14), bg='#F0E6EF', padx=20, command=buscardatos)
boton_buscar.grid(row=5, column=2, sticky="E")

# Label MENSAJE
label_mensaje = tkinter.Label(ventana, text="", font=('Arial', 14, 'bold'), bg='#A8DCD9')  # Asignamos a esta variable la etiqueta LABEL de tkinter
label_mensaje.grid(row=6, column=0, pady=20, columnspan=5)

ventana.mainloop()  # Siempre tiene que ir al final
