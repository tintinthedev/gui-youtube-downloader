import customtkinter as ctk
from pytubefix import YouTube

ctk.set_appearance_mode("system")

app = ctk.CTk()
app.geometry("400x240")
app.title("Youtube video downloader")

APP_FONT = ("Ubuntu", 15)

def download_video():
    try:
        video_url = video_url_entry.get()

        if video_url == "":
            download_status_label.configure(text="Please enter a valid URL!", text_color="red")
            return
        
        download_progress_bar.set(0)
        download_progress_label.configure(text="")
        video_download_button.configure(state="disabled")

        yt = YouTube(video_url, on_progress_callback=download_progress_callback)
        video = yt.streams.get_highest_resolution()

        download_status_label.configure(text=f"Downloading {yt.title}...", text_color="yellow")
        download_status_label.update()

        video.download()

        download_status_label.configure(text="Download finished!", text_color="green")
        video_download_button.configure(state="normal")
    except:
        download_status_label.configure(text="Download error! Maybe your URL is invalid?", text_color="red")
        video_download_button.configure(state="normal")

def download_progress_callback(stream, chunk, bytes_remaining):
    video_size = stream.filesize
    downloaded_amount = video_size - bytes_remaining
    downloaded_percentage = (downloaded_amount / video_size) * 100
    download_progress_bar.set(downloaded_percentage/100)
    download_progress_label.configure(text=f"{int(downloaded_percentage)}%")
    download_progress_bar.update()
    download_progress_label.update()
    

video_url_entry = ctk.CTkEntry(master=app, placeholder_text="YouTube URL", width=220, font=APP_FONT)
download_status_label = ctk.CTkLabel(master=app, text="", font=APP_FONT)
video_download_button = ctk.CTkButton(master=app, text="Download video", command=download_video, font=APP_FONT)
download_progress_bar = ctk.CTkProgressBar(master=app, width=200)
download_progress_bar.set(0)
download_progress_label = ctk.CTkLabel(master=app, text="")

# Displaying widgets on screen
video_url_entry.pack(pady=20)
video_download_button.pack(pady=20)
download_status_label.place(x=20, y=200)
download_progress_label.pack()
download_progress_bar.pack()

app.mainloop()