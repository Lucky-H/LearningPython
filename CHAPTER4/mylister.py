#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: mylister.py
@date: 2018-08-19
@time: 22:58:59
"""


import sys, os


def mylister(root):
    print('[' + root + ']')
    for file in os.listdir(root):
        file = os.path.join(root, file)
        if not os.path.isdir(file):
            print(file)
        else:
            mylister(file)


if __name__ == '__main__':
    mylister(os.path.abspath(sys.argv[1]))
    # mylister(os.path.abspath('..'))


