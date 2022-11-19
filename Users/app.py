import tkinter 
import sqlite3
import datetime
import pytz
from tkinter import messagebox
# from defs import *

window = tkinter.Tk()
window.geometry('630x630') 
window.title("USERS")
window.configure(bg="#485460")

# def validateData():
#     try:
#         if idd != ""  and name != "" and age !="" and country != "" and phone !="" and date !="":
#             saveData()    
#     except ValueError:
#         message['text'] = "😑Fill all out. "
#         idd.delete(0, tkinter.END) 
def validateData():
    if not idEntry.get().isdigit():
        message['text'] = "😑Your id must be only numbers. "
    if idEntry.get() == ""  or nameEntry.get() == "" or ageEntry.get() == "" or countryEntry.get() == ""      or phoneEntry.get()=="" or dateEntry.get()=="":
        message['text'] = "😑Fill all out. "
    else:
          saveData()

def saveData(): 
    idd =int(idEntry.get())
    name = nameEntry.get()
    age = ageEntry.get()
    country = countryEntry.get()
    phone = phoneEntry.get()

    date = datetime.datetime.now(pytz.timezone('America/Bogota'))

    con = sqlite3.connect("Users\Database.db")
    con.execute(
        f"insert into Users(id,name,age,country,phone,date) values ({idd},'{name}', {age}, '{country}', '{phone}','{date}')")
    con.commit() 
    con.close() 
    messagebox.showinfo(message="👌🏼 Info saved.", title="Data Saved")

def searchData():
    if not searchEntry.get().isdigit():
        message['text'] = "😑Your id must be only numbers. "
        searchEntry.delete(0, tkinter.END) 
    else:
        con = sqlite3.connect("Users\Database.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Users WHERE id = {searchEntry.get()}")
        row = cur.fetchone()
        if row != None:
            messagebox.showinfo(message=f"id: {row[0]},  Age: {row[1]}, Country: {row[2]}, Phone: {row[3]}, Date: {row[4]}", title="Record found")
            message['text'] = ""
        else:
            message['text'] = "😲Not found."                
        con.close()


#entries & labels
titleLabel = tkinter.Label(window, text="Form", font=('Verdana', 20, 'bold'), bg='#485460',fg="#95a5a6")
titleLabel.grid(row=0, column=1, padx=20)

idLabel = tkinter.Label(window, text="Type your id(only numbers)", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
idLabel.grid(row=1, column=0, pady=20)
idEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
idEntry.grid(row=1, column=1)

nameLabel = tkinter.Label(window, text="Type your name", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
nameLabel.grid(row=2, column=0, pady=10,padx=20)
nameEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
nameEntry.grid(row=2, column=1)

ageLabel = tkinter.Label(window, text="Type your age", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
ageLabel.grid(row=3, column=0, pady=20)
ageEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
ageEntry.grid(row=3, column=1)

countryLabel = tkinter.Label(window, text="Type your country", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
countryLabel.grid(row=4, column=0, pady=20)
countryEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
countryEntry.grid(row=4, column=1)

phoneLabel = tkinter.Label(window, text="Type your phone", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
phoneLabel.grid(row=5, column=0, pady=20)
phoneEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
phoneEntry.grid(row=5, column=1)

dateLabel = tkinter.Label(window, text="Type your date", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
dateLabel.grid(row=6, column=0, pady=20)
dateEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
dateEntry.grid(row=6, column=1)

searchLabel = tkinter.Label(window, text="", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
searchLabel.grid(row=7, column=0, pady=20)
searchEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
searchEntry.grid(row=7, column=1)


saveBtn = tkinter.Button(window, text="SAVE", font=('Verdana', 14, 'italic'), bg='#34495e', fg='#FFFFFF', command=validateData)
saveBtn.grid(row=8, column=1, pady=20, sticky="E")

searchBtn = tkinter.Button(window, text="🔎SEARCH ID", font=('Verdana', 14), bg='#34495e', fg='#FFFFFF',command=searchData)
searchBtn.grid(row=7, column=0, pady=20)


message = tkinter.Label(window, text="", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
message.grid(row=8, column=0 ,pady=20)


window.mainloop()







