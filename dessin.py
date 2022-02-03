from tkinter import *
win=Tk()
win.geometry("500x500")
win.title("Window")
can = Canvas(win, width=500, height =500)
can.grid()

for i in range(1,501,10) :
    can.create_oval(i,10,i+10,10, activefill="black")

win.mainloop()
