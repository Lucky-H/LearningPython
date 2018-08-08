#! python

"""
@author： "Lucky-H"
@file: peoplegui.py
@date: 2018-08-08
@time: 21:35:23
"""


from tkinter import *
from tkinter.messagebox import showerror
import shelve
fieldnames = ('name', 'age', 'pay', 'job')
enties = {}
db = {}


def makewidget():
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        enties[label] = ent
    Button(window, text='Fetch', command=fetch_record).pack(side=LEFT)
    Button(window, text='Update', command=update_record).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window


def fetch_record():
    key = enties['key'].get()
    try:
        record = db[key]
    except:
        showerror('Error', 'No such key!')
    else:
        for field in fieldnames:
            enties[field].delete(0, END)
            enties[field].insert(0, repr(getattr(record, field)))

def update_record():
    key = enties['key'].get()
    if key in db:
        record = db[key]
    else:
        from person import Person
        record = Person(name='?', age='?')
    for field in fieldnames:
        setattr(record, field, eval(enties[field].get()))
    db[key] = record


if __name__ == '__main__':
    db = shelve.open('class-shelve')
    window = makewidget()
    window.mainloop()
    db.close()
