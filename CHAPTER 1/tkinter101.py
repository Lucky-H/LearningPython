#! python

"""
@author: "Lucky-H"
@file: tkinter
@date: 2018-08-07
@time: 12:49:44
"""


import tkinter
from tkinter.messagebox import showinfo

def reply():
    showinfo('popup', 'Button pressed!')

window = tkinter.Tk()
button = tkinter.Button(window, text='press', command=reply)
button.pack()
window.mainloop()

