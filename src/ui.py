from tkinter import *

from logic import open_urls, create_profile
from classes import Profile


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

def new_profile_window():
    dialog = Toplevel(root)
    dialog.title("New Profile")
    dialog.transient(root)

    # Name field
    name_frame = Frame(dialog)
    name_frame.pack(pady=10)

    name_label = Label(name_frame, text="Profile Name:")
    name_label.pack(side=LEFT, padx=10)

    name_entry = Entry(name_frame)
    name_entry.pack(side=RIGHT, padx=10)

    # URLs field
    urls_frame = Frame(dialog)
    urls_frame.pack(pady=10)

    urls_label = Label(urls_frame, text="URLs (comma-separated):")
    urls_label.pack(side=LEFT, padx=10)

    urls_entry = Entry(urls_frame)
    urls_entry.pack(side=RIGHT, padx=10)

    # Background Colour field
    bg_colour_frame = Frame(dialog)
    bg_colour_frame.pack(pady=10)

    bg_colour_label = Label(bg_colour_frame, text="Background Colour:")
    bg_colour_label.pack(side=LEFT, padx=10)

    bg_colour_entry = Entry(bg_colour_frame)
    bg_colour_entry.pack(side=RIGHT, padx=10)


    def create_profile_from_form():

        name = name_entry.get()
        urls = [
            url.strip() for url in urls_entry.get().split(",")
        ]
        bg_colour = bg_colour_entry.get()

        new_profile = Profile(
            urls=urls,
            name=name,
            bg_colour=bg_colour
        )

        create_profile_frame(root, new_profile)
        dialog.destroy()

    create_profile_button = Button(
        dialog,
        text="Create Profile",
        command=create_profile_from_form
    )
    create_profile_button.pack(pady=10)
    

root = Tk()
root.title("Auto Tabs")
root.minsize(width=300, height=200)

new_profile_button = Button(
    root,
    text="New Profile",
    command=new_profile_window
)
new_profile_button.pack(side=BOTTOM, pady=20)

profiles = [
    Profile(
        urls=[
            "https://mail.google.com",
            "https://calendar.google.com",
            "https://github.com",
        ],
        name="Default Profile",
        bg_colour="#f0f0f0"
    )
]

for existing_profile in profiles:
    create_profile_frame(root, existing_profile)

root.mainloop()