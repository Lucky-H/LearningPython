#! python

"""
@author： "Lucky-H"
@file: dump_db_file.py
@date: 2018-08-04
@time: 22:45:11
"""


from make_db_file import loaddb
db = loaddb()
for key in db:
    print(key, '=>\n', db[key])
    print(db['sue']['pay'])
    print(db['tom']['name'])

