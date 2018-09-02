#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: thread-server.py
@date: 2018-09-02
@time: 15:17:42
"""


import socket, time, threading
myhost = ''
myport = 50007
sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind((myhost, myport))
sockobj.listen(5)


def now():
    return time.asctime()


def handle(conn):
    time.sleep(5)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        reply = 'Echo => ' + str(data) + ' at ' + now()
        conn.send(reply.encode())
    conn.close()


def dispatcher():
    while True:
        conn, addr = sockobj.accept()
        print('Server connected by %s at %s' % (addr, now()))
        p = threading.Thread(target=handle, args=(conn,))
        p.start()


if __name__ == '__main__':
    dispatcher()
