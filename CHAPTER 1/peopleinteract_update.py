#! python

"""
@author： "Lucky-H"
@file: peopleinteract_update.py
@date: 2018-08-06
@time: 22:57:28
"""


import shelve
from person import Person
fieldname = ('name', 'age', 'job', 'pay')
db = shelve.open('class-shelve')


while True:
    key = input('\nkey? => ')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldname:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, newtext)
    db[key] = record
db.close()
