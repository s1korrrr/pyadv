import tkinter as t
from tkinter import ttk


def f():
    a = input.get()
    output.set(a)


root = t.Tk()

input = t.StringVar()
output = t.StringVar()

frame = t.Frame(root)
frame.grid()

textbox = ttk.Entry(frame, textvariable=input)
textbox.grid()

button = ttk.Button(frame, command=f, text='click')
button.grid()

label = ttk.Label(frame, textvariable=output)
label.grid()

root.mainloop()
