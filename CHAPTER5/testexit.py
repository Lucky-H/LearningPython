#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: testexit.py
@date: 2018-08-23
@time: 23:27:11
"""


def sysexit():
    import sys
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')


def osexit():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')
