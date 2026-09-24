# Created by Jack D on 2024-06-10
# this file contains the UI logic for the Auto Tabs application.

#import the necessary modules
from tkinter import (
    Tk,
    Frame,
    Label,
    Button,
    Entry,
    Toplevel,
    LEFT,
    RIGHT,
    colorchooser
)

from logic import (
    open_urls,
    read_profiles_from_csv,
    write_profiles_to_csv
)

from classes import Profile

from styles import (
    PROFILE_FONT,
    PROFILE_PADDING_X,
    PROFILE_PADDING_Y,
    WIDGET_PADDING_X,
    WIDGET_PADDING_Y,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_TITLE,
)

def create_profile_frame(parent, profile):
    # create a frame for the profile with the specified background colour
    frame = Frame(
        parent,
        bg = profile.bg_colour
    )
    frame.pack(
        fill="x",
        padx=PROFILE_PADDING_X,
        pady=PROFILE_PADDING_Y,
    )

    profile_label = Label(
        frame,
        text = profile.name,
        bg = profile.bg_colour,
        font=PROFILE_FONT,
    )
    profile_label.pack(
        side=LEFT,
        pady=WIDGET_PADDING_Y,
        padx=WIDGET_PADDING_X,
    )

    # create a button to open the URLs associated with the profile and pack it to the right of the frame
    url_button = Button(
        frame,
        text="Open Tabs",
        bg = profile.bg_colour,
        command=lambda: open_urls(profile.urls)
    )
    url_button.pack(
        side=RIGHT,
        pady=WIDGET_PADDING_Y,
        padx=WIDGET_PADDING_X,
    )

    return frame

# function to create a window where the user can input details for a new profile
def new_profile_window():

    selected_colour = "#FFFFFF"  # default colour

    def choose_colour():
        nonlocal selected_colour

        colour_code = colorchooser.askcolor(
            title="Choose Background Colour",
            initialcolor=selected_colour
        )

        if colour_code[1]:  # If a colour was selected
            selected_colour = colour_code[1]
            colour_preview.config(bg=selected_colour)
    

    # function to create a new profile from the form inputs
    def create_profile_from_form():

        # get the values from the form entries
        name = name_entry.get()
        urls = [
            url.strip() for url in urls_entry.get().split(",")
        ]
        bg_colour = selected_colour

        # create a new profile instance with the provided values
        new_profile = Profile(
            urls=urls,
            name=name,
            bg_colour=bg_colour
        )

        # create a new profile frame in the main window for the newly created profile
        create_profile_frame(root, new_profile)
        write_profiles_to_csv(profiles + [new_profile])  # Save the new profile to the CSV file
        dialog.destroy()
    
    # create a new top-level window for the new profile dialog
    dialog = Toplevel(root)
    dialog.title(f"New {WINDOW_TITLE} Profile")
    dialog.transient(root)

    # Name field
    name_frame = Frame(dialog)
    name_frame.pack(pady=WIDGET_PADDING_Y)

    name_label = Label(name_frame, text="Profile Name:")
    name_label.pack(side=LEFT, padx=WIDGET_PADDING_X)

    name_entry = Entry(name_frame)
    name_entry.pack(side=RIGHT, padx=WIDGET_PADDING_X)

    # URLs field
    urls_frame = Frame(dialog)
    urls_frame.pack(pady=WIDGET_PADDING_Y)

    urls_label = Label(urls_frame, text="URLs (comma-separated):")
    urls_label.pack(side=LEFT, padx=WIDGET_PADDING_X)

    urls_entry = Entry(urls_frame)
    urls_entry.pack(side=RIGHT, padx=WIDGET_PADDING_X)

    # Background Colour field
    bg_colour_frame = Frame(dialog)
    bg_colour_frame.pack(pady=WIDGET_PADDING_Y)

    bg_colour_label = Label(bg_colour_frame, text="Background Colour:")
    bg_colour_label.pack(side=LEFT, padx=WIDGET_PADDING_X)

    colour_preview = Label(bg_colour_frame, text=selected_colour, bg=selected_colour, width=10)
    colour_preview.pack(side=LEFT, padx=WIDGET_PADDING_X)



    choose_colour_button = Button(bg_colour_frame, text="Choose Colour", command=choose_colour)
    choose_colour_button.pack(side=RIGHT, padx=WIDGET_PADDING_X)

    # create a button to submit the form and create the new profile
    create_profile_button = Button(
        dialog,
        text="Create Profile",
        command= create_profile_from_form
    )
    create_profile_button.pack(pady=WIDGET_PADDING_Y)

    

# create the main application window
root = Tk()
root.title("Auto Tabs")
root.minsize(width=300, height=200)

# create a button in the main window to open the new profile dialog window
new_profile_button = Button(
    root,
    text="New Profile",
    command=new_profile_window
)
new_profile_button.pack(pady=20)

# populate a list of profiles by reading from the CSV file
profiles = read_profiles_from_csv()

# populate the main window with existing profiles
for existing_profile in profiles:
    create_profile_frame(root, existing_profile)

root.mainloop()