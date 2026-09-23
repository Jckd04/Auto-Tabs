# Created by Jack D on 2024-06-10
# this file contains the logic for the Auto Tabs application.

import webbrowser
import csv
from classes import Profile

# function to open a list of URLs in the default web browser
def open_urls(urls):
    for url in urls:
        webbrowser.open(url)

# function to read profiles from a CSV file and return a list of Profile objects
def read_profiles_from_csv():
    profiles = []
    try:
        with open("profiles.csv", "r") as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True)
            for row in reader:
                name = row[0]
                urls = row[1].split(";")
                bg_colour = row[2]
                profile = Profile(urls, name, bg_colour)
                profiles.append(profile)
    except FileNotFoundError:
        print("profiles.csv file not found.")
    except Exception as e:
        print(f"An error occurred while reading the profiles.csv file: {e}")
    return profiles


