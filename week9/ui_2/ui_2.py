# pip install tk
from tkinter import Tk # Window
from tkinter import Label # Label
from tkinter import Entry # Entry
from tkinter import Button # Button

# Declare and initialize
window = Tk()#declare and initialize
window.geometry("250x350")# Resize
window.resizable(False,False)# resizable-> False
window.title("Main Door")

lblNID = Label(window, text="NID:")
lblPages = Label(window, text="PAGE:")
lblPrice = Label(window, text="PRICE:")

txtNID = Entry(window,width=20)
txtPages = Entry(window,width=20)
txtPrice = Entry(window,width=20)

btnSave = Button(window,text="SAVE")
btnClose = Button(window,text="CLOSE")

lblNID.place(x=20, y=10)
txtNID.place(x=100, y=10)

lblPages.place(x=20, y=40)
txtPages.place(x=100, y=40)

lblPrice.place(x=20, y=70)
txtPrice.place(x=100, y=70)

btnSave.place(x=100, y=100)
btnClose.place(x=150, y=100)

window.mainloop()# display

# Resize window
