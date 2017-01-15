#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        master.option_add('*tearOff', False)  # use this for menu

        self.menubar = Menu(master)
        master.config(menu = self.menubar)

        #create the menus
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.file, label="File")
        self.edit = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.edit, label="Edit")
        self.help_ = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.help_, label="Help")

        # add commands in file
        self.file.add_command(label="New", command= lambda:print('New File') )
        self.file.add_separator()

        self.file.add_command(label="Open...", command=lambda: print('Opening File'))
        self.file.add_command(label="Save", command=lambda: print('Saving File'))

        # add description to "New" command , first one we created
        self.file.entryconfig("New", accelerator = "Ctrl + N")

        # add image
        self.logo = PhotoImage(file="a634dc.png").subsample(100, 100)
        self.file.entryconfig("Open...", image=self.logo, compound="left")

        #delete command
        self.file.delete("Save")

        # add more Menu with child commands
        self.save = Menu(self.file)
        self.file.add_cascade(menu=self.save, label="Save")
        self.save.add_command(label="Save As", command= lambda: print("Saving as..."))
        self.save.add_command(label="Save All", command=lambda: print("Saving All..."))

        self.choice = IntVar()
        self.edit.add_radiobutton(label="One", variable=self.choice, value=1)
        self.edit.add_radiobutton(label="Two", variable=self.choice, value=2)
        self.edit.add_radiobutton(label="Three", variable=self.choice, value=3)


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
