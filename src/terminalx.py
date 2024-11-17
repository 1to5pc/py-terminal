"""
This module is the main program used to call all other subprograms
"""
from colorama import Fore, Style, init  # For cross-platform colored output

import boot
import def_cmd

# Initialize colorama
init()

# Dictionary of available commands for easier maintenance, with functions mapped to commands
COMMANDS = {
    'py': {
        'desc': 'Enter a Python environment',
        'color': Fore.BLUE,
        'func': def_cmd.py
    },
    'fwrite': {
        'desc': 'Write user input to a configurable file',
        'color': Fore.BLUE,
        'func': def_cmd.fwrite
    },
    'ls': {
        'desc': 'List files in the working directory',
        'color': Fore.BLUE,
        'func': def_cmd.ls
    },
    'help': {
        'desc': 'Show the help text for Terminalx',
        'color': Fore.GREEN,
        'func': def_cmd.prog_help
    },
    'exit': {
        'desc': 'Exit Terminalx',
        'color': Fore.RED,
        'func': def_cmd.prog_exit
    },
    'clear': {
        'desc': 'Clear the terminal screen',
        'color': Fore.CYAN,
        'func': def_cmd.clear_screen
    }
}


def main():
    """ The main function called to initialize the program"""
    def_cmd.clear_screen()
    boot.boot()
    def_cmd.clear_screen(0.3)
    print(f"{Fore.CYAN}Welcome to Terminalx{Style.RESET_ALL}")
    print("This is a 'terminal emulator' in Python")

    while True:
        try:
            cmd = input(f"{Fore.GREEN}➜ {Style.RESET_ALL}").strip().lower()
            if cmd in COMMANDS and cmd != "help":
                COMMANDS[cmd]['func']()

            elif cmd == 'help':
                def_cmd.prog_help(COMMANDS)
            else:
                def_cmd.unknown_cmd(cmd)

        except KeyboardInterrupt:
            def_cmd.clear_screen()
            def_cmd.exit_prgm()
            break

if __name__ == "__main__":
    main()
