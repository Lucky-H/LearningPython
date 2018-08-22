#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: filters.py
@date: 2018-08-18
@time: 23:37:49
"""


import sys


def filter_files(name, function):
    input = open(name, 'r')
    output = open(name+'.out', 'w')
    for line in input:
        output.write(function(line))
    input.close()
    output.close()


def filter_streams(function):
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        else:
            print(function(line), end='')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        filter_streams(lambda line: line)
    elif len(sys.argv) == 2:
        filter_files(sys.argv[1], lambda line: line)
