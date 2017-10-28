import tkinter as t

root = t.Tk()
root.geometry('320x240')

button1 = t.Button(root, text="Click me",
                   height=20, width=20)

button1.config(state=t.DISABLED)
button1['state'] = t.DISABLED

button1.pack()
root.mainloop()
