#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: fork-exec.py
@date: 2018-08-20
@time: 23:31:08
"""


import os


def fork_exec():
    parm = 0
    while True:
        parm += 1
        pid = os.fork()
        if pid == 0:
            os.execlp('python', 'python', 'child.py', str(parm))
            assert False, 'error starting program'
        else:
            print('Child is', pid)
        if input() == 'q':
            break


if __name__ == '__main__':
    fork_exec()