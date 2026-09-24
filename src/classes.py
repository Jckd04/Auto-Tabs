# Created by Jack D on 2024-06-10
# this file contains the classes for the Auto Tabs application.

class Profile:
    def __init__(self, urls, name, bg_colour):
        self.name = name
        self.urls = urls
        self.bg_colour = bg_colour

class NewProfileDialog:
    def __init__(self, parent, profiles):
        # create a new dialog window for creating a new profile
        self.parent = parent
        self.profiles = profiles
        self.selected_colour = "#FFFFFF"

        
        self.dialog = Toplevel(parent)
        self.dialog.title(f"New {WINDOW_TITLE} Profile")
        self.dialog.transient(parent)

        self.name_entry = Entry(self.dialog)
        self.name_entry.pack()

        self.urls_entry = Entry(self.dialog)
        self.urls_entry.pack()

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

        self.create_button = Button(
            self.dialog,
            text="Create Profile",
            command=self.create_profile
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

    def create_profile(self):
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

        self.profiles.append(new_profile)
        write_profiles_to_csv(self.profiles)
        create_profile_frame(self.parent, new_profile)

        self.dialog.destroy()