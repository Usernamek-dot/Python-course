import tkinter 
from tkinter import messagebox
import sqlite3
import datetime
import pytz
window = tkinter.Tk()
window.geometry('600x600') 
window.title("USERS")
window.configure(bg="#485460")
def validateData():
     if idEntry.get()==""  or nameEntry.get() == "" or ageEntry.get() == "" or countryEntry.get() == "" or phoneEntry.get()=="" or dateEntry.get()=="":
          messagebox.showinfo(message="📛 Invalid data, make sure everything is filled out correctly.",title="Error")
     else:
          saveData()
def saveData(): 
    idd = idEntry.get()
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
    readData() 
    messagebox.showinfo(message="👌🏼 Info saved.", title="Data Saved")
def readData():
    con = sqlite3.connect("Users\Database.db")
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM Users;'):
        print(row)
    con.close()
def searchData():
    if not searchEntry.get().isdigit():
        outputMessage['text'] = "😑Your id must be only numbers. "
        searchEntry.delete(0, tkinter.END) 
    else:
        con = sqlite3.connect("Users\Database.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Users WHERE id = {searchEntry.get()}")
        row = cur.fetchone()
        if row != None:
            messagebox.showinfo(message=f"id: {row[0]},  Age: {row[1]}, Country: {row[2]}, Phone: {row[3]}, Date: {row[4]}", title="Record found")
            outputMessage['text'] = ""
        else:
            outputMessage['text'] = "😲Not found."                
        con.close()
#ttitle
titleLabel = tkinter.Label(window, text="Form", font=('Verdana', 20, 'bold'), bg='#485460',fg="#95a5a6")
titleLabel.grid(row=0, column=1, padx=20)
#id
idLabel = tkinter.Label(window, text="Type your id", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
idLabel.grid(row=1, column=0, pady=20)
idEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
idEntry.grid(row=1, column=1)
#name
nameLabel = tkinter.Label(window, text="Type your name", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
nameLabel.grid(row=2, column=0, pady=10,padx=20)
nameEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
nameEntry.grid(row=2, column=1)
#age
ageLabel = tkinter.Label(window, text="Type your age", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
ageLabel.grid(row=3, column=0, pady=20)
ageEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
ageEntry.grid(row=3, column=1)
#country
countryLabel = tkinter.Label(window, text="Type your country", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
countryLabel.grid(row=4, column=0, pady=20)
countryEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
countryEntry.grid(row=4, column=1)
#phone
phoneLabel = tkinter.Label(window, text="Type your phone", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
phoneLabel.grid(row=5, column=0, pady=20)
phoneEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
phoneEntry.grid(row=5, column=1)
#date
dateLabel = tkinter.Label(window, text="Type your date", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
dateLabel.grid(row=6, column=0, pady=20)
dateEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
dateEntry.grid(row=6, column=1)
# #search
searchLabel = tkinter.Label(window, text="", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
searchLabel.grid(row=7, column=0, pady=20)
searchEntry = tkinter.Entry(window, font=('Verdana', 15, 'italic'))
searchEntry.grid(row=7, column=1)
#buttons
saveBtn = tkinter.Button(window, text="SAVE", font=('Verdana', 14, 'italic'), bg='#34495e', fg='#FFFFFF', command=validateData)
saveBtn.grid(row=8, column=1, pady=20, sticky="E")
searchBtn = tkinter.Button(window, text="🔎SEARCH ID", font=('Verdana', 14), bg='#34495e', fg='#FFFFFF',command=searchData)
searchBtn.grid(row=7, column=0, pady=20)
# message
outputMessage = tkinter.Label(window, text="", font=('Verdana', 15, 'italic'), bg='#485460',fg="#bdc3c7")
outputMessage.grid(row=8, column=0 ,pady=20)
window.mainloop()







