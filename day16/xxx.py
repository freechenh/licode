from datetime import datetime
from tkinter import *
from threading import Timer
from random import randint


def autoText():
    global timer, var
    var.set(datetime.now())
    timer = Timer(0.1, autoText)
    timer.start()


win = Tk()
var = StringVar()
var.set(datetime.now())
lb1 = Label(textvariable=var)
lb1.pack()
timer = Timer(0.1, autoText)
timer.start()
win.mainloop()
