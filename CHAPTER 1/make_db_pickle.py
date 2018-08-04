#! python

"""
@author： "Lucky-H"
@file: make_db_pickle.py
@date: 2018-08-04
@time: 23:06:42
"""


from initdata import db
import pickle
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()