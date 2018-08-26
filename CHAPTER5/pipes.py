#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: pipes.py
@date: 2018-08-25
@time: 22:46:08
"""


# bind pipe to stdin/stdout


import os, sys


def spawn(prop, *args):
    stdin_fd = sys.stdin.fileno()
    stdout_fd = sys.stdout.fileno()

    parentin, childout = os.pipe()
    childin, parentout = os.pipe()

    if os.fork():
        os.close(childin)
        os.close(childout)
        os.dup2(parentin, stdin_fd)
        os.dup2(parentout, stdout_fd)
    else:
        os.close(parentin)
        os.close(parentout)
        os.dup2(childin, stdin_fd)
        os.dup2(childout, stdout_fd)
        args = (prop, ) + args
        os.execvp(prop, args)
        assert False, 'execvp failed!'


if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'pipes-testchild.py', 'spam')

    print('Hello 1 from parent', mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write('Parent got: "%s"\n' % reply)

    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write('Parent got: "%s"\n' % reply)
