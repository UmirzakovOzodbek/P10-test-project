from tkinter import messagebox, END, Tk, Label, Entry, Button, StringVar, OptionMenu
from transliterate import *

window = Tk()
window.title("Translate from Latin to Cyrillic")
window.geometry("700x350")
window.configure(bg="#6E6E7B")


def translate():
    from_ = clicked1.get()
    to_ = clicked2.get()
    text_ = entry1.get()
    if from_ == "Latin" and to_ == "Cyrillic":
        result_text = to_cyrillic(text_)
        res_label = Label(window, width=20, height=-100, text=result_text, borderwidth=10, bg="lightcyan", font="Roboto 13")
        res_label.place(x=425, y=120)
    elif from_ == "Cyrillic" and to_ == "Latin":
        res_text = to_latin(text_)
        res_label = Label(window, width=20, text=res_text, borderwidth=10, bg="lightcyan", font="Roboto 15")
        res_label.place(x=420, y=110)
    else:
        messagebox.showinfo("You choose the same option!!!")


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    clicked1.set("Latin")
    clicked2.set("Cyrillic")


convert_label = Label(window, text="Translate from Latin to Cyrillic and vice versa", font=25, bg="thistle", fg="blue")
convert_label.place(x=200, y=10)


options = [
            "Latin",
            "Cyrillic"
          ]

clicked1 = StringVar()
clicked1.set("Latin")

drop1 = OptionMenu(window, clicked1, *options)
drop1.config(width=20, height=2, bg="#EEEEE0", fg="#2B2B2B", font="Robote 15")
drop1.place(x=20, y=40)
entry1 = Entry(window, width=13, font="Robote 30")
entry1.config(borderwidth=10, bg="lightcyan")
entry1.place(x=4, y=100)

result_btn = Button(window, text="Translate", width=15, bg="thistle", fg="#22228B", command=translate, font="Roboto 15")
result_btn.place(x=280, y=200)

clear_btn = Button(window, text="clear", width=10, bg="red", fg="#22228B", command=clear, font="Roboto 15")
clear_btn.place(x=305, y=240)

clicked2 = StringVar()
clicked2.set("Cyrillic")

drop2 = OptionMenu(window, clicked2, *options)
drop2.config(width=20, height=2, bg="#EEEEE0", fg="#2B2B2B", font="Robote 15")
drop2.place(x=420, y=40)
entry2 = Entry(window, width=12, font="Robote 30")
entry2.config(borderwidth=10, bg="lightcyan")
entry2.place(x=400, y=100)


if __name__ == "__main__":
    window.mainloop()





