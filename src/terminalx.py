from colorama import Fore, Style, init  # For cross-platform colored output

import boot
import cmdDef

# Initialize colorama
init()

# Dictionary of available commands for easier maintenance, with functions mapped to commands
COMMANDS = {
    'py': {'desc': 'Enter a Python environment', 'color': Fore.BLUE, 'func': cmdDef.py},
    'fwrite': {'desc': 'Write user input to a configurable file', 'color': Fore.BLUE, 'func': cmdDef.fwrite},
    'ls': {'desc': 'List files in the working directory', 'color': Fore.BLUE, 'func': cmdDef.ls},
    'help': {'desc': 'Show the help text for Terminalx', 'color': Fore.GREEN, 'func': cmdDef.help},
    'exit': {'desc': 'Exit Terminalx', 'color': Fore.RED, 'func': cmdDef.exit},
    'clear': {'desc': 'Clear the terminal screen', 'color': Fore.CYAN, 'func': cmdDef.clear_screen},
}

def main():
    cmdDef.clear_screen()
    boot.boot()
    cmdDef.clear_screen(0.3)
    print(f"{Fore.CYAN}Welcome to Terminalx{Style.RESET_ALL}")
    print("This is a 'terminal emulator' in Python")
    
    while True:
        try:
            cmd = input(f"{Fore.GREEN}➜ {Style.RESET_ALL}").strip().lower()
            if cmd in COMMANDS and cmd != "help":
                COMMANDS[cmd]['func']()

            elif cmd == 'help':
                cmdDef.help(COMMANDS)
            else:
                cmdDef.unknown_cmd(cmd)
                
        except KeyboardInterrupt:
            cmdDef.clear_screen()
            cmdDef.prgmExit()
            break

if __name__ == "__main__":
    main()
