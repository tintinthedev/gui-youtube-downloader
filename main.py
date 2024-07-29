import customtkinter
from pytubefix import YouTube

customtkinter.set_appearance_mode("system")

app = customtkinter.CTk()
app.geometry("400x240")
app.title("Youtube video downloader")

APP_FONT = ("Ubuntu", 15)

app.mainloop()