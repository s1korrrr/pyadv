import tkinter as t
from tkinter import ttk

class CopyPaster(ttk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.input = t.StringVar()
        self.output = t.StringVar()
        self._build()
        self.value = None

    def _build(self):
        self.grid()

        textbox = ttk.Entry(self,
                textvariable=self.input)
        textbox.grid()

        button = ttk.Button(self,
                    command=self.copypaste,
                    text='click')
        button.grid()

        label = ttk.Label(self,
                  textvariable=self.output)
        label.grid()

    def copypaste(self):
        self.value = self.input.get()
        self.output.set(self.value)
        tw = t.Toplevel(self)
        tw.grab_set()
        CopyPaster(tw)


if __name__ == '__main__':
    root = t.Tk()
    a = CopyPaster(root)
    b = CopyPaster(root)
    root.mainloop()
