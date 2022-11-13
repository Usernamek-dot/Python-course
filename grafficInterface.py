import tkinter
window = tkinter.Tk()
window.geometry("900x600")
window.title("Diagram")
label_title = tkinter.Label(window,text="Diagram label",font=("Poppins",24),padx=20,pady=20)
label_title.pack()
label_item = tkinter.Label(window,text="Item",font=("Poppins",14),padx=20,pady=20)
label_item.pack()
window.mainloop() # always at the end