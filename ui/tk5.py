import tkinter as t


class MyWindow(t.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.button_text = t.StringVar()
        self.button_text.set('click me')
        self.button1 = t.Button(self,
                                textvariable=self.button_text,
                                command=self.print)

    def setup(self):
        self.button1.pack()
        self.pack()

    def print(self):
        self.button_text.set("i have been clicked")

root = t.Tk()
m = MyWindow(root)
m.setup()
root.mainloop()
