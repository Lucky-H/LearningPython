#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: pipe2.py
@date: 2018-08-25
@time: 21:42:41
"""


import os, time


def child(pipeout):
    z = 0
    while True:
        time.sleep(z)
        msg = ('Spam %03d\n' % z).encode()
        os.write(pipeout, msg)
        z = (z + 1) % 5


def parent():
    pipein, pipeout = os.pipe()
    if os.fork():
        os.close(pipeout)
        pipein = os.fdopen(pipein)
        while True:
            line = pipein.readline()[: -1]
            try:
                print('Parent %d got [%s] at %s' % (os.getpid(), line, time.asctime(time.localtime())))
                # raise ValueError
            except Exception as e:
                print('Exception:', repr(e))
                pass
    else:
        os.close(pipein)
        child(pipeout)


if __name__ == '__main__':
    parent()
