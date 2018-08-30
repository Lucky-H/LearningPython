#! python

"""
@author: "Lucky-H"
@file: launchmodes
@date: 2018-08-28
@time: 19:13:45
"""


import os, sys
pyfile = (sys.platform[: 3] == 'win' and 'python.exe') or 'python'
pypath = sys.executable


def fix_windows_path(cmdline):
    splitlines = cmdline.lstrip().split(' ')
    fixed_path = os.path.normpath(splitlines[0])
    return ' '.join([fixed_path] + splitlines[1:])


class Launchmode:
    def __init__(self, label, command):
        self.what = label
        self.where = command

    def __call__(self):
        self.anounce(self.what)
        self.run(self.where)

    def anounce(self, text):
        print(text)

    def run(self, cmdline):
        assert False, 'run must be define'


class System(Launchmode):
    def run(self, cmdline):
        cmdline = fix_windows_path(cmdline)
        os.system(pypath + ' ' + cmdline)


class Popen(Launchmode):
    def run(self, cmdline):
        cmdline =fix_windows_path(cmdline)
        os.popen(pypath + ' ' + cmdline)


class Fork(Launchmode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = fix_windows_path(cmdline)
        if os.fork() == 0:
            os.execvp(pypath, [pyfile] + cmdline)


class Start(Launchmode):
    def run(self, cmdline):
        assert sys.platform[: 3] == 'win'
        cmdline = fix_windows_path(cmdline)
        os.startfile(cmdline)


class StartArgs(Launchmode):
    def run(self, cmdline):
        assert sys.platform[: 3] == 'win'
        os.system('start ' + cmdline)


class Spawn(Launchmode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))


class Top_level(Launchmode):
    # 待实现功能
    def run(self, cmdline):
        assert False, 'mode not yet implemented'


if sys.platform[: 3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork


class QuietPortableLauncher(PortableLauncher):
    def anounce(self, text):
        pass


def selftest():
    file = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher()
    input('system mode...')
    System(file, file)()
    if sys.platform[: 3] == 'win':
        input('DOS start mode...')
        StartArgs(file, file)()


if __name__ == '__main__':
    selftest()
