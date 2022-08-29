import time
import os
import animation
import boot

Lp = 0

boot.boot()
print("Welcome to Terminalx" )
print("This is a 'terminal emulator' in python" )
while Lp <= 1:
 cmd = input("Enter your command: ")
 if cmd == "py" :
      print(" Entering python." )
      time.sleep(0.16)
      print(" P-Y-T-H-O-N" )
      time.sleep(0.3)
      print(" [OK] Python3 Opened" )
 elif cmd == "exit" :
      print(" exiting terminalx" )
      time.sleep(0.08)
      time.sleep(0.2)
      for i in range(101):
       animation.progress(i)
       time.sleep(0.004)
      print()
      print(" [OK] Quit 'Terminalx'")
      time.sleep(0.069)
      break
 elif cmd == "help" :
    print(" Welcome to Terminalx" )
    print(" This a 'terminal emulator' in python" )
    print(" To get a list of the availble commands run 'list'")
 elif cmd == "list" :
    print(" py - Enter a :python env" )
    print(" help - Show the help text for terminalx" )
    print(" exit - Exit terminalx" )
 else:
    print(" Unknown command! Run 'help' for help and 'list' for a list of commands" )