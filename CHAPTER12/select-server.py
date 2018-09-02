#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: select-server.py
@date: 2018-09-02
@time: 19:58:36
"""


import select, time, socket
myhost = ''
myport = 50007
mainsock, readsock, writesock = [], [], []

portsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portsock.bind((myhost, myport))
portsock.listen(5)
mainsock.append(portsock)
readsock.append(portsock)


print('Select-server loop starting')
while True:
    readables, writeables, exceptions = select.select(readsock, writesock, [])
    for read in readables:
        if read in mainsock:
            conn, addr = read.accept()
            print('Connect:', addr, id(conn))
            readsock.append(conn)
        else:
            data = read.recv(1024)
            # print('\tgot', data, 'on', id(read))
            if not data:
                read.close()
                readsock.remove(read)
            else:
                print('\tgot', data, 'on', id(read))
                reply = 'Echo => %s at %s' % (data, time.asctime())
                read.send(reply.encode())
