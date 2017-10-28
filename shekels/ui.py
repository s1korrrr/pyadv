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


class AddExpense(tk.Frame):
    def __init__(self, master, add_product_command=None):
        super().__init__(master)
        self.name_variable = tk.StringVar()
        self.price_variable = tk.StringVar()

        self.add_product_command = add_product_command

        name_text_box = tk.Entry(self, textvariable=self.name_variable)
        name_text_box.grid(row=0, column=0)

        price_text_box = tk.Entry(self, textvariable=self.price_variable)
        price_text_box.grid(row=0, column=1)

        add_button = tk.Button(self, text='add', command=self.add_cmd)
        add_button.grid(row=0, column=2)

    def add_cmd(self):
        name = self.name_variable.get()
        price = self.price_variable.get()
        if name and price:
            try:
                price_int = int(price)
            except:
                return

            new_product = {'name': name, 'price': price_int}
            if self.add_product_command:
                self.add_product_command(new_product)

            self.name_variable.set('')
            self.price_variable.set('')


class MainApp():
    def __init__(self):
        root = tk.Tk()
        self.root = root
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.title('Super shekels')

        self.listbox_variable = tk.StringVar()
        self.search_variable = tk.StringVar()

        list_box = tk.Listbox(root, listvariable=self.listbox_variable,
                              selectmode=tk.MULTIPLE)

        list_box.grid(row=0, column=0,
                      sticky=tk.E + tk.W + tk.S + tk.N)

        button_frame = tk.Frame(root)
        button_frame.grid(row=1, column=0)

        quit_button = tk.Button(button_frame, text='quit',
                                command=self.quit_cmd)
        quit_button.grid(row=0, column=2)

        search_button = tk.Button(button_frame, text='search',
                                  command=self.search_cmd)
        search_button.grid(row=0, column=1)

        text_box = tk.Entry(button_frame,
                            textvariable=self.search_variable)
        text_box.grid(row=0, column=0)

        add_product_frame = AddExpense(root,
                           add_product_command=self.add_product_cmd)
        add_product_frame.grid(row=2, column=0)

        expenses = get_expenses()
        self.listbox_variable.set(expenses)

    def run(self):
        self.root.mainloop()

    def search_cmd(self):
        text = self.search_variable.get()
        data = get_expenses(text)
        self.listbox_variable.set(data)

    def add_product_cmd(self, new_product):
        writer = ExpenseCSVData('expense.csv')
        with writer:
            writer.save(new_product)
        data = get_expenses()
        self.listbox_variable.set(data)

    def quit_cmd(self):
        self.root.quit()


if __name__ == '__main__':
    app = MainApp()
    app.run()
