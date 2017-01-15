#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.progressbar = ttk.Progressbar(master, orient=HORIZONTAL, length=200)
        self.progressbar.pack()
        self.progressbar.config(mode='indeterminate')
        self.progressbar.start()
        #self.progressbar.stop()

        self.progressbar2 = ttk.Progressbar(master, orient=HORIZONTAL, length=200)
        self.progressbar2.pack()
        self.progressbar2.config(mode='determinate', maximum=11.0, value=4.2)

        # create scale
        value = DoubleVar()
        self.scale = ttk.Scale(master, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=11.0)
        self.scale.pack()
        self.scale.set(11.0)

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
