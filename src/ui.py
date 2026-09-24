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
    write_profiles_to_csv,
    delete_profile,
    update_profile
)

from classes import (
    Profile
)

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

    edit_button = Button(
        frame,
        text="Edit",
        bg = profile.bg_colour,
        command=lambda: ProfileDialog(root, profiles, profile, frame)
    )
    edit_button.pack(
        side=LEFT,
        pady=WIDGET_PADDING_Y,
        padx=WIDGET_PADDING_X,
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

# class to create a window where the user can input details for a profile
class ProfileDialog:
    def __init__(self, parent, profiles, profile=None, frame=None):
        # create a new dialog window for creating or editing a profile
        self.parent = parent
        self.profiles = profiles
        self.profile = profile
        self.frame = frame
        self.selected_colour = "#FFFFFF"

        
        self.dialog = Toplevel(parent)
        self.dialog.title(f"New {WINDOW_TITLE} Profile")
        self.dialog.transient(parent)

        # name entry field
        self.name_entry = Entry(self.dialog)
        self.name_entry.pack()

        #url entry field
        self.urls_entry = Entry(self.dialog)
        self.urls_entry.pack()

        # colour preview label
        self.colour_preview = Label(
            self.dialog,
            text=self.selected_colour,
            bg=self.selected_colour,
            width=10
        )
        self.colour_preview.pack()

        self.choose_colour_button = Button(
            self.dialog,
            text="Choose Colour",
            command=self.choose_colour
        )
        self.choose_colour_button.pack()


        # if this profile already exists, create a delete button and save button and fill out the forms with the existing profile data
        if self.profile:
            # fill out the forms with the existing profile data
            self.name_entry.insert(0, self.profile.name)
            self.urls_entry.insert(0, ", ".join(self.profile.urls))
            self.selected_colour = self.profile.bg_colour
            self.colour_preview.config(
                text=self.selected_colour,
                bg=self.selected_colour
            )

            # create a delete button and save button
            self.delete_button = Button(
                self.dialog,
                text="Delete Profile",
                command=self.delete_profile
            )
            self.delete_button.pack()
            
            self.save_button = Button(
                self.dialog,
                text="Save Profile",
                command=self.save_profile
            )
            self.save_button.pack()
        # Otherwise, create a create profile button
        else:
            self.create_button = Button(
                self.dialog,
                text="Create Profile",
                command=self.save_profile
            )
            self.create_button.pack()


    def choose_colour(self):
        colour = colorchooser.askcolor(
            title="Choose Background Colour",
            initialcolor=self.selected_colour
        )[1]

        if colour:
            self.selected_colour = colour
            self.colour_preview.config(
                text=colour,
                bg=colour
            )

    def save_profile(self):
        name = self.name_entry.get()
        urls = [
            url.strip()
            for url in self.urls_entry.get().split(",")
        ]

        new_profile = Profile(
            urls=urls,
            name=name,
            bg_colour=self.selected_colour
        )

        if self.profile:
            update_profile(self.profiles, self.profile, new_profile)
            self.frame.destroy()
            create_profile_frame(self.parent, new_profile)
        else:
            self.profiles.append(new_profile)
            write_profiles_to_csv(self.profiles)
            create_profile_frame(self.parent, new_profile)

        self.dialog.destroy()

    def delete_profile(self):
        delete_profile(self.profiles, self.profile)
        self.frame.destroy()
        self.dialog.destroy()
    

# create the main application window
root = Tk()
root.title("Auto Tabs")
root.minsize(width=300, height=200)

# create a button in the main window to open the new profile dialog window
new_profile_button = Button(
    root,
    text="New Profile",
    command=lambda: ProfileDialog(root, profiles)
)
new_profile_button.pack(pady=20)

# populate a list of profiles by reading from the CSV file
profiles = read_profiles_from_csv()

# populate the main window with existing profiles
for existing_profile in profiles:
    create_profile_frame(root, existing_profile)

root.mainloop()