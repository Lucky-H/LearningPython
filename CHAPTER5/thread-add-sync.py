#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: thread-add-sync.py
@date: 2018-08-22
@time: 00:00:45
"""


import threading, time
count = 0
addlock = threading.Lock()


def adder(lock, tid):
    global count

    with lock:
        count += 1
    # time.sleep(0.5)
    with lock:
        count += 1
    print(tid)


if __name__ == '__main__':
    threads = []
    for i in range(100):
        thread = threading.Thread(target=adder, args=(addlock, i))
        threads.append(thread)
    for thread in threads:
        thread.start()
        thread.join()
    print(count)
