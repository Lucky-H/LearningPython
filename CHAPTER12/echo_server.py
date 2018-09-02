#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: echo_server.py
@date: 2018-09-01
@time: 22:25:40
"""


import socket, time
myhost = ''
myport = 50007


sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind((myhost, myport))
sockobj.listen(5)


if __name__ == '__main__':
    while True:
        conn, addr = sockobj.accept()
        print('Server connected by', addr)
        while True:
            data = conn.recv(1024)
            time.sleep(3)
            if not data:
                break
            conn.send(b'Echo=>' + data)
        conn.close()
