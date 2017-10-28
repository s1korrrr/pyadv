
from tkinter import filedialog

filename = filedialog.asksaveasfilename(filetypes=[('text', '*.txt')])
print(filename)

