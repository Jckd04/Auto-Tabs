from tkinter import *

from logic import open_urls
from classes import profile


def create_profile_frame(parent, profile):
    frame = Frame(
        parent,
        bg = profile.bg_colour
    )
    frame.pack(fill="x", padx=20, pady=20)

    profile_label = Label(
        frame,
        text = profile.name,
        bg = profile.bg_colour
    )
    profile_label.pack(side=LEFT, pady=10, padx=10)

    url_button = Button(
        frame,
        text="Open Tabs",
        bg = profile.bg_colour,
        command=lambda: open_urls(profile.urls)
    )
    url_button.pack(side=RIGHT, pady=10, padx=10)

    return frame


root = Tk()
root.title("Auto Tabs")
root.minsize(width=300, height=200)

  
profiles = [
    profile(
        urls=[
            "https://mail.google.com",
            "https://calendar.google.com",
            "https://github.com",
        ],
        name="Default Profile",
        bg_colour="#f0f0f0"
    )
]

for profile in profiles:
    create_profile_frame(root, profile)

root.mainloop()