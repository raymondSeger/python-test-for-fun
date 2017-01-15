#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        #master is the Tk() TopLevel object
        master.title("The title")
        master.title("a")
        #master.state('zoomed') # fullscreen

        # master.resizable(False, False) # cannot be resized

        master.maxsize(640, 480)
        master.minsize(100, 100)



def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
