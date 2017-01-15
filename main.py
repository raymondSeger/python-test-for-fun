#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.notebook = ttk.Notebook(master)
        self.notebook.pack()

        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)

        self.notebook.add(self.frame1, text="One")
        self.notebook.add(self.frame2, text="Two")

        ttk.Button(self.frame1, text="Click Me").pack()

        # add more frame
        self.frame3 = ttk.Frame(self.notebook)
        self.notebook.insert(1, self.frame3, text="Three") #first param is position

        self.notebook.tab(1, state="disabled")
        #self.notebook.tab(1, state="hidden")



def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
