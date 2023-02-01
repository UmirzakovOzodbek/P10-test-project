import csv
import os
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, PhotoImage, Radiobutton, StringVar

from person import Person

win = Tk()
win.title("Hotel Registration")
win.geometry("500x400")
photo = PhotoImage(file="fun1.png")
win.iconphoto(False, photo)

persons = []


def add():
    person = Person(
        fullname_entry.get(),
        dob_entry.get(),
        phone_entry.get(),
        accommodation_entry.get(),
        gender.get(),
        length_of_stay_entry.get(),
        daily_fee_entry.get()
    )
    persons.append(person.get_attrs(as_dict=True))
    messagebox.showinfo("Information", "The data has been added successfully")


def save():
    with open("hotel.csv", "a", newline="\n") as file:
        header = ["Fullname", "DOB", "Phone", "Accommodation", "Gender", "Length of stay", "Daily fee"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize("hotel.csv") == 0:
            csv_writer.writeheader()
        csv_writer.writerows(persons)
        messagebox.showinfo("Information", "Saved successfully")


def clear():
    fullname_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    accommodation_entry.delete(0, END)
    length_of_stay_entry.delete(0, END)
    daily_fee_entry.delete(0, END)


# Fullname
fullname_label = Label(win, text="Fullname: ", padx=20, pady=10)
fullname_label.grid(row=0, column=0)
fullname_entry = Entry(win, width=30, borderwidth=3)
fullname_entry.grid(row=0, column=1)

# DOB - Date of birth
dob_label = Label(win, text="DOB: ", padx=20, pady=10)
dob_label.grid(row=2, column=0)
dob_entry = Entry(win, width=30, borderwidth=3)
dob_entry.grid(row=2, column=1)

# Phone
phone_label = Label(win, text="Phone: ", padx=20, pady=10)
phone_label.grid(row=3, column=0)
phone_entry = Entry(win, width=30, borderwidth=3)
phone_entry.grid(row=3, column=1)

# Gender
gender = StringVar()
GENDER_TYPES = {"male": "Male", "female": "Female"}
gender_label = Label(win, text="Gender: ", padx=20, pady=10)
gender_label.grid(row=4, column=0)
male_radio_btn = Radiobutton(
    win, text=GENDER_TYPES.get("male"), value="male", variable=gender
)
male_radio_btn.place(x=140, y=125)
female_radio_btn = Radiobutton(
    win, text=GENDER_TYPES.get("female"), value="female", variable=gender
)
female_radio_btn.place(x=230, y=125)

# Accommodation
accommodation_label = Label(win, text="Accommodation: ", padx=20, pady=10)
accommodation_label.grid(row=5, column=0)
accommodation_entry = Entry(win, width=30, borderwidth=3)
accommodation_entry.grid(row=5, column=1)

# Length of stay
length_of_stay_label = Label(win, text="Length of stay: ", padx=20, pady=10)
length_of_stay_label.grid(row=6, column=0)
length_of_stay_entry = Entry(win, width=30, borderwidth=3)
length_of_stay_entry.grid(row=6, column=1)

# Daily fee
daily_fee_label = Label(win, text="Daily fee: ", padx=20, pady=10)
daily_fee_label.grid(row=7, column=0)
daily_fee_entry = Entry(win, width=30, borderwidth=3)
daily_fee_entry.grid(row=7, column=1)

# Save button
save_btn = Button(win, text="Save", padx=20, pady=10, command=save)
save_btn.place(x=60, y=280)

# Add button
add_btn = Button(win, text="Add", padx=20, pady=10, command=add)
add_btn.place(x=140, y=280)
# Clear button
clear_btn = Button(win, text="Clear", padx=18, pady=10, command=clear)
clear_btn.place(x=215, y=280)

# Exit button
exit_btn = Button(win, text="Exit", padx=20, pady=10, command=win.quit)
exit_btn.place(x=295, y=280)

if __name__ == "__main__":
    win.mainloop()
