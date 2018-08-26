#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: testexit_fork.py
@date: 2018-08-25
@time: 14:21:34
"""


# Only for Unix-like OS


import os, time
EXITSTAT = 0


def child():
    global EXITSTAT
    EXITSTAT += 1
    print('Hello from child world', os.getpid(), EXITSTAT)
    # time.sleep(20)
    os._exit(EXITSTAT)
    print('never reached')


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pid, status = os.wait()
            print('parent got', pid, status, (status >> 8))
        if input() == 'q':
            break


if __name__ == '__main__':
    parent()


