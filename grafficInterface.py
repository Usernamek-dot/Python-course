import tkinter
window = tkinter.Tk()
window.geometry("900x600")
window.title("Diagram")
labelTitle = tkinter.Label(window,text="Diagram label",font=("Poppins",24),padx=20,pady=20,fg="#2c3e50")
labelTitle.pack(pady=15)
labeltem = tkinter.Label(window,text="Item",font=("Poppins",14),padx=20,pady=20)
labeltem.pack(pady=15)
entryItem = tkinter.Entry(window,font=("Poppins",19))
entryItem.pack()
window.mainloop() # always at the end