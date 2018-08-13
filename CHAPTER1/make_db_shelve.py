#! python

"""
@author: "Lucky-H"
@file: make_db_shelve
@date: 2018-08-05
@time: 20:25:00
"""


import shelve
from initdata import sue, bob

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
