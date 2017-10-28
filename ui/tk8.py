import tkinter as t
from tkinter import ttk


def f():
    print(mainframe.grid_bbox(1, 1))


root = t.Tk()

mainframe = ttk.Frame(root)
mainframe.grid(sticky=t.E + t.W + t.S + t.N)
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

button1 = ttk.Button(mainframe,
                     text="Click me",
                     command=f)
button1.grid(row=0, column=0, columnspan=2,
             sticky=t.E + t.W)

button2 = ttk.Button(mainframe,
                     text="Click me2       fdsdsafasfda"
                     )
button2.grid(row=1, column=1)

button3 = ttk.Button(mainframe,
                     text="Click me2       fdsdsafasfda"
                     )
button3.grid(row=1, column=0)

root.mainloop()
