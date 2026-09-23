from tkinter import *
from tkinter import ttk

from logic import open_urls


root = Tk()
root.title("Auto Tabs")
root.minsize(width=300, height=200)

class profile:
    def __init__(self, urls, name):
        self.name = name
        self.urls = urls
    
profile = profile(
    urls=[
        "https://mail.google.com",
        "https://calendar.google.com",
        "https://github.com",
    ],
    name="Default Profile"
)

profile_label = ttk.Label(
    root,
    text=f"Profile: {profile.name}",
    font=("Arial", 14)

).pack(pady=10)

url_button = ttk.Button(
    profile_label,
    text="Open Tabs",
    command=lambda: open_urls(profile.urls)

).pack(pady=20)

root.mainloop()