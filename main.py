import tkinter
from tkinter import ttk

root = tkinter.Tk()
button = tkinter.ttk.Button(root, text="Click me")
button.pack()

print( button["text"] ) #Click me

button.config(text = "Push me") #text becomes Push me
print( button.config() ) #{'class': ('class', '', '', '', ''), 'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'command': ('command', 'command', 'Command', '', ''), 'underline': ('underline', 'underline', 'Underline', -1, -1), 'compound': ('compound', 'compound', 'Compound', <index object: 'none'>, <index object: 'none'>), 'width': ('width', 'width', 'Width', '', ''), 'state': ('state', 'state', 'State', <index object: 'normal'>, <index object: 'normal'>), 'padding': ('padding', 'padding', 'Pad', '', ''), 'default': ('default', 'default', 'Default', <index object: 'normal'>, <index object: 'normal'>), 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'), 'style': ('style', 'style', 'Style', '', ''), 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 'text': ('text', 'text', 'Text', '', 'Push me'), 'image': ('image', 'image', 'Image', '', '')}

label = tkinter.ttk.Label(root, text="Hi all")
label.pack()

root.mainloop()

