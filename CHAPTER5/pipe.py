#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: pipe.py
@date: 2018-08-25
@time: 21:26:51
"""


import os, time


def child(pipeout):
    z = 0
    while True:
        time.sleep(z)
        msg = ('Spam %03d' % z).encode()
        os.write(pipeout, msg)
        z = (z + 1) % 5


def parent():
    pipein, pipeout = os.pipe()
    if os.fork():
        while True:
            line = os.read(pipein, 32)
            print('Parent %d got [%s] at %s' %(os.getpid(), line, time.asctime(time.localtime())))
    else:
        child(pipeout)


if __name__ == '__main__':
    parent()