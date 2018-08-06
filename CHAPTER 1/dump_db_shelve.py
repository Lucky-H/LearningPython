#! python

"""
@author: "Lucky-H"
@file: dump_db_shelve
@date: 2018-08-05
@time: 20:28:38
"""


import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, ' => ', db[key])

print(db['sue']['name'])
