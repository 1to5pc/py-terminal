# Animation
#!/usr/bin/env python
import time
import sys
import itertools
import threading

def progress(percent=0, width=30, message="Loading"):
    """Enhanced progress bar with message and percentage"""
    filled = width * percent // 100
    bar = '█' * filled + '░' * (width - filled)
    print(f'\r{message}: |{bar}| {percent:.0f}%', end='', flush=True)

def progress_spinner(duration, message="Processing"):
    """New spinning cursor animation"""
    spinner = itertools.cycle(['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏'])
    end_time = time.time() + duration
    
    while time.time() < end_time:
        sys.stdout.write(f'\r{message} {next(spinner)} ')
        sys.stdout.flush()
        time.sleep(0.1)
    
    sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
    sys.stdout.flush()

#Use the following code to use the animation
#for i in range(101):
#    progress(i)
#    time.sleep(0.01)
# Newline so command prompt isn't on the same line
print()
