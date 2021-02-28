from additional.run_arguments import run_arguments
from additional.run_scripts import run_scripts
from additional.run_console import run_console
import sys


class ANT:
    def __init__(self):
        self.home = __file__  # Папка расположения.

        self.mode_console = True  # Можно запускать интерактивную консоль?
        self.mode_arguments = True  # Можно читать аргументы как команду? как правило в ней запускают модуль arg ()
        self.mode_scripts = False  # Можно запускать скриптовые файлы типов .a .py?

    def set_console(self, console):
        self.mode_console = console

    def set_arguments(self, arguments):
        self.mode_arguments = arguments

    def set_scripts(self, scripts):
        self.mode_scripts = scripts

    def set_home(self, home):
        self.home = home


ant = ANT()
# TODO: Открывать файлы и
#     изменять mode_arguments,
#     mode_scripts, mode_console
#     bool(copy_file("scripts.txt"))
#     bool(copy_file("arguments.txt"))
#     bool(copy_file("console.txt"))

if ant.mode_arguments:
    run_arguments(sys.argv)

if ant.mode_scripts:
    run_scripts()

if ant.mode_console:
    run_console()
