from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import json
import requests

cor0 = "#FFFFFF"  # White
cor1 = "#333333"  # Black
cor2 = "#006400"  # Red

win = Tk()
win.geometry("300x320")
win.title("Converter")
win.configure(bg=cor0)
win.resizable(height=FALSE, width=FALSE)

# Frames
top = Frame(win, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(win, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)
currency = ["UZS", "USD", "EUR", "RUB"]


def convert():
    import requests

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    url = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    headers = {
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com",
        "x-rapidapi-key": "91d8898136msh83f56071c8737b2p1cbab2jsn4413d1661d85"
    }
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)

    for i in data:
        if i['Ccy'] == currency_1 and currency_2 == "UZS":
            float_value = float(i["Rate"])
            amount = float(amount)
            result["text"] = float_value * amount
            break
        elif i['Ccy'] == currency_2 and currency_1 == "UZS":
            float_value = float(i["Rate"])
            amount = float(amount)
            result["text"] = amount / float_value
            break
        elif currency_1 == i['Ccy']:
            for r in data:
                if currency_2 == r['Ccy']:
                    first_value = float(i["Rate"])
                    second_value = float(r["Rate"])
                    result["text"] = first_value / second_value
        else:
            if currency_1 == "UZS" and currency_2 == "UZS":
                result["text"] = float(amount)


# Top frame
icon = Image.open("currency.png")
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=5,
                 padx=13, pady=30, anchor=CENTER, font=("Arial 16 bold"), bg=cor2, fg=cor0)
app_name.place(x=0, y=0)

# Main frame
result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid",
               anchor=CENTER, font=("Ivy 15 bold"), bg=cor0, fg=cor1)
result.place(x=50, y=10)

url = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
headers = {
    "x-rapidapi-host": "currency-converter18.p.rapidapi.com",
    "x-rapidapi-key": "91d8898136msh83f56071c8737b2p1cbab2jsn4413d1661d85"
}
response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

for d in data:
    currency.append(d['Ccy'])


from_label = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief="flat",
                   anchor=NW, font=("Ivy 10 bold"), bg=cor0, fg=cor1)
from_label.place(x=40, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1["values"] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief="flat",
                 anchor=NW, font=("Ivy 10 bold"), bg=cor0, fg=cor1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2["values"] = (currency)
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=155)

button = Button(main, text="Converter", width=19, padx=5, height=1,
                bg=cor2, fg=cor0, font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=210)


if __name__ == "__main__":
    win.mainloop()
