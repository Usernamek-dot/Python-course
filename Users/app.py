import tkinter 
from tkinter import messagebox
import sqlite3
import datetime
import pytz
window = tkinter.Tk()
window.geometry('1000x600') 
window.title("USERS")
#name
nameLabel = tkinter.Label(window, text="Type your name", font=('Verdana', 19, 'bold'), bg='#5FA8D3')
nameLabel.grid(row=1, column=0, pady=20)
nameEntry = tkinter.Entry(window, font=('Verdana', 19, 'bold'))
nameEntry.grid(row=1, column=1)
#age
ageLabel = tkinter.Label(window, text="Type your age", font=('Verdana', 19, 'bold'), bg='#5FA8D3')
ageLabel.grid(row=2, column=0, pady=20)
ageEntry = tkinter.Entry(window, font=('Verdana', 19, 'bold'))
ageEntry.grid(row=2, column=1)
#country
countryLabel = tkinter.Label(window, text="Type your country", font=('Verdana', 19, 'bold'), bg='#5FA8D3')
countryLabel.grid(row=3, column=0, pady=20)
countryEntry = tkinter.Entry(window, font=('Verdana', 19, 'bold'))
countryEntry.grid(row=3, column=1)
#phone
phoneLabel = tkinter.Label(window, text="Type your phone", font=('Verdana', 19, 'bold'), bg='#5FA8D3')
phoneLabel.grid(row=4, column=0, pady=20)
phoneEntry = tkinter.Entry(window, font=('Verdana', 19, 'bold'))
phoneEntry.grid(row=4, column=1)
#date
dateLabel = tkinter.Label(window, text="Type your date", font=('Verdana', 19, 'bold'), bg='#5FA8D3')
dateLabel.grid(row=5, column=0, pady=20)
dateEntry = tkinter.Entry(window, font=('Verdana', 19, 'bold'))
dateEntry.grid(row=5, column=1)
#buttons
saveBtn = tkinter.Button(window, text="SAVE", font=('Verdana', 20, 'bold'), bg='#1B4965', fg='#FFFFFF', command=validate)
saveBtn.grid(row=6, column=1, pady=20)



window.mainloop()



