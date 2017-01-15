#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.frame = ttk.Frame(master)
        self.frame.pack()

        self.frame.config(height=100, width=200)
        self.frame.config(relief=RIDGE)

        #put the button in the frame we just created
        self.button1 = ttk.Button(self.frame, text="Click Me")
        self.button1.pack()
        # add padding to the frame
        self.frame.config(padding=(30,15))

        self.labelFrame = ttk.LabelFrame(master, height=100, width=200, text="My Frame")
        self.labelFrame.pack()


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
