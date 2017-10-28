import tkinter as tk

from shekels.expense import ExpenseCSVData


def get_expenses(search=None):
    reader = ExpenseCSVData('expense.csv')
    result = []
    with reader:
        if search:
            data = reader.search(search)
        else:
            data = reader.load()

        for item in data:
            r = "{name} - {price}".format(**item)
            result.append(r)
    return result


def search_cmd():
    text = search_variable.get()
    data = get_expenses(text)
    listbox_variable.set(data)


root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title('Super shekels')

listbox_variable = tk.StringVar()
search_variable = tk.StringVar()

list_box = tk.Listbox(root, listvariable=listbox_variable,
                      selectmode=tk.MULTIPLE)

list_box.grid(row=0, column=0,
              sticky=tk.E + tk.W + tk.S + tk.N)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0)

quit_button = tk.Button(button_frame, text='quit')
quit_button.grid(row=0, column=2)

search_button = tk.Button(button_frame, text='search',
                          command=search_cmd)
search_button.grid(row=0, column=1)

text_box = tk.Entry(button_frame,
                    textvariable=search_variable)
text_box.grid(row=0, column=0)

expenses = get_expenses()
listbox_variable.set(expenses)

root.mainloop()
