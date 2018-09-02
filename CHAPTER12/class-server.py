#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: class-server.py
@date: 2018-09-02
@time: 15:39:19
"""


import socketserver, time
myhost = ''
myport = 50007
myaddr = (myhost, myport)


def now():
    return time.asctime()


class MyClientHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address, now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            reply = 'Echo => %s at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()


def server():
    server = socketserver.ThreadingTCPServer(myaddr, MyClientHandle)
    server.serve_forever()


if __name__ == '__main__':
    server()
