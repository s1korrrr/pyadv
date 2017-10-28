import tkinter as t
# Zle praktyki z tym button1 :)

root = t.Tk()
root.geometry('320x240')
button1 = t.Button(root, text="Click me")

def f1(*args):
    print('hi', *args)
    button1['state'] = t.DISABLED

button2 = t.Button(root, text="Click me",
                   height=20, width=20,
                   command=f1)
button1.pack()
button2.pack()
root.mainloop()
