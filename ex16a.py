from tkinter import *
win=Tk()
#win.geometry("500x500")
win.title("Window")
can = Canvas(win, width=500, height =500)
can.grid()

for i in range(1,11) :
    can.create_rectangle(10,10,i*50,i*50)

win.mainloop()
