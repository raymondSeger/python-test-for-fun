#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.button1 = ttk.Button(master, text="Button 1")
        self.button1.pack()
        self.button2 = ttk.Button(master, text="Button 2")
        self.button2.pack()

        self.style = ttk.Style()

        # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        print(self.style.theme_names())

        self.style.theme_use('winnative')

        # set defaults for TTK
        print( self.button1.winfo_class() )  #TButton
        self.style.configure('TButton', foreground="blue")

        # create "CSS class" and use it for a button
        self.style.configure('Alarm.TButton', foreground="orange", font=("Arial", 24, 'bold'))
        self.button2.config(style="Alarm.TButton")

        # add style for pressed state / disabled state
        self.style.map("Alarm.TButton", foreground=[('pressed', 'pink'), ('disabled', 'grey')])
        # self.button2.state(['disabled'])

        # get all the states
        """
        [('Button.border',
          {'children': [('Button.padding', {'children': [('Button.label', {'sticky': 'nswe'})], 'sticky': 'nswe'})],
           'sticky': 'nswe'})]
        """
        print( self.style.layout('TButton') )


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
