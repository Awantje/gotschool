from __future__ import unicode_literals
from __future__ import print_function
import sys
from io import StringIO
import os
from termcolor import colored
from colorama import init, deinit
from builtins import input


def show_list(lst):
    for item in lst:
        print(' - ' + item)


def ask(question):
    print(colored(question, 'blue'))


def warn(text):
    print(colored(text, 'yellow'))


def cls():
    if in_pycharm():
        for x in range(0, 30):
            print("")
        return

    os.system('cls' if os.name == 'nt' else 'clear')


def in_pycharm():
    return "PYCHARM_HOSTED" in os.environ


def choose(opties):

    cur_index = -1 if in_pycharm() else 0
    key = 0
    aantal_opties = len(opties)
    prev_out = sys.stdout.getvalue()

    while (cur_index < 0 or cur_index > aantal_opties - 1) if in_pycharm() else key != 13:

        sys.stdout = StringIO()
        cls()
        print(prev_out, end='')
        for idx in range(0, len(opties)):
            if cur_index == idx:
                print(colored(">> " + opties[idx], "red"))
            else:
                if in_pycharm():
                    print(str(idx) + ". ", end='')
                print((">> " if not in_pycharm() else "") + opties[idx])

        if in_pycharm():
            print("Maak een keuze: ")

        string_out = sys.stdout
        sys.stdout = sys.__stdout__
        init()
        print(string_out.getvalue())
        deinit()
        sys.stdout = string_out

        if in_pycharm():
            input_text = input()
            cur_index = int(input_text) if represents_int(input_text) else -1
        else:
            key = ord(getch())
            if key == 66 or key == 80:     #down
                cur_index = min(cur_index + 1, len(opties) - 1)
            elif key == 65 or key == 72:   #up
                cur_index = max(cur_index - 1, 0)
            elif chr(key) == 'q':
                sys.exit(0)

    if not in_pycharm():
        sys.stdout = StringIO()
        cls()
        print(prev_out, end='')
        print(">> " + colored(opties[cur_index], "green"))
        print("")       # lege regel

    result = opties[cur_index]
    return result


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            pass
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
