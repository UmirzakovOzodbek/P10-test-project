import tkinter as tk
import datetime as date

win = tk.Tk()
photo = tk.PhotoImage(file="fun1.png")
win.iconphoto(False, photo)
# win.config(bg="pink")
win.title("Marshal")
win.geometry("400x500+100+200")
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)


def make_calc_age():
    year = int(birth_year_entry.get())
    if year <= 0 or year >= 2023:
        year_label1['text'] = 'Error'
    else:
        age = 2023 - year
        year_label1['text'] = age


# Age calculator
label_1 = tk.Label(win, text="Age calculator", fg="#FF4D00")
label_1.pack()

# Birth year
birth_year_label = tk.Label(win, text="Birth year:")
birth_year_label.place(x=10, y=45)
birth_year_entry = tk.Entry(win, width=20)
birth_year_entry.place(x=75, y=45)

# Calculate age
label_1 = tk.Label(win, text="Calculate age", bg="green")
label_1.place(x=10, y=105)

# Your age
year_label = tk.Label(win, text="Your age:")
year_label.place(x=10, y=135)
# year_entry = tk.Entry(win, width=20)
# year_entry.place(x=75, y=135)
year_label1 = tk.Label(win, text="____")
year_label1.place(x=75, y=135)

# Enter
enter_btn = tk.Button(win, text="Enter", padx=85, pady=1, command=make_calc_age)
enter_btn.place(x=10, y=75)


if __name__ == "__main__":
    win.mainloop()

