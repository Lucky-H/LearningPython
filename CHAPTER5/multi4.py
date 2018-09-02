#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: multi4.py
@date: 2018-08-27
@time: 20:30:36
"""


import os, time, multiprocessing, queue


class counter(multiprocessing.Process):
    label = ' @'

    def __init__(self, start, queue, lock):
        self.state = start
        self.post = queue
        self.lock = lock
        multiprocessing.Process.__init__(self)

    def run(self):
        for i in range(3):
            time.sleep(1)
            self.state += 1
            with self.lock:
                print(self.label, self.pid, self.state)
            self.post.put([self.pid, self.state])
        with self.lock:
            print(self.label, self.pid, '-')


if __name__ == '__main__':
    print('start', os.getpid())
    expected = 9
    lock = multiprocessing.Lock()
    post = multiprocessing.Queue()
    p = counter(0, post, lock)
    q = counter(100, post, lock)
    r = counter(1000, post, lock)
    ps = [p, q, r]
    for i in ps:
        i.start()

    while expected:
        time.sleep(0.5)
        try:
            data = post.get(block=False)
        except queue.Empty:
            with lock:
                print('no data...')
        else:
            with lock:
                print('posted:', data)
            expected -= 1

    for i in ps:
        i.join()

    print('finish', os.getpid(), r.exitcode)

