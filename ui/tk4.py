import tkinter as t


class MyWindow(t.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.button1 = t.Button(self, text='click me',
                                command=self.print)

    def setup(self):
        self.button1.pack()
        self.pack()

    def print(self):
        print(self.button1['text'])


root = t.Tk()
m = MyWindow(root)
m.setup()
root.mainloop()
