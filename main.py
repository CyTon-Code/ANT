from additional.run_arguments import run_arguments
from additional.run_scripts import run_scripts
from additional.run_console import run_console
from additional.ANT import ANT
import sys
from additional.copy_file import copy_file

ant = ANT()

# TODO: перейти позже на SQL.
ant.mode_scripts = bool(copy_file("bd_v1/scripts.txt"))
ant.mode_console = bool(copy_file("bd_v1/console.txt"))
ant.mode_arguments = bool(copy_file("bd_v1/arguments.txt"))

if ant.mode_arguments:  # использовать аргументы при запуске ANT:
    print("start: arguments")
    run_arguments(sys.argv)

if ant.mode_scripts:  # использовать скрипты при запуске ANT:
    print("start: scripts")
    run_scripts(ant.ant_path)

if ant.mode_console:  # использовать общение пользователя с ANT:
    print("start: console")
    run_console()
