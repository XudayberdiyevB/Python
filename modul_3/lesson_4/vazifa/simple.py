import csv
import os
import tkinter as tk
from tkinter import StringVar, Tk, Radiobutton, messagebox, END
from tkcalendar import DateEntry
from datetime import datetime

from student import Student
from Python.python_exceptions import write_exceptions

window = Tk()

window.title("P10 Registration")
width = 600
height = 500
window.geometry(f"{width}x{height}")

students = []


def toggle_state():
    lst = [fullname_entry, email_entry, phone_entry, course_entry]
    count = 0
    for i in lst:
        if len(i.get()) != 0:
            count += 1
    if count == 3:
        print("Yes")
        save_btn['state'] = 'normal'

    else:
        print("NO")
        save_btn['state'] = 'disabled'


check = window.register(toggle_state)


def add():
    student = Student(
        fullname_entry.get(),
        email_entry.get(),
        dob_entry.get(),
        gender.get(),
        phone_entry.get(),
        course_entry.get(),
        datetime.now()
    )
    students.append(student.get_attrs(as_dict=True))
    messagebox.showinfo("Information", "The data has been added successfully")


def save():
    try:
        with open("students.csv", "a", newline="\n") as file:
            header = ["Fullname", "Email", "DOB", "Gender", "Phone", "Course", "DOJ"]
            csv_writer = csv.DictWriter(file, header)
            if os.path.getsize("students.csv") == 0:
                csv_writer.writeheader()
            csv_writer.writerows(students)
    except FileNotFoundError as e:
        write_exceptions(e)
    messagebox.showinfo("Information", "Successfully")
    students.clear()
    clear()


def clear():
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    course_entry.delete(0, END)


def info():
    window_2 = Tk()
    window_2.title("Students Info")
    window_2.geometry("1000x600")
    lst = ["Fullname", "Email", "DOB", "Gender", "Phone", "Course", "DOJ"]
    count = 0
    student_count = 0
    try:
        with open("students.csv") as files:
            file = csv.reader(files)
            for i in file:
                for j in range(1, len(i)):
                    k = tk.Label(window_2, text=f"{i[count]}")
                    k.grid(column=count, row=student_count)
                    count += 1
                student_count += 1
    except FileNotFoundError as e:
        write_exceptions(e)


# Full name
fullname_label = tk.Label(window, text="Your name: ", font="Arial")
fullname_label.place(x=165, y=10)
fullname_entry = tk.Entry(window, width=20, validate="key", validatecommand=check)
fullname_entry.place(x=250, y=10)

# Email
email_label = tk.Label(window, text="Email: ", font="Arial")
email_label.place(x=200, y=40)
email_entry = tk.Entry(window, width=20, validate="key", validatecommand=check)
email_entry.place(x=250, y=40)

# DOB: Date of birth
dob_label = tk.Label(window, text="DOB: ", font="Arial")
dob_label.place(x=205, y=70)
dob_entry = DateEntry(window)
dob_entry.place(x=250, y=70, width=170)

# Gender
gender = StringVar()
GENDER_TYPES = {"male": "Male", "female": "Female"}
gender_label = tk.Label(window, text="Gender: ", font="Arial")
gender_label.place(x=185, y=100)
male_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("male"), value="male", variable=gender
)
male_radio_btn.place(x=350, y=100)
female_radio_btn = Radiobutton(
    window, text=GENDER_TYPES.get("female"), value="female", variable=gender
)
female_radio_btn.place(x=250, y=100)

# Phone
phone_label = tk.Label(window, text="Phone: ", font="Arial")
phone_label.place(x=190, y=130)
phone_entry = tk.Entry(window, width=20, validate="key", validatecommand=check)
phone_entry.place(x=250, y=130)

# Course
course_label = tk.Label(window, text="Course: ", font="Arial")
course_label.place(x=185, y=160)
course_entry = tk.Entry(window, width=20, validate="key", validatecommand=check)
course_entry.place(x=250, y=160)

# Save button
save_btn = tk.Button(window, text="Save", font="Arial", command=save)
save_btn.place(x=160, y=190)

# Add button
add_btn = tk.Button(window, text="Add", font="Arial", command=add)
add_btn.place(x=240, y=190)

# Clear button
clear_btn = tk.Button(window, text="Clear", font="Arial", command=clear)
clear_btn.place(x=315, y=190)

# Exit button
exit_btn = tk.Button(window, text="Exit", font="Arial", command=window.destroy)
exit_btn.place(x=400, y=190)

# Info button
info_btn = tk.Button(window, text="Info", font="Arial", command=info)
info_btn.place(x=475, y=190)

if __name__ == "__main__":
    window.mainloop()
