#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: redirect.py
@date: 2018-08-13
@time: 21:15:20
"""


import sys

class Output:
    def __init__(self):
        self.text = ''

    def write(self, string):
        self.text += string

    def writelines(self, lines):
        for line in lines:
            self.write(line)


class Input:
    def __init__(self, input=''):
        self.text = input

    def read(self, size=None):
        if size is None:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[: size], self.text[size:]
        return res

    def readline(self):
        eoln = self.text.find('\n')
        if eoln == -1:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[: eoln+1], self.text[eoln+1:]
        return res


def redirect(function_, pargs, kargs, input_):
    temp = sys.stdin, sys.stdout
    sys.stdin = Input(input_)
    sys.stdout = Output()
    try:
        result = function_(*pargs, **kargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = temp
    return result, output


if __name__ == '__main__':
    from teststreams import interact
    result, output = redirect(interact, (), {}, '2\n3\n4\n')
    print('result => ', result)
    print('output => ', output)
