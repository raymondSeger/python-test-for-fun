#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.button = ttk.Button(master, text="Click Me", command=self.button_handler)
        self.button.pack()

    def button_handler(self):
        print("hi all")


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
