import tkinter as t
from tkinter import ttk

def f():
    print(mainframe.grid_bbox(1, 1))

root = t.Tk()

mainframe = ttk.Frame(root)
mainframe.grid()

button1 = ttk.Button(mainframe,
                     text="Click me",
                     command=f, width=20)
button1.grid(row=0, column=0)

button2 = ttk.Button(mainframe,
                     text="Click me2       fdsdsafasfda"
                     , width=20)
button2.grid(row=1, column=1)



root.mainloop()
