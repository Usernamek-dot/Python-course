import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
# ❌
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My app")
        # self.geometry('400x400')
        self.config(background="black",highlightthickness=0)

        #grid layout manager
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=3)
        self.__create_widgets()

    def __create_widgets(self):
        ttk.Label(self, text='Id:').grid(column=0, row=0, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky=tk.W)

        ttk.Label(self, text='Name:').grid(column=0, row=1, sticky=tk.W)
        name = ttk.Entry(self, width=30)
        name.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self, text='Age:').grid(column=0, row=2, sticky=tk.W)
        age = ttk.Entry(self, width=30)
        age.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self, text='Country:').grid(column=0, row=3, sticky=tk.W)
        country = ttk.Entry(self, width=30)
        country.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self, text='Phone:').grid(column=0, row=4, sticky=tk.W)
        phone = ttk.Entry(self, width=30)
        phone.grid(column=1, row=4, sticky=tk.W)

        ttk.Label(self, text='Date of birth:').grid(column=0, row=5, sticky=tk.W)
        date = ttk.Entry(self, width=30)
        date.grid(column=1, row=5, sticky=tk.W)

        
        ttk.Button(self, text='Submit')["command"]=self.submit_clicked

        ttk.Button(self, text='Search').grid(column=5, row=0)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)

    def submit_clicked(self):
          showinfo(title="Message", message="Info saved. ✔")
          


if __name__ == "__main__":
    app = App()
    app.mainloop()