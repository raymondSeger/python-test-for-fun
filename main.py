#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        # messagebox.showinfo(title="the title",message="The message")
        # messagebox.showerror(title="the title", message="The message")
        # messagebox.showwarning(title="the title", message="The message")

        #value = messagebox.askyesno(title="THe title", message="The message")
        # print(value) # true or false

        # filename = filedialog.askopenfile()
        # print(filename)  # the location

        tuple_returned = colorchooser.askcolor()

        #((152.59375, 172.671875, 149.58203125), '#98ac95')
        # first is the RGB, the second is the hex
        print(tuple_returned)



def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
