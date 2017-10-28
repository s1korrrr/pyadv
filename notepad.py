import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
# To jest potrzebne aby okno się skalowało
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry('300x200')
root.title('Super notepad')
root.minsize(300, 200)

text = tk.Text(root)
text.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky=tk.E)


def open_cmd():
    file = filedialog.askopenfile(filetypes=[('Text', '*.txt')])
    if file:
        content = file.read()
        text.delete('0.0', tk.END)
        text.insert('0.0', content)
        file.close()

open_button = tk.Button(button_frame, text='open', command=open_cmd)
open_button.grid(row=0, column=0)


def save_cmd():
    file_name = filedialog.asksaveasfilename(filetypes=[('Text', '*.txt')])
    if file_name:
        text_value = text.get('0.0', tk.END)
        with open(file_name, 'w') as f:
            f.write(text_value)


save_button = tk.Button(button_frame, text='save', command=save_cmd)
save_button.grid(row=0, column=1)


def quit_cmd():
    root.quit()


quit_button = tk.Button(button_frame, text='quit', command=quit_cmd)
quit_button.grid(row=0, column=2)

root.mainloop()
