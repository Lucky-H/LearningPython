#! python

"""
@author: "Lucky-H"
@file: update_db_classes
@date: 2018-08-06
@time: 13:21:30
"""


import shelve


db = shelve.open('class-shelve')
sue = db['sue']
sue.give_raise(0.25)
db['sue'] = sue

tom = db['tom']
tom.give_raise(0.20)
db['tom'] = tom

db.close()
