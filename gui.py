from tkinter import *

root = Tk()
root.title('Grahp builder')
root.geometry('600x500+50+50')
root.minsize(600, 500)

iconGr = PhotoImage(file='icons/iconGr.png')
root.iconphoto(False, iconGr)

# -1.139 -- 1.139
btnSetStartPos = Button(text='set start value')
btnSetStartPos.grid(row=0, column=0)

btnSetStartPos = Button(text='set interval')
btnSetStartPos.grid(row=0, column=1)

btnSetStartPos = Button(text='save ghaph')
btnSetStartPos.grid(row=0, column=2)

root.mainloop()