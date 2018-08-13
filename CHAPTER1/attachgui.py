#! python

"""
@author： "Lucky-H"
@file: attachgui.py
@date: 2018-08-07
@time: 23:09:43
"""


from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()
    def reply(self):
        showinfo('popup', 'Button pressed!')

if __name__ == '__main__':
    mainwin = Tk()
    Label(mainwin, text=__name__).pack()

    popup = Toplevel()
    Label(popup, text='attach').pack(side=LEFT)
    MyGui(popup).pack(side=RIGHT)

    mainwin.mainloop()
