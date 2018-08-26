#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: socket_preview.py
@date: 2018-08-26
@time: 11:03:18
"""


from socket import socket, AF_INET, SOCK_STREAM
port = 50008
host = 'localhost'


def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'server got: [%s] from %s' % (data, addr)
        conn.send(reply.encode())


def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print('Client got: [%s]' % reply)


if __name__ == '__main__':
    import threading
    sthread = threading.Thread(target=server, args=())
    sthread.daemon = True
    sthread.start()
    for i in range(5):
        threading.Thread(target=client, args=(('client%s' % i), )).start()
