from tkinter import *
from translate import Translator
from tkinter import ttk
import googletrans

win = Tk()
win.title("Google Translate")
win.geometry("1010x300")
win.config(bg="blue")

# icon
image_icon = PhotoImage(file="google.png")
win.iconphoto(False, image_icon)

arrow_image = PhotoImage(file="arrow.png")
image_label = Label(win, image=arrow_image, width=150, height=160)
image_label.place(x=430, y=10)

choice1 = StringVar(win)
choice2 = StringVar(win)

choice = {"English", "Hindi", "Gujarati", "Spanish", "German", "French", "Uzbek", "Russian"}

choice1.set("English")
choice2.set("Russian")


def translate():
    translator = Translator(from_choiceg=choice1.get(),
                            to_lang=choice2.get())
    translation = translator.translate(var.get())
    var1.set(translation)


def clear():
    textbox.delete(0, END)
    textbox1.delete(0, END)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

choice1_menu = ttk.Combobox(win, values=languageV, font="Roboto 14", state="r")
choice1_menu.place(x=10, y=100, width=400, height=50)
choice1_menu.set("ENGLISH")

choice1_menu = ttk.Combobox(win, values=languageV, font="Roboto 14", state="r")
choice1_menu.place(x=600, y=100, width=400, height=50)
choice1_menu.set("SELECT LANGUAGE")


var = StringVar()
textbox = Entry(win, textvariable=var, relief=GROOVE, font="Robote 20")
textbox.place(x=10, y=150, width=400, height=100)

var1 = StringVar()
textbox1 = Entry(win, textvariable=var1, relief=GROOVE, font="Robote 20")
textbox1.place(x=600, y=150, width=400, height=100)


button_trans = Button(win, text="Translate", font="Roboto 15 bold italic", activeforeground="purple",
                      cursor="hand2", bd=5, command=translate)
button_trans.place(x=450, y=190)

button_clear = Button(win, text="Clear", font="Roboto 15 bold italic", activeforeground="purple",
                      cursor="hand2", bd=5, command=clear)
button_clear.place(x=470, y=240)


if __name__ == "__main__":
    win.mainloop()















# from tkinter import *
# from tkinter import ttk, messagebox
# from googletrans import Translator
#
# win = Tk()
# win.title("Language Translator")
# win.geometry("590x370")
#
#
# def translate():
#     lang_1 = text_entry1.get(1.0, "end-1c")  # END
#     cl = choose_language.get()
#
#     if lang_1 == '':
#         messagebox.showerror("Language Translator", "Enter the to translate!")
#     else:
#         text_entry2.delete(1.0, "end")
#         translator = Translator()
#         output = translator.translate(lang_1, dest=cl)
#         text_entry2.insert("end", output.text)
#
#
# def clear():
#     text_entry1.delete(1.0, "end")
#     text_entry2.delete(1.0, "end")
#
#
# a = StringVar()
#
# framel = Frame(win, width=590, height=370, relief=RIDGE, borderwidth=5, bg="#F7DC6F")
# framel.place(x=0, y=0)
#
# Label(win, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg="#F7DC6F").pack(pady=10)
#
# auto_select = ttk.Combobox(framel, width=27, textvariable=a, state="randomly", font=("verdana", 10, "bold"))
#
# auto_select["values"] = (
#                             "Auto Select",
#                         )
# auto_select.place(x=15, y=60)
# auto_select.current(0)
#
# l = StringVar()
# choose_language = ttk.Combobox(framel, width=27, textvariable=l, state="randomly", font=("verdana", 10, "bold"))
#
# choose_language["values"] = (
#                             'Afrikaans',
#                             'Albanian',
#                             'Amharic',
#                             'Arabic',
#                             'Armenian',
#                             'Azerbaijani',
#                             'Basque',
#                             'Belarusian',
#                             'Bengali',
#                             'Bosnian',
#                             'Bulgarian',
#                             'Batalan',
#                             'Cebuano',
#                             'Chichewa',
#                             'Chinese (simplified)',
#                             'Chinese (traditional)',
#                             'Corsican',
#                             'Croatian',
#                             'Czech',
#                             'Danish',
#                             'Dutch',
#                             'English',
#                             'Esperanto',
#                             'Estonian',
#                             'Filipino',
#                             'Finnish',
#                             'French',
#                             'Frisian',
#                             'Galician',
#                             'Georgian',
#                             'German',
#                             'Greek',
#                             'Gujarati',
#                             'Haitian creole',
#                             'Hausa',
#                             'Hawaiian',
#                             'Hebrew',
#                             'Hebrew',
#                             'Hindi',
#                             'Hmong',
#                             'Hungarian',
#                             'Icelandic',
#                             'Igbo',
#                             'Indonesian',
#                             'Irish',
#                             'Italian',
#                             'Japanese',
#                             'Javanese',
#                             'Kannada',
#                             'Kazakh',
#                             'Khmer',
#                             'Korean',
#                             'Kurdish (kurmanji)',
#                             'Kyrgyz',
#                             'Lao',
#                             'Latin',
#                             'Latvian',
#                             'Lithuanian',
#                             'Luxembourgish',
#                             'Macedonian',
#                             'Malagasy',
#                             'Malay',
#                             'Malayalam',
#                             'Maltese',
#                             'Maori',
#                             'Marathi',
#                             'Mongolian',
#                             'Myanmar (burmese)',
#                             'Nepali',
#                             'Norwegian',
#                             'Odia',
#                             'Pashto',
#                             'Persian',
#                             'Polish',
#                             'Portuguese',
#                             'Punjabi',
#                             'Romanian',
#                             'Russian',
#                             'Samoan',
#                             'Scots gaelic',
#                             'Serbian',
#                             'Sesotho',
#                             'Shona',
#                             'Sindhi',
#                             'Sinhala',
#                             'Slovak',
#                             'Slovenian',
#                             'Somali',
#                             'Spanish',
#                             'Sundanese',
#                             'Swahili',
#                             'Swedish',
#                             'Sajik',
#                             'Tamil',
#                             'Telugu',
#                             'Thai',
#                             'Turkish',
#                             'Ukrainian',
#                             'Urdu',
#                             'Uyghur',
#                             'Uzbek',
#                             'Vietnamese',
#                             'Welsh',
#                             'Xhosa',
#                             'Yiddish',
#                             'Yoruba',
#                             'Zulu',
#                             )
#
# choose_language.place(x=305, y=60)
# choose_language.current(0)
#
#
# text_entry1 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
# text_entry1.place(x=10, y=100)
#
# text_entry2 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=("verdana", 15))
# text_entry2.place(x=300, y=100)
#
# btn1 = Button(framel, text="Translate", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg="#248aa2",
#               fg="white", cursor="hand2", command=translate)
# btn1.place(x=200, y=300)
#
# btn2 = Button(framel, text="Clear", relief=RAISED, borderwidth=2, font=("verdana", 10, "bold"), bg="#248aa2",
#               fg="white", cursor="hand2", command=clear)
# btn2.place(x=300, y=300)
#
#
# if __name__ == "__main__":
#     win.mainloop()















