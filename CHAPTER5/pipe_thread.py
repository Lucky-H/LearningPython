#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: pipe_thread.py
@date: 2018-08-25
@time: 22:28:28
"""


import os, time, threading


def child(pipeout):
    z = 0
    while True:
        time.sleep(z)
        msg = ('Spam [%d]\n' % z).encode()
        os.write(pipeout, msg)
        z = (z + 1) % 5


def parent(pipein):
    pipein = os.fdopen(pipein)
    while True:
        line = pipein.readline()[: -1]
        print('Parent %i got [%s] at %s' % (os.getpid(), line, time.asctime(time.localtime())))


if __name__ == '__main__':
    pipein, pipeout = os.pipe()
    threading.Thread(target=child, args=(pipeout,)).start()
    parent(pipein)
