import tkinter as t
from tkinter import ttk

root = t.Tk()
root.overrideredirect(True)

mainframe = ttk.Frame(root)
mainframe.grid()

f1 = ttk.Frame(mainframe)
f1.grid(row=0, column=0)

button1 = ttk.Button(f1,
                     text="Click me", width=20)
button1.grid(row=0, column=0)

button2 = ttk.Button(f1,
                     text="Click me2", width=20)
button2.grid(row=1, column=1)

f2 = ttk.Frame(mainframe)
f2.grid(row=0, column=1, sticky=(t.N, t.S))

textbox = ttk.Entry(f2)
textbox.grid(row=0, column=0, sticky=(t.N, t.S))

root.mainloop()
