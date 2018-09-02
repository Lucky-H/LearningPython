#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: multi6.py
@date: 2018-08-27
@time: 21:18:34
"""


import os, multiprocessing, time


def power(x):
    # print(os.getpid())
    return 2 ** x


if __name__ == '__main__':
    workers = multiprocessing.Pool(10)
    # result = workers.map(power, [2] * 100)
    # print(result[: 16])
    # print(result[-2: ])

    t1 = time.time_ns()
    result = workers.map(power, range(10000))
    # print(result[: 16])
    # print(result[-2: ])
    workers.close()
    workers.join()
    t2 = time.time_ns()

    t3 =time.time_ns()
    result = map(power, range(10000))
    t4 = time.time_ns()

    print('parallel:', (t2 - t1))
    print('single:', (t4 - t3))
    print(list(result)[-1])
