#! python

"""
@author: "Lucky-H"
@file: multi3
@date: 2018-08-27
@time: 13:46:29
"""


import os, multiprocessing
proc = 3
count = 0


def showdata(label, val, arr):
    print('%-12s: pid:%5s, global:%s, value:%s, array:%s' % (label, os.getpid(), count, val.value, list(arr)))

def updater(val, arr):
    global count
    count += 1
    val.value += 1
    for i in range(3):
        arr[i] += 1


if __name__ == '__main__':
    scalar = multiprocessing.Value('i', 0)
    vector = multiprocessing.Array('d', proc)

    showdata('parent start', scalar, vector)

    p = multiprocessing.Process(target=showdata, args=('child', scalar, vector))
    p.start()
    p.join()

    print('\nloop1 (updates in parent, serial children)...')
    for i in range(proc):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = multiprocessing.Process(target=showdata, args=('process %s' % i, scalar, vector))
        p.start()
        p.join()

    print('\nloop2 (updates in parent, parallel children)...')
    ps = []
    for i in range(proc):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = multiprocessing.Process(target=showdata, args=('process %s' % i, scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()

    print('\nloop3 (updates in serial children)...')
    for i in range(proc):
        p = multiprocessing.Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()
    showdata('parent temp', scalar, vector)

    print('\nloop4 (updates in parallel children)...')
    ps = []
    for i in range(proc):
        p = multiprocessing.Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
    showdata('parent end', scalar, vector)
