#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: fork1.py
@date: 2018-08-20
@time: 22:42:43
"""


import os


def child():
    print('Hello from child', os.getpid())
    os._exit(0)


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q':
            break


if __name__ == '__main__':
    parent()
