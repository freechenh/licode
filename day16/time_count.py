from datetime import datetime
import tkinter

print(datetime.now())

top = tkinter.Tk()

# li = ['c', 'python', "php"]
#
# movies = ['css', 'jquery', "bootstrap"]
#
# list_b = tkinter.Listbox(top)
# list_a = tkinter.Listbox(top)
#
#
# for item in li:
#     list_b.insert(0, item)
#
# for item in movies:
#     list_a.insert(0, item)


# list_b.pack()
# list_a.pack()

while True:
    show_time = tkinter.Label(top, text=datetime.now())

    show_time.pack()

    top.mainloop()
