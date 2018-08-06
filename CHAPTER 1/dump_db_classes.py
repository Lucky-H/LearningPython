#! python

"""
@author: "Lucky-H"
@file: dump_db_classes
@date: 2018-08-06
@time: 13:21:03
"""


import shelve


db = shelve.open('class-shelve')
for key in db:
    print(key, ' =>\n   ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.last_name())
print(db['tom'].last_name())
