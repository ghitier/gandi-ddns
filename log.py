import os
import time

class log:

    color = {
        'black' : '\033[0;30m',
        'red' : '\033[0;31m',
        'green' : '\033[0;32m',
        'yellow' : '\033[0;33m',
        'blue' : '\033[0;34m',
        'maganta' : '\033[0;35m',
        'cyan' : '\033[0;36m',
        'white' : '\033[0;37m',
        'reset' : '\033[0m'
        }

    def __init__(self):
        self._time = time.localtime()
        self._prompt = log.color['cyan'] + time.strftime("[%d/%m/%Y][%H:%M:%S]: ", self._time) + log.color['reset']
        self._error = log.color['red'] + '[Error] ' + log.color['reset']
        self._warning = log.color['yellow'] + '[Warning] ' + log.color['reset']
        self._file = os.path.dirname(os.path.realpath(__file__)) + '/log.txt'
        self._buffer = 50

    def append(self, str):
        try:
            f = open(self._file, "a")
            f.write(self._prompt + str + '\n')
            f.close()
        except:
            return
        # self.truncate()

    def lines(self):
        try:
            f = open(self._file, "r")
            for i, l in enumerate(f):
                pass
            return i + 1
        except:
            return (-1)

    def truncate(self):
        nb = self.lines()
        if nb > self._buffer:
            # read all lines in log file
            try:
                f = open(self._file, "r")
                lines = f.readlines()
                f.close()
            except:
                return
            # rewrite the latest lines to fit buffer
            try:
                i = 0
                f = open(self._file, "w")
                for line in lines:
                    if i >= nb - self._buffer:
                        f.write(line)
                    i += 1
                f.close()
            except:
                return

    def error(self, error):
        self.append(self._error + error)

    def warning(self, warning):
        self.append(self._warning + warning)

    def __str__(self):
        str = self._prompt + '\n' + self._file + '\n' + self._buffer
        return str
