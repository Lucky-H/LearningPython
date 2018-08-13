#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: moreplus.py
@date: 2018-08-12
@time: 20:11:09
"""


a = open('/dev/tty')
a.write('Hello tth World!')
b = a.read()
print(b, end='')

