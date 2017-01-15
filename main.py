#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.entry = ttk.Entry(master)
        self.entry.pack()

        # bind to copy event
        self.entry.bind("<<Copy>>", lambda e:print("Copy") )
        #bind to paste event
        self.entry.bind("<<Paste>>", lambda e:print("Paste") )


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
