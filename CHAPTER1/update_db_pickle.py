#! python

"""
@author： "Lucky-H"
@file: update_db_pickle.py
@date: 2018-08-04
@time: 23:12:14
"""


import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile= open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()



