#! python

"""
@author： "Lucky-H"
@file: tkinter102.py
@date: 2018-08-08
@time: 00:43:16
"""


from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo('Reply', 'Hello ' + name + '!')

top = Tk()
top.title('Echo')

Label(top, text='Enter your name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=lambda :reply(ent.get()))
btn.pack(side=LEFT)
top.mainloop()
