#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: testecho.py
@date: 2018-09-01
@time: 23:38:49
"""


import multiprocessing, os


def exec(*args):
    # print(['python', 'echo_client.py'] + list(args))
    os.execvp('python', ['python', 'echo_client.py'] + list(args))


def multip(num):
    ps = []
    for i in range(num):
        p = multiprocessing.Process(target=exec, args=('localhost', 'hello net world', str(i)))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()


if __name__ == '__main__':
    print('parallel client test')
    multip(8)
    print('END!')
