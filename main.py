#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.button = ttk.Button(master, text="Click Me", command=self.button_handler)
        self.button.pack()

        master.bind("<KeyPress>", self.key_press_handler)

        master.bind("<Control-c>", self.control_c_handler)

    def button_handler(self):
        print("hi all")

    def key_press_handler(self, event):
        print(event.type)
        print(event.widget)
        print(event.char)
        print(event.keysym)
        print(event.keycode)

    def control_c_handler(self, event):
        print('control c pressed')



def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
