"""
./ant command *arguments - этот блок отвечает за исполнения аргументов при старте.
"""
arguments = True

if arguments:
    # import sys
    # ant_arguments(sys.argv)
    pass

"""
file: *.a - этот блок отвечает за исполнение скриптов при старте.
"""
script = False

if script:
    # script_path = []
    # ant_scripts(script_path)
    pass

"""
Этот блок предназначен для прямого взаимодействия с пользователем.
"""
console = True
while console:
    command = input()

    if command[0] == ".":
        console = False
