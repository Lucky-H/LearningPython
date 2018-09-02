#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: multi5.py
@date: 2018-08-27
@time: 21:10:00
"""


import os, multiprocessing


def runprogram(arg):
    os.execlp('python', 'python', 'child.py', str(arg))


if __name__ == '__main__':
    for i in range(5):
        multiprocessing.Process(target=runprogram, args=(i, )).start()

    print('parent exit.')