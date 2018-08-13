#! python

"""
@author： "Lucky-H"
@file: dump_db_pickle.py
@date: 2018-08-04
@time: 23:11:58
"""


import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['pay'])
print(db['tom']['name'])
