#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: testargv.py
@date: 2018-08-12
@time: 15:59:47
"""


def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts


if __name__ == '__main__':
    from sys import argv
    myargv = getopts(argv)
    if '-i' in myargv:
        print(myargv['-i'])
    print(myargv)

