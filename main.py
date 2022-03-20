from tkinter import *
from poker import *

def rungame():
    mylabel = Label(text="u ran the rungame function")
    mylabel.pack()

root = Tk()
button = Button(root, text='Click to play', command=rungame)
button.pack()
# root.mainloop()
