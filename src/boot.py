""""
This module displays the boot screen for the main program
"""
from colorama import Fore, Style, init
import animation

def boot():
    """ Outputs the boot sequence """
    init()
    print(f"{Fore.CYAN}╔══════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║        Terminalx Bootloader      ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚══════════════════════════════════╝{Style.RESET_ALL}")

    animation.progress_spinner(1, "Initializing system")

    while True:
        try:
            cbt = input(f"\n{Fore.YELLOW}Boot into pyOS 20.69? [Y/n]:{Style.RESET_ALL} ").lower()
        except KeyboardInterrupt:
            cbt='n'
        if cbt in ['y', 'yes', '']:
            print(f"\n{Fore.GREEN}[OK]{Style.RESET_ALL} Initiating boot sequence")
            animation.progress(message="Loading system components")
            print()  # New line after progress bar
            return
        elif cbt in ['n', 'no']:
            print(f"\n{Fore.RED}[ABORT]{Style.RESET_ALL} Boot sequence aborted")
            exit()
        else:
            print(f"{Fore.RED}Invalid input. Please enter Y or N{Style.RESET_ALL}")
