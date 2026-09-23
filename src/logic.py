# Created by Jack D on 2024-06-10
# this file contains the logic for the Auto Tabs application.

import webbrowser

# function to open a list of URLs in the default web browser
def open_urls(urls):
    for url in urls:
        webbrowser.open(url)


