#! python

"""
@author: "Lucky-H"
@file: update_db_shelve
@date: 2018-08-05
@time: 20:44:07
"""


import shelve
from initdata import tom
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue
db['tom'] = tom
db.close()
