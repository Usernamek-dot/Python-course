import tkinter
def printt():
     print("This is a function.", entryItem.get())
window = tkinter.Tk()
#style window
window.geometry("900x600")
window.title("Diagram")
labelTitle = tkinter.Label(window,text="Diagram label",font=("Poppins",24),padx=20,pady=20,fg="#2c3e50")
labelTitle.pack(pady=15)
#add label  & entry
labeltem = tkinter.Label(window,text="Item",font=("Poppins",14),padx=20,pady=20)
labeltem.pack(pady=15)
entryItem = tkinter.Entry(window,font=("Poppins",19))
entryItem.pack()
#add label  & entry
labeltem2 = tkinter.Label(window,text="Item",font=("Poppins",14),padx=10,pady=10)
labeltem2.pack()
entryItem2 = tkinter.Entry(window,font=("Poppins",19))
entryItem2.pack(pady=15)
#button
btnSubmit = tkinter.Button(window,text="Submit",font=("Poppins",14,"bold"),bg="#e67e22",command=printt)
btnSubmit.pack()
# always at the end
window.mainloop() 