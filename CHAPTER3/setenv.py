#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: setenv.py
@date: 2018-08-12
@time: 16:32:09
"""


import os
while 1:
    user = input('?')
    if not user:
        break
    os.environ['USER'] = user
    print(os.popen('python3 echoenv.py').read())

