import time
import os
import animation
import boot
from colorama import Fore, Style, init  # For cross-platform colored output

# Initialize colorama
init()

# Dictionary of available commands for easier maintenance
COMMANDS = {
    'py': {'desc': 'Enter a Python environment', 'color': Fore.BLUE},
    'help': {'desc': 'Show the help text for Terminalx', 'color': Fore.GREEN},
    'exit': {'desc': 'Exit Terminalx', 'color': Fore.RED},
    'clear': {'desc': 'Clear the terminal screen', 'color': Fore.CYAN},
}

def clear_screen(slptime=0):
    if slptime!=0:
        time.sleep(slptime)
    os.system('cls' if os.name == 'nt' else 'clear')

def prgmExit():
    print(f"{Fore.YELLOW}Exiting Terminalx...{Style.RESET_ALL}")
    animation.progress(100, message="Shutting down")
    print(f"\n{Fore.GREEN}[OK]{Style.RESET_ALL} Quit 'Terminalx'")

def main():
    clear_screen()
    boot.boot()
    clear_screen(0.3)
    print(f"{Fore.CYAN}Welcome to Terminalx{Style.RESET_ALL}")
    print("This is a 'terminal emulator' in Python")
    
    while True:
        try:
            cmd = input(f"{Fore.GREEN}➜ {Style.RESET_ALL}").strip().lower()
            
            if cmd == "py":
                print(f"{Fore.BLUE}Entering Python...{Style.RESET_ALL}")
                animation.progress_spinner(0.5)  # New spinning animation
                print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} Python3 Opened")
                
            elif cmd == "exit":
                prgmExit()
                break

            elif cmd == "clear":
                clear_screen()
                
            elif cmd == "help" or cmd == "list":
                print(f"\n{Fore.CYAN}Available Commands:{Style.RESET_ALL}")
                for command, details in COMMANDS.items():
                    print(f"{details['color']}{command:<10}{Style.RESET_ALL} - {details['desc']}")
                print()
                
            else:
                print(f"{Fore.RED}Unknown command!{Style.RESET_ALL} Run 'help' for available commands")
                
        except KeyboardInterrupt:
            clear_screen()
            prgmExit()
            break

if __name__ == "__main__":
    main()
