#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.panedWindow = ttk.PanedWindow(master, orient=HORIZONTAL)
        self.panedWindow.pack(fill = BOTH, expand = TRUE)

        self.frame1 = ttk.Frame(self.panedWindow, width=100, height=300, relief= SUNKEN)
        self.frame2 = ttk.Frame(self.panedWindow, width=400, height=400, relief=SUNKEN)
        self.frame3 = ttk.Frame(self.panedWindow, width=50, height=400, relief=SUNKEN)

        self.panedWindow.add(self.frame1, weight=1)
        self.panedWindow.add(self.frame2, weight=1)
        self.panedWindow.add(self.frame3, weight=1)

        self.panedWindow.forget(2) # hides the third frame

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
