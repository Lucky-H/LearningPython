#! python

"""
@author： "Lucky-H"
@file: customizegui.py
@date: 2018-08-07
@time: 23:41:50
"""


from tkinter import mainloop
from tkinter.messagebox import showinfo
from attachgui import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo('popup', 'Ouch!')


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
