# Animation
#!/usr/bin/env python
import time

def progress(percent=0, width=20):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

#Use the following code to use the animation
#for i in range(101):
#    progress(i)
#    time.sleep(0.01)

# Newline so command prompt isn't on the same line
print()
