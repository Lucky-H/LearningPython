#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: multi1.py
@date: 2018-08-26
@time: 23:30:27
"""


import os, multiprocessing


def whoami(label, lock):
    with lock:
        print('%s: name:%s, pid:%s' % (label, __name__, os.getpid()))


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    whoami('function call', lock)


    p = multiprocessing.Process(target=whoami, args=('spaured chile', lock))
    p.start()
    p.join()


    for i in range(5):
        multiprocessing.Process(target=whoami, args=('run process %s' % i, lock)).start()

    with lock:
        print('Main process exit.')
