#! python

"""
@author: "Lucky-H"
@file: make_db_classes
@date: 2018-08-06
@time: 13:16:06
"""


import shelve
from person import Person
from manager import Manager


bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)
db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()