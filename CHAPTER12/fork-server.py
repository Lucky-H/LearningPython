#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: fork-server.py
@date: 2018-09-02
@time: 11:05:34
"""


import os, socket, time, signal
myhost = ''
myport = 50007
active_children = []


sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind((myhost, myport))
sockobj.listen(5)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


def now():
    return time.asctime()


def reap_children():
    while active_children:
        (pid, stat) = os.waitpid(0, os.WNOHANG)
        if not pid:
            break
        active_children.remove(pid)


def handle(conn):
    time.sleep(5)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        reply = 'Echo => %s at %s' % (data, now())
        conn.send(reply.encode())
    conn.close()
    os._exit(0)


def dispatcher():
    while True:
        conn, addr = sockobj.accept()
        print('Server connected by', addr, end=' ')
        print('at', now())
        # reap_children()
        c_pid = os.fork()
        if c_pid:
            active_children.append(c_pid)
        else:
            handle(conn)


if __name__ == '__main__':
    dispatcher()