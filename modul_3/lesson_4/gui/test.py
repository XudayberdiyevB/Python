import tkinter as tk
from tkinter import *

my_w = tk.Tk()
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+\w+[.]\w{2,3}$'
my_w.geometry("400x100")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title


def validate(u_input):
    if (re.search(regex, u_input) and u_input.isalpha):
        print(True)
        b1.config(state='active')
        return True
    else:
        print(False)
        b1.config(state='disabled')
        return False


my_valid = my_w.register(validate)
l1 = tk.Label(my_w, text='Email')
l1.grid(row=1, column=1, padx=5, pady=20)
e1 = Entry(my_w, validate='focusout', validatecommand=(my_valid, '%P'))
e1.grid(row=1, column=2, padx=10)
l2 = tk.Label(my_w, text='Name')
l2.grid(row=1, column=3, padx=5, pady=20)
e2 = tk.Entry(my_w, width=10)
e2.grid(row=1, column=4)
b1 = tk.Button(my_w, text='Submit')
b1.grid(row=1, column=5)
my_w.mainloop()  # Keep the window open
print(type(4.5))
