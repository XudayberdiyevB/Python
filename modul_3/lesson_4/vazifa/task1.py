import tkinter as tk
from datetime import date

window = tk.Tk()
window.title("Age calculator")
window.geometry("500x600")


def calculate_age():
    year = birth_year_entry.get().split("/")
    import datetime
    a = datetime.date(year=int(year[-1]), month=int(year[-2]), day=int(year[-3]))
    b = date.today()
    text = int((b - a).days / (365.2425))
    info["text"] = f" Your age {text}"


birth_year = tk.Label(window, text="Enter birth year:")
birth_year.grid(column=0, row=0)
birth_year_entry = tk.Entry(window)
birth_year_entry.grid(column=1, row=0)

print(birth_year_entry.get())

calculate_btn = tk.Button(window, text="Calculate age", command=calculate_age)
calculate_btn.grid(column=0, row=1)

info = tk.Label(window)
info.grid(column=0, row=3)
window.mainloop()
