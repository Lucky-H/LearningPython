#! python

"""
@author： "Lucky-H"
@file: update_db_file.py
@date: 2018-08-03
@time: 00:14:27
"""


from make_db_file import storedb, loaddb
db = loaddb()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'tom tom'
storedb(db)

