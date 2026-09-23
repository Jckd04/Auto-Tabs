import webbrowser

def open_urls(urls):
    for url in urls:
        webbrowser.open(url)

def create_profile(name, urls, bg_colour):
    return profile(urls, name, bg_colour)