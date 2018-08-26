#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: signal1.py
@date: 2018-08-26
@time: 20:10:33
"""


import sys, signal, time
def now():
    return time.asctime()


def onsignal(signum, stackframe):
    print('Got signal', signum, 'at', now())


if __name__ == '__main__':
    signum = sys.argv[1]
    signal.signal(signum, onsignal)
    while True:
        signal.pause()
