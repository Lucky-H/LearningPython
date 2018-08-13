#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: 2-1_more.py
@date: 2018-08-12
@time: 14:53:30
"""


def more(text, numlines=5):
    lines = text.splitlines()
    while lines:
        chunk = lines[: numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('?') not in ['Y', 'y']:
            break


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        more(open(sys.argv[1], 'r').read(), int(sys.argv[2]))
    else:
        more(open(sys.argv[1], 'r').read())

