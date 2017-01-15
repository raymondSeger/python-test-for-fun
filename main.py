#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        # create text field / entry
        self.entry = ttk.Entry(master, width=30)
        self.entry.pack()

        self.entry.insert(0, "Enter your password")
        #everything you type becomes *
        # self.entry.config(show="*")


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
