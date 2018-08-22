#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: thread-class.py
@date: 2018-08-21
@time: 23:44:10
"""


import threading


class Mythreading(threading.Thread):
    def __init__(self, tid, count, mutex):
        self.tid = tid
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('[%s] => %s' % (self.tid, i))


if __name__ == '__main__':
    threads = []
    stdoutmutex = threading.Lock()
    for i in range(10):
        thread = Mythreading(i, 100, stdoutmutex)
        threads.append(thread)
    for thread in threads:
        thread.start()
        thread.join()
    print('Main thread exiting.')
