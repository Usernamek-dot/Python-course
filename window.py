import sqlite3
import tkinter as tk
from tkinter import END, Frame, messagebox
import datetime
import pytz


def validate_data():
    if not entry_id.get().isdigit():
     messagebox.showinfo( message="Only numbers ❌ ", title="ERROR")
    if entry_id.get() == ""  or entry_name.get() == "" or entry_age.get() == "" or entry_country.get() == ""      or entry_phone.get()=="" :
     messagebox.showinfo(message="Invalid data ❌ ", title="ERROR")
    else:
          save_data()

def save_data(): 
    idd =int(entry_id.get())
    name = entry_name.get()
    age = entry_age.get()
    country = entry_country.get()
    phone = entry_phone.get()

    date = datetime.datetime.now(pytz.timezone('America/Bogota'))

    con = sqlite3.connect("Users\Database.db")
    con.execute(
        f"insert into Users(id,name,age,country,phone,date) values ({idd},'{name}', {age}, '{country}', '{phone}','{date}')")
    con.commit() 
    con.close() 
    messagebox.showinfo(message="Saved data ✔ ", title="SAVE DATA")

def search_data():
    if not entry_search.get().isdigit():
        label_message['text'] = "Only numbers ❌ !"
        entry_search.delete(0, tk.END)
    else:
        con = sqlite3.connect("Users/Database.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Users WHERE id = {entry_search.get()}")
        row = cur.fetchone()
        if row != None:
            messagebox.showinfo(message=f"  Id 📸:    {row[0]}\n  Name🐱‍💻:    {row[1]}\n  Age🙊:    {row[2]}\n  Country🌍:    {row[3]}\n  Phone☎:    {row[4]}\n  Date🕚:    {row[5]}",    title="RECORD FOUND ")
            label_message['text'] = ""
        
        else:
            label_message['text'] = "Record not found ❌ "                
        con.close()

def clear_widgets():
     entry_id.delete(0,END)
     entry_name.delete(0,END)
     entry_age.delete(0,END)
     entry_country.delete(0,END)
     entry_phone.delete(0,END)



root = tk.Tk()
root.title("USER")  
root.configure(background='black')

border_color = tk.Frame(root, highlightbackground = "black",highlightthickness = 2, bd=0)

label_id = tk.Label(root, text="Id:", font=('Verdana', 18),bd=0)  
label_id.grid(row=1, column=0, pady=20, padx=10, sticky="E")

entry_id = tk.Entry(root,  font=('Verdana', 25,'bold'))
entry_id.grid(row=1, column=1, padx=20)
entry_id.config(bg="#2d3436")

label_name = tk.Label(root, text="Name:", font=('Verdana', 18))
label_name.grid(row=2, column=0, pady=20, padx=10, sticky="E")

entry_name = tk.Entry(root,  font=('Verdana', 25,'bold'))
entry_name.grid(row=2, column=1, padx=20)
entry_name.config(bg="#2d3436")

label_age = tk.Label(root, text="Age:", font=('Verdana', 18))  
label_age.grid(row=3, column=0, pady=20, padx=10, sticky="E")

entry_age = tk.Entry(root, font=('Verdana', 25, 'bold'))
entry_age.grid(row=3, column=1, padx=20)
entry_age.config(bg="#2d3436")

label_country = tk.Label(root, text="Country:", font=('Verdana', 18))  
label_country.grid(row=4, column=0, pady=20, padx=10, sticky="E")

entry_country = tk.Entry(root, font=('Verdana', 25, 'bold'))
entry_country.grid(row=4, column=1, padx=20)
entry_country.config(bg="#2d3436")

label_phone = tk.Label(root, text="Phone:", font=('Verdana', 18))  
label_phone.grid(row=5, column=0, pady=20, padx=10, sticky="E")

entry_phone = tk.Entry(root, font=('Verdana', 25, 'bold'))
entry_phone.grid(row=5, column=1, padx=20)
entry_phone.config(bg="#2d3436")

button_submit = tk.Button(root, text="📥 SUBMIT", font=('Verdana', 14), bg='#7f8c8d', padx=20, command=validate_data)
button_submit.grid(row=8, column=1, pady=20)

button_clear = tk.Button(root, text="📥 CLEAR", font=('Verdana', 14), bg='#7f8c8d', padx=20, command=clear_widgets)
button_clear.grid(row=9, column=1, pady=20)

label_search = tk.Label(root, text="Search for id:", font=('Verdana', 12))  
label_search.grid(row=7, column=0, pady=20, padx=10, sticky="E")

entry_search = tk.Entry(root, font=('Verdana', 25, 'bold'))
entry_search.grid(row=7, column=1)
entry_search.config(bg="#2d3436")

button_search = tk.Button(root, text="🔎SEARCH", font=('Verdana', 14), bg='#7f8c8d', padx=20, command=search_data)
button_search.grid(row=7, column=2, sticky="E")

label_message = tk.Label(root, text="", font=('Verdana', 14, 'bold'), bg='#7f8c8d')  
label_message.grid(row=6, column=0, pady=20, columnspan=5)

root.mainloop()  
