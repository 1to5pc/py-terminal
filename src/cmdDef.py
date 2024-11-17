"""
This module stores all command that will be called from the main program
"""
import time
import os
import sys

from colorama import Fore, Style, init  # For cross-platform colored output

import animation
import fileFunc
import llmAPI

def clear_screen(slptime=0):
    """
    Clears the terminal screen. Optionally, waits for a specified time before clearing.
    
    Args:
        slptime (float): Time to wait before clearing the screen. Default is 0.
    """
    if slptime != 0:
        time.sleep(slptime)  # Wait before clearing
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the screen depending on the OS

def prgmExit(): 
    """
    Exits the program after displaying a shutdown animation and message.
    """
    print(f"{Fore.YELLOW}Exiting Terminalx...{Style.RESET_ALL}")
    animation.progress(AnimTime=0.4, message="Shutting down")  # Shows progress animation
    print(f"\n{Fore.GREEN}[OK]{Style.RESET_ALL} Quit 'Terminalx'")

def py():
    """
    Enters Python interactive shell and shows an animation.
    """
    print(f"{Fore.BLUE}Entering Python...{Style.RESET_ALL}")
    animation.progress_spinner(0.5)  # Show progress spinner animation for 0.5 seconds
    print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} Python3 Opened")  # Confirmation message

def exit():
    """
    Exits the program by calling `prgmExit()` and then terminating the process.
    """
    prgmExit()  # Call the exit function to display exit animation
    sys.exit()  # Exit the program completely

def clear():
    """
    Clears the screen using `clear_screen()` function.
    """
    clear_screen()  # Just calls the function without delay

def help(COMMANDS):
    """
    Displays a list of available commands and their descriptions.
    
    Args:
        COMMANDS (dict): Dictionary of available commands.
    """
    print(f"\n{Fore.CYAN}Available Commands:{Style.RESET_ALL}")
    for command, details in COMMANDS.items(): # List each command
        print(f"{details['color']}{command:<10}{Style.RESET_ALL} - {details['desc']}") 
    print()

def ls():
    """
    Lists the files in the current working directory.
    """
    errCode, dirlist = fileFunc.ls()  # Call `ls()` from `fileFunc` to get files
    if errCode == 0:
        list(map(print, dirlist))  # Print the files in the directory
    else: # Error if `ls` failed
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} The command failed to run")

def fwrite():
    """
    Writes text to a specified file based on user input and natural language processing.
    """
    usrInput = input("Enter the text you want to write and the file name in natural language:\n")
    errCode, fileName, inputText = llmAPI.NatLangParser(usrInput)  # Parse the input using LLM API
    if errCode == -2: # Handle API KEY not found
        print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}Gemini API Key not found. Check README for more info.")

    if errCode == 0:
        errCode, errTxt = fileFunc.fwrite(fileName, inputText)  # Write the parsed text to file
        if errCode == -1:
            print(f"{Fore.RED}[ERROR] {Style.RESET_ALL}" + errTxt)  # Handle file writing errors

def unknown_cmd(cmd):
    """Handles unknown commands and print the command that was entered."""
    print(f"{Fore.RED}'{cmd}' Unknown command!{Style.RESET_ALL} Run 'help' for available commands")
