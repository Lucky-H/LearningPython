#! /usr/bin/env python3

"""
@author： "Lucky-H"
@file: scanfile.py
@date: 2018-08-18
@time: 22:56:48
"""


from sys import argv
COMMANDS = {'*': 'Ms.', '+': 'Mr.'}


def scanner(name, function):
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        function(line)
    file.close()


def processline(line):
    try:
        print(COMMANDS[line[0]], line[1: -1])
    except KeyError:
        raise UnknowCommand(line)


if __name__ == '__main__':
    #scanner('testfile', processline)
    if len(argv) == 2:
        scanner(argv[1], processline)
    else:
        print('No file has been appointed')

