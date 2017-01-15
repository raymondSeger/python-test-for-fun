#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        #create checkbox
        self.checkbutton = ttk.Checkbutton(master, text="SPAM?")
        self.checkbutton.pack()

        self.checkbutton2 = ttk.Checkbutton(master, text="SPAM?")
        self.checkbutton2.pack()

        self.radiobutton = ttk.Radiobutton(master, text="SPAM?")
        self.radiobutton.pack()

        self.radiobutton2 = ttk.Radiobutton(master, text="SPAM?")
        self.radiobutton2.pack()

        string_var = StringVar()
        string_var.set("SPAM!")
        print( string_var.get() ) #SPAM!

        # when we check one of the checkbox, both will be the same because both use the same StringVar.
        self.checkbutton.config(variable=string_var, onvalue="SPAM PLEASE", offvalue="BOO SPAM")
        self.checkbutton2.config(variable=string_var, onvalue="SPAM PLEASE", offvalue="BOO SPAM")

        # when we check one of the radiobutton, both will be the same because both use the same StringVar.
        self.radiobutton.config(variable=string_var, )
        self.radiobutton2.config(variable=string_var,)


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
