#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: fork-count.py
@date: 2018-08-20
@time: 22:52:56
"""


import os, time


def counter(count):
    for j in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), j))
    os._exit(0)


if __name__ == '__main__':
    for i in range(5):
        pid = os.fork()
        if pid == 0:
            counter(5)
        else:
            print('process %s spawned' % pid)
    print('Main process exiting.')
