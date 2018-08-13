#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: adder.py
@date: 2018-08-12
@time: 19:46:40
"""


import sys
sum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        sum += int(line)
print(sum)

