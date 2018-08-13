#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: teststreams.py
@date: 2018-08-12
@time: 19:15:44
"""


def interact():
    print('Hello stream world')
    while True:
        try:
            reply = input('Enter a number>')
        except EOFError:
            break
        else:
            num = int(reply)
            print('%d squared is %d' % (num, num**2))
    print('Bye')


if __name__ == '__main__':
    interact()
