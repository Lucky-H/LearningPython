#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: child.py
@date: 2018-08-20
@time: 23:37:10
"""


import os, sys
print('Hello from child', os.getpid(), sys.argv[1])
