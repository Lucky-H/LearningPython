#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: echo_client.py
@date: 2018-09-01
@time: 22:33:30
"""


import sys, socket
serverhost = 'localhost'
serverport = 50007
message = [b'Hello network world']


sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        serverhost = sys.argv[1]
        if len(sys.argv) > 2:
            message = [x.encode() for x in sys.argv[2:]]

    sockobj.connect((serverhost, serverport))
    for line in message:
        sockobj.send(line)
        data = sockobj.recv(1024)
        print('Client received:', data)
    sockobj.close()
