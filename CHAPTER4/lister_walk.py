#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: lister_walk.py
@date: 2018-08-19
@time: 22:13:57
"""


import sys, os


def lister(root):
    for (thisdir, subshere, fileshere) in os.walk(root):
        print('[' + thisdir + ']')
        for fname in fileshere:
            print(os.path.join(thisdir, fname))
        # subshere.clear()


if __name__ == '__main__':
    lister(os.path.abspath(sys.argv[1]))
