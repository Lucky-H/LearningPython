#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: pipes-testchild.py
@date: 2018-08-25
@time: 23:23:25
"""


import os, time, sys
mypid = os.getpid()
parentid = os.getppid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' % (mypid, parentid, sys.argv[1]))

for i in range(2):
    time.sleep(3)
    revc = input()
    time.sleep(3)
    send = 'Child %d got: [%s]' % (mypid, revc)
    print(send)
    sys.stdout.flush()
