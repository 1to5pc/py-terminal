#boot Sequence
import time
def boot():
 print("Initiating bootloader")
 time.sleep(0.3)
 cbt = input("Boot into pyOS 20.69? [Y/n]: ")
 cbt=cbt.upper()
 cbt = cbt.upper()
 if cbt == "Y" or "YES":
    print("Initiating boot sequence")
 else:
    print("Aborting boot")
    exit()
