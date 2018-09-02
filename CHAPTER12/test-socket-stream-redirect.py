#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: test-socket-stream-redirect.py
@date: 2018-09-02
@time: 21:53:05
"""


import sys, os, multiprocessing
from socket_stream_redirect import *


def server1():
    mypid = os.getpid()
    conn = init_listener_socket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        print('Server %s got [%s]' % (mypid, data))


def client1():
    mypid = os.getpid()
    redirect_out()
    for i in range(3):
        print('Client %s: %s' % (mypid, i))
        sys.stdout.flush()


def server2():
    mypid = os.getpid()
    conn = init_listener_socket()
    for i in range(3):
        conn.send(('Server %s: %s\n' % (mypid, i)).encode())


def client2():
    mypid = os.getpid()
    redirect_in()
    for i in range(3):
        data = input()
        print('Client %s got [%s]' % (mypid, data))


def server3():
    mypid = os.getpid()
    conn = init_listener_socket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        conn.send(('Server %s got [%s]' % (mypid, data)).encode())


def client3():
    mypid = os.getpid()
    redirect_both_client()
    for i in range(3):
        print('Client %s: %s' % (mypid, i))
        data = input()
        sys.stderr.write('Client %s got [%s]\n' % (mypid, data))


def server4():
    mypid = os.getpid()
    redirect_both_server()
    for i in range(3):
        print('Server %s: %s' % (mypid, i))
        data = input()
        sys.stderr.write('Server %s got [%s]\n' % (mypid, data))


def client4():
    mypid = os.getpid()
    redirect_both_client()
    for i in range(3):
        data = input()
        print('Client %s got [%s]' % (mypid, data))
        sys.stdout.flush()


if __name__ == '__main__':
    server = eval('server' + sys.argv[1])
    client = eval('client' + sys.argv[1])
    multiprocessing.Process(target=server).start()
    # import time
    # time.sleep(1)
    client()
