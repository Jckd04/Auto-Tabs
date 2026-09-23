# Auto-Tabs

A small Python/Tkinter application for opening groups of URLs

## Features

- Create profiles with a name, URLs and a background colour
- Displays each profile in its own frame
- Open all URLs in a profile in one button
- Load profiles from a CSV file

#### yet to come

- a colour selecter
- Saving created profiles to csv
- automatically launch certain pages on startup
- editing, copying and deleting profiles
- export as a .exe file to launch the profile via a quick search
- packaged as an application
- url validation


## Requiremnts

- Python 3
- Tkinter

## Running the Application

From the project root:

```Termianl
python ui.py
```

## Profiles File

Profiles are stored in profiles.csv in the project root.
Each row uses this format
```
Profile Name,url1;url2;url3,#f0f0f0
```

```Example
Default Profile,https://mail.google.com;https://calendar.google.com;https://github.com,#f0f0f0
```
URLs are seperated by semicolons. The final value is the profile background colour as a hex.

## Project Structure
```
Auto-Tabs/
├── profiles.csv
├── README.md
└── src/
    ├── classes.py
    ├── logic.py
    ├── styles.py
    └── ui.py
```

ui.py: Creates the Tkinter windows, frames, labels and buttons
logic.py: Loads profiles and opens URLs
Classes.py: Defines the Profile class
styles.py: Stores the shared UI styling values
profiles.csv: Srores saved profiles
