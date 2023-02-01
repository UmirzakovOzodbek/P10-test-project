import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file="fun1.png")
win.iconphoto(False, photo)
# win.config(bg="pink")
win.title("Marshal")
win.geometry("400x500+100+200")
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, True)

"""_Label_"""
# label_1 = tk.Label(win, text='''Hello!\nworld!''',
#                    bg="red",
#                    fg="white",
#                    font=("Arial", 15, "bold"),
#                    padx=20,
#                    pady=40,
#                    width=20,
#                    height=10,
#                    anchor="sw",
#                    relief=tk.RAISED,
#                    bd=10,
#                    justify=tk.LEFT
#                    )
# label_1.pack()


"""_Button_"""
# def say_hello():
#     print("hello")
#
#
# def add_label():
#     label = tk.Label(win, text="new")
#     label.pack()
#
#
# def counter():
#     global count
#     count += 1
#     btn4["text"] = f"Count: {count}"
#
#
# count = 0
#
#
# btn1 = tk.Button(win, text="Hello",
#                  command=say_hello
#                  )
#
# btn2 = tk.Button(win, text="Add new label",
#                  command=add_label
#                  )
#
# btn3 = tk.Button(win, text="Add new label",
#                  command=lambda: tk.Label(win, text="new lambada").pack()
#                  )
#
# btn4 = tk.Button(win, text=f"Count: {count}",
#                  command=counter,
#                  activebackground="blue",
#                  bg="red"
#                  )
#
# btn1.pack()
# btn2.pack()
# btn3.pack()
# btn4.pack()


"""_Grid_"""
# for i in range(5):
#     for j in range(2):
#         tk.Button(win, text=f"Hello {i} {j}").grid(row=i, column=j, stick="we")
#
# win.grid_columnconfigure(0, minsize=200)
# win.grid_columnconfigure(1, minsize=100)


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty entry")


def delete_entry():
    name.delete(0, tk.END)


def submit():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0, tk.END)


tk.Label(win, text="Name:").grid(row=0, column=0, stick="w")
tk.Label(win, text="Password:").grid(row=1, column=0, stick="w")
name = tk.Entry(win)
password = tk.Entry(win, show="*")
name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(win, text="get", command=get_entry).grid(row=2, column=0, sticky="we")
tk.Button(win, text="delete", command=delete_entry).grid(row=2, column=1, sticky="we")
tk.Button(win, text="Submit", command=submit).grid(row=3, column=0, sticky="we")
tk.Button(win, text="insert", command=lambda: name.insert(0, "hello")) \
    .grid(row=2, column=2, stick="we")


win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)


win.mainloop()
