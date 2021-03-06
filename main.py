#!/usr/bin/env python3
"""
    The module works only through import.
    Via os.system or return (RUN) - doesn't work.
"""

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am ANT and work as a module!!!")
    # Answer: I stay, I am a module.
else:
    print("I am ANT and work like a program!!!")
    # Answer: I stay, I am a program.

from additional.run_arguments import run_arguments
from additional.run_scripts import run_scripts
from additional.run_console import run_console
from additional.ANT import ANT
from additional.copy_file import copy_file
import sys

# import sqlite3
# bd = sqlite3.

ant = ANT()
ant.args = sys.argv
# TODO: перейти позже на SQL.
ant.mode_scripts = bool(copy_file("bd_v1/scripts.txt"))
ant.mode_console = bool(copy_file("bd_v1/console.txt"))
ant.mode_arguments = bool(copy_file("bd_v1/arguments.txt"))

if ant.mode_arguments:  # использовать аргументы при запуске ANT:
    print("start: arguments")
    run_arguments(ant.args)

if ant.mode_scripts:  # использовать скрипты при запуске ANT:
    print("start: scripts")
    run_scripts(ant.path)

if ant.mode_console:  # использовать общение пользователя с ANT:
    print("start: console")
    run_console()
