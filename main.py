#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hello, Tkinter!").pack()

        ttk.Button(master, text = "Texas", command = self.texas_hello).pack()

        ttk.Button(master, text = "Hawaii", command = self.hawaii_hello).pack()

        self.label2 = ttk.Label(master, text="Hawaii HawaiiHawaii HawaiiHawaiiHawaiiHawaiiHawaiiHawaiiHawaiiHawaiiHawaiiHawaiiHawaiiHawaii")
        self.label2.config(wraplength=150) # 150 width/chars wrapping
        self.label2.config(justify=CENTER) #textalign center
        self.label2.config(foreground='blue', background='yellow')
        self.label2.img = PhotoImage(file='a634dc.png')
        self.label2.config(image=self.label2.img, compound='left')

        self.label2.pack()

    #changes the text when button clicked
    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    # changes the text when button clicked
    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
