#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):
        self.treeview = ttk.Treeview(master)
        self.treeview.pack()

        self.treeview.insert('', '0', 'item1', text="First Item")
        self.treeview.insert('', '1', 'item2', text="Second Item")
        self.treeview.insert('', 'end', 'item3', text="Third Item")

        self.logo = PhotoImage(file="a634dc.png").subsample(100,100)
        # insert this treeview inside item2, which is in position 1
        self.treeview.insert('item2', 'end', 'python', text="Python", image=self.logo)
        self.treeview.item('item2', open=True) #open by default

        self.treeview.move('item1', 'item2', 'end') #put item 1 to item2, and puts it at the end index


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if(__name__ == "__main__"):
    main()
