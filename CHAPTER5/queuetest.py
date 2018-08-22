#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: queuetest.py
@date: 2018-08-22
@time: 00:41:46
"""


import threading, queue, time
numconsumers = 1
numproduces = 4
nummessages = 4
safepoint = threading.Lock()
queue_data = queue.Queue()


def producer(tid):
    for msgnum in range(nummessages):
        queue_data.put('[producer id=%d, count=%d]' % (tid, msgnum))
        time.sleep(0.1)


def consumer(tid):
    while True:
        time.sleep(0.1)
        try:
            data = queue_data.get(False)
        except queue.Empty:
            pass
        else:
            with safepoint:
                print('consumer', tid, 'got =>', data)


if __name__ == '__main__':
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i,))
        thread.daemon = True
        thread.start()


    for i in range(numproduces):
        thread = threading.Thread(target=producer, args=(i,))
        thread.start()
        thread.join()
    print('Main thread exiting.')
