from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, N, S
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.multiply_button = Button(master, text="x", command=lambda: self.update("multiply"))
        self.divide_button = Button(master, text="/", command=lambda: self.update("divide"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.multiply_button.grid(row=3, column=0)
        self.divide_button.grid(row=3, column=1)
        self.reset_button.grid(row=2, column=2, rowspan=2, sticky=W+E+N+S)
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = float(new_text)
            return True
        except ValueError:
            return False
    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "multiply":
            self.total *= self.entered_number
        elif method == "divide":
            if self.entered_number != 0:
                self.total /= self.entered_number
            else:
                self.total_label_text.set("Error: Div by 0") # Menampilkan pesan error
                return
        else: # reset
            self.total = 0
            self.entry.delete(0, END)
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()