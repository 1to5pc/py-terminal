"""
This module stores all command that will be called from the main program
"""
import time
import os
import sys

from colorama import Fore, Style  # For cross-platform colored output

import animation
import file_func
import llm_api

def clear_screen(slptime=0):
    """
    Clears the terminal screen. Optionally, waits for a specified time before clearing.
    
    Args:
        slptime (float): Time to wait before clearing the screen. Default is 0.
    """
    if slptime:
        time.sleep(slptime)  # Wait before clearing
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen depending on the OS

def exit_prgm():
    """
    Exits the program after displaying a shutdown animation and message.
    """
    print(f"{Fore.YELLOW}Exiting Terminalx...{Style.RESET_ALL}")
    animation.progress(anim_time=0.4, message="Shutting down")  # Shows progress animation
    print(f"\n{Fore.GREEN}[OK]{Style.RESET_ALL} Quit 'Terminalx'")

def py():
    """
    Enters Python interactive shell and shows an animation.
    """
    print(f"{Fore.BLUE}Entering Python...{Style.RESET_ALL}")
    animation.progress_spinner(0.5)  # Show progress spinner animation for 0.5 seconds
    print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} Python3 Opened")  # Confirmation message

def prog_exit():
    """
    Exits the program by calling `exit_prgm()` and then terminating the process.
    """
    exit_prgm()  # Call the exit function to display exit animation
    sys.exit()  # Exit the program completely

def clear():
    """
    Clears the screen using `clear_screen()` function.
    """
    clear_screen()  # Just calls the function without delay

def prog_help(cmd_list):
    """
    Displays a list of available commands and their descriptions.
    
    Args:
        cmd_list (dict): Dictionary of available commands.
    """
    print(f"\n{Fore.CYAN}Available Commands:{Style.RESET_ALL}")
    for command, details in cmd_list.items(): # List each command
        print(f"{details['color']}{command:<10}{Style.RESET_ALL} - {details['desc']}")
    print()

def ls():
    """
    Lists the files in the current working directory.
    """
    err_code, dirlist = file_func.ls()  # Call `ls()` from `file_func` to get files
    if not err_code:
        list(map(print, dirlist))  # Print the files in the directory
    else: # Error if `ls` failed
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} The command failed to run")

def fwrite():
    """
    Writes text to a specified file based on user input and natural language processing.
    """
    usr_input = input("Enter the text you want to write and the file name in natural language:\n")
    err_code, file_name, input_text = llm_api.natlang_parser(usr_input) # Parse input using an LLM
    if err_code == -2: # Handle API KEY not found
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Gemini API Key not found. "
                "Check README for more info.")
    if not err_code:
        err_code, err_txt = file_func.fwrite(file_name, input_text)  # Write the parsed text to file
        if err_code == -1:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}" + err_txt)  # Handle file writing errors

def unknown_cmd(cmd):
    """Handles unknown commands and print the command that was entered."""
    print(f"{Fore.RED}'{cmd}' Unknown command!{Style.RESET_ALL} Run 'help' for available commands")
