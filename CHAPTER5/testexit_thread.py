#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: testexit_thread.py
@date: 2018-08-25
@time: 14:48:37
"""


import threading, time, sys
EXITSTAT = 0


def child():
    global EXITSTAT
    EXITSTAT += 1
    threadid = threading.get_ident()
    print('Hello from child', threadid, EXITSTAT)
    raise SystemExit
    # sys.exit()
    print('never reached')


def parent():
    while True:
        try:
            thread = threading.Thread(target=child(), args=())
        except SystemExit:
            pass
        # thread.start()
        print('Parent alive')
        # time.sleep(2)
        if input() == 'q':
            break


if __name__ == '__main__':
    parent()


