import tkinter 
window = tkinter.Tk()
window.geometry('1000x600') 
window.title("USERS")
#id
idLabel = tkinter.Label(window, text="Type your id", font=('Verdana', 19, 'bold'), bg='#5FA8D3')
idLabel.grid(row=5, column=0, pady=20)
idEntry = tkinter.Entry(window, font=('Verdana', 19, 'bold'))
idEntry.grid(row=5, column=1)
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
#search
searchLabel = tkinter.Label(window, text="Type your search", font=('Verdana', 19, 'bold'), bg='#5FA8D3')
searchLabel.grid(row=6, column=0, pady=20)
searchEntry = tkinter.Entry(window, font=('Verdana', 19, 'bold'))
searchEntry.grid(row=6, column=1)
#buttons
saveBtn = tkinter.Button(window, text="SAVE", font=('Verdana', 20, 'bold'), bg='#1B4965', fg='#FFFFFF', command=validateData)
saveBtn.grid(row=6, column=1, pady=20)

searchBtn = tkinter.Button(window, text="🔎SEARCH", font=('Verdana', 14), bg='#F0E6EF', padx=20, command=searchData)
searchBtn.grid(row=5, column=2, sticky="E")

