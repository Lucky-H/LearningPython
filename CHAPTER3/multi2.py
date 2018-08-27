#! python

"""
@author: "Lucky-H"
@file: multi2
@date: 2018-08-27
@time: 12:54:37
"""


import os, multiprocessing


def sender(pipe):
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()


def talker(pipe):
    pipe.send(dict(name='Bob', spam=42))
    reply = pipe.recv()
    print('talker got:', reply)


if __name__ == '__main__':
    (parentpipe, childpipe) = multiprocessing.Pipe()
    multiprocessing.Process(target=sender, args=(childpipe, )).start()
    print('parent got:', parentpipe.recv())
    parentpipe.close()

    (parentpipe, childpipe) = multiprocessing.Pipe()
    child = multiprocessing.Process(target=talker, args=(childpipe, ))
    child.start()
    print('parent got:', parentpipe.recv())
    child.join()

    parentpipe.send({x * 2 for x in 'spam'})
    print('parent exit.')
