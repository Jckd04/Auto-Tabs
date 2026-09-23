from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Auto Tabs")
root.minsize(width=300, height=200)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frm = ttk.Frame(root, padding=10)
frm.grid(column=0, row=0, sticky=(N, W, E, S))

frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)


ttk.Label(frm, text="Hello World!").grid(
    column=0,
    row=0
)

ttk.Button(frm, text="Quit", command=root.destroy).grid(
    column=1,
    row=1
)

root.mainloop()