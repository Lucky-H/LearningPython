#! python

"""
@author： "Lucky-H"
@file: peopleinteract_query
@date: 2018-08-06
@time: 22:26:04
"""


import shelve
fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')


while True:
    key = input('\nKey? => ')
    if not key:
        break
    try:
        record = db[key]
    except:
        print('No such key "%s"!' % key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
db.close()