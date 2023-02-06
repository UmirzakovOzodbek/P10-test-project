from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

win = Tk()
win.title("Weather App")
win.geometry("900x500+300+200")
win.resizable(False, False)


def get_weather():
    try:
        city = text_filed.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description_ = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"]-273.15)
        pressure_ = json_data["main"]["pressure"]
        humidity_ = json_data["main"]["humidity"]
        wind_ = json_data["wind"]["speed"]

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        wind.config(text=wind_)
        humidity.config(text=humidity_)
        description.config(text=description_)
        pressure.config(text=pressure_)
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")


# Search box
search_image = PhotoImage(file="search.png")
my_image = Label(image=search_image)
my_image.place(x=20, y=20)

text_filed = Entry(win, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
text_filed.place(x=50, y=40)
text_filed.focus()

search_icon = PhotoImage(file="search_icon.png")
my_image_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=get_weather)
my_image_icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Bottom box
frame_image = PhotoImage(file="box.png")
frame_my_image = Label(image=frame_image)
frame_my_image.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(win, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(win, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Label
label_1 = Label(win, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_1.place(x=120, y=400)

label_2 = Label(win, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_2.place(x=250, y=400)

label_3 = Label(win, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_3.place(x=430, y=400)

label_4 = Label(win, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

wind = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
wind.place(x=120, y=430)
humidity = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
humidity.place(x=280, y=430)
description = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
description.place(x=450, y=430)
pressure = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
pressure.place(x=670, y=430)


if __name__ == "__main__":
    win.mainloop()
