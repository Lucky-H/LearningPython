#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: pipefifo.py
@date: 2018-08-26
@time: 10:35:14
"""


# FIFO


import os, time, sys
filename = 'FIFO'


def child():
    pipeout = os.open(filename, os.O_WRONLY)
    z = 0
    while True:
        time.sleep(z)
        msg = ('spam %03d\n' % z).encode()
        os.write(pipeout, msg)
        z = (z + 1) % 5


def parent():
    pipein = open(filename)
    while True:
        line = pipein.readline()[: -1]
        if line:
            print('Parent %d got "%s" at %s' % (os.getpid(), line, time.asctime(time.localtime())))


if __name__ == '__main__':
    if not os.path.exists(filename):
        os.mkfifo(filename)
    if len(sys.argv) == 1:
        parent()
    else:
        child()