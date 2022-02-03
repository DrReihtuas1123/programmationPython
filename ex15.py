from tkinter import *
win=Tk()
#win.geometry("500x500")
win.title("Window")
can = Canvas(win, width=500, height =500)
can.grid()

for i in range(1,11) :
    can.create_line(10, 30*i, 280, 30*i)
    can.create_line(30*(i-1) +10, 30, 30*(i-1)+10, 300)


win.mainloop()
