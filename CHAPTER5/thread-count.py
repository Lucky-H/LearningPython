#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: thread-count.py
@date: 2018-08-21
@time: 22:35:18
"""


import _thread as thread
import time


stdoutmutex = thread.allocate_lock()
threadsnum = 5
exitsig = [False] * 5


def counter(tid, count, mutex):
    for i in range(count):
        time.sleep(1/(tid + 1))
        with mutex:
            print('[%s] => %s' % (tid, i))
    exitsig[tid] = True


if __name__ == '__main__':
    for i in range(threadsnum):
        thread.start_new_thread(counter, (i, 10, stdoutmutex))
    while not all(exitsig):
        time.sleep(0.25)
    print('Main thread exiting.')
