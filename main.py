#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        #create select button
        self.month = StringVar()
        self.combobox = ttk.Combobox(master, textvariable=self.month)
        self.combobox.pack()
        self.combobox.config(values=("Jan", "feb", "mar"))
        # set default value
        self.combobox.set("Jan")

        self.year = StringVar()
        self.spinbox = Spinbox(master, from_=1990, to=2017, textvariable=self.year)
        self.spinbox.pack()

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
