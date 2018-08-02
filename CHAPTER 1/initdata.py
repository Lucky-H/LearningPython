#! python

"""
@author： "Lucky-H"
@file: make_db_file.py.py
@date: 2018-08-03
@time: 00:11:15
"""

# 记录
bob = {'name': 'Bob Smith', 'age': 43, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

# 数据库
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])
