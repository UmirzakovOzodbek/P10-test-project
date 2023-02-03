from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import shutil


def select_video_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_video():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    win.title("Downloading...")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()

    shutil.move(mp4_video, user_path)

    win.title("Download Completed! Download Another Video...")


win = Tk()
win.title("Youtube Video Downloader")
canvas_ = Canvas(win, width=500, height=800)
canvas_.pack()

logo_img = PhotoImage(file="youtube.png")
logo_img = logo_img.subsample(2, 2)
canvas_.create_image(250, 80, image=logo_img)

link_field = Entry(win, width=40, font=("Arial", 15))
link_label = Label(win, text="Enter Video Link Below: ", font=("Arial", 15))

path_label = Label(win, text="Select Path For Download", font=("Arial", 15))
select_btn = Button(win, text="Select Path", bg="crimson", padx=22, pady=5, font=("Arial", 15), command=select_video_path)

canvas_.create_window(250, 280, window=path_label)
canvas_.create_window(250, 330, window=select_btn)

canvas_.create_window(250, 170, window=link_label)
canvas_.create_window(250, 220, window=link_field)

download_btn = Button(win, text="Download Video", bg="green", padx=22, pady=5, font=("Arial", 15), command=download_video)
canvas_.create_window(250, 390, window=download_btn)


if __name__ == "__main__":
    win.mainloop()





















# from tkinter import messagebox, Tk, Label, Entry, Button
# from pytube import YouTube
#
# window = Tk()
# window.title("Youtube downloader")
# window.geometry("700x350")
# window.configure(bg="indianred")
#
#
# youtube_label = Label(window, text="Youtube downloader", font=25, bg="indianred", fg="darkseagreen")
# youtube_label.place(x=250, y=50)
#
# y_label = Label(window, text="Enter url", width=30, font=10, bg="indianred", fg="blue")
# y_label.place(x=30, y=150)
#
# url_entry = Entry(window, width=40)
# url_entry.configure(borderwidth=8, bg="khaki")
# url_entry.place(x=300, y=150)
#
#
# def download():
#     try:
#         url = url_entry.get()
#         YouTube(url).streams.first().download()
#         yt = YouTube(url)
#         yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#     except Exception as e:
#         print(e)
#         messagebox.showinfo("successfully downloaded")
#
#
# result_btn = Button(window, text="download", font=7, bg="olive", fg="blue", command=download)
# result_btn.place(x=250, y=230)
#
#
# if __name__ == "__main__":
#     window.mainloop()

