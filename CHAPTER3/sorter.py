#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: sorter.py
@date: 2018-08-12
@time: 19:42:38
"""


import sys
lines = sys.stdin.readlines()
lines.sort()
for line in lines:
    print(line, end='')
