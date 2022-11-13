import tkinter
from tkinter import messagebox
import sqlite3
def save():
     conexion = sqlite3.connect("db.db")
     conexion.execute("insert into sales(product,price,quantity,date) values('Product1',' 2300','3',' 1990-12-03')")
     conexion.commit()
     conexion.close()
     cursor = conexion.cursor()#read data
     pass
def validate():
     if entryItem.get() == "" or entryItem2.get() == "":
          messagebox.showwarning(message="Fill all out",title="Warning")
     else:
          message["text"]= entryItem.get()
          save()
window = tkinter.Tk()
#style window
window.geometry("900x600")
window.title("Diagram")
window.configure(background="#130f40")
labelTitle = tkinter.Label(window,text="Diagram label",font=("Poppins",24),padx=20,pady=20,fg="#2c3e50")
labelTitle.grid(row=0,column=0,pady=20)
#add label  & entry
labeltem = tkinter.Label(window,text="Item",font=("Poppins",14),padx=20,pady=10)
labeltem.grid(row=1,column=0)
entryItem = tkinter.Entry(window,font=("Poppins",19))
entryItem.grid(row=1,column=1)
#add label  & entry
labeltem2 = tkinter.Label(window,text="Item",font=("Poppins",14),padx=20,pady=10)
labeltem2.grid(row=2,column=0)
entryItem2 = tkinter.Entry(window,font=("Poppins",19))
entryItem2.grid(row=2,column=1)
#add label  & entry
message = tkinter.Label(window,text="",font=("Poppins",14))
message.grid(row=5,column=1)
message = tkinter.Entry(window,text="",font=("Poppins",14))
#button
btnSubmit = tkinter.Button(window,text="Submit",font=("Poppins",14,"bold"),bg="#e67e22",command=validate)
btnSubmit.grid(row=3,column=1)
# always at the end
window.mainloop() 