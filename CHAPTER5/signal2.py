#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: signal2.py
@date: 2018-08-26
@time: 22:34:23
"""


import signal, time
def now():
    return time.asctime()


def onsignal(signum, stackframe):
    print('Got alarm', signum, 'at', now())


if __name__ == '__main__':
    while True:
        print('Setting at', now())
        signal.signal(signal.SIGALRM, onsignal)
        signal.alarm(5)
        signal.pause()
