import tkinter 
from tkinter import messagebox
import sqlite3
import datetime
import pytz
from inputs import *
def validateData():
    if  idEntry.get().isdigit() or not nameEntry.get() == "" or not ageEntry.get().isdigit() or not countryEntry.get() or not phoneEntry.get().isdigit()or not dateEntry.get().isdigit() :
        messagebox.showinfo(
            message="📛 Invalid data, make sure everything is filled out.", title="Error")
    else:
        saveData()
def saveData(): 
    idd = idEntry.get()
    name = nameEntry.get()
    age = int(ageEntry.get())
    country = countryEntry.get()
    phone = phoneEntry.get()
    date = datetime.datetime.now(pytz.timezone('America/Bogota'))
    con = sqlite3.connect("Database.db")
    con.execute(
        f"insert into Users(id,name,age,country,phone,date) values ('{idd}','{name}', {age}, {country}, '{phone}','{date}',)")
    con.commit() 
    con.close() 
    readData() 
    messagebox.showinfo(message="👌🏼 Info saved.", title="Data Saved")

def readData():
    con = sqlite3.connect("Database.db")
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM Users;'):
        print(row)
    con.close()

def searchData():
    if not searchEntry.get().isdigit():
        searchLabel['text'] = "😑Your id must be only numbers. "
        searchEntry.delete(0, tkinter.END) 
    else:
        con = sqlite3.connect("Database.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Users WHERE id = {searchEntry.get()}")
        row = cur.fetchone()
        if row != None:
            messagebox.showinfo(message=f"id: {row[0]},  Age: {row[1]}, Country: {row[2]}, Phone: {row[3]}, Date: {row[4]}", title="Record found")
            searchLabel['text'] = ""
        else:
            searchLabel['text'] = "😲Not found."                
        con.close()
    window.mainloop()






