#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.canvas = Canvas(master)
        self.canvas.pack()
        self.canvas.config(width=640, height=480)
        self.canvas.create_line(160, 360, 480, 120, fill="blue", width=5)

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
