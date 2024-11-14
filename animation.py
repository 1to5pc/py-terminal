# Animation
#!/usr/bin/env python
import time
import sys
import itertools
import threading

def progress(percent=0, width=30, message="Loading", AnimTime=0.7):
    """Enhanced progress bar with message and percentage"""
    
    for i in range(101):  # Loop through 0-100 (percent values)
        filled = width * i // 100  # Calculate filled portion of the bar
        bar = '█' * filled + '░' * (width - filled)  # Create the progress bar
        print(f'\r{message}: |{bar}| {i:.0f}%', end='', flush=True)  # Update the bar in place
        time.sleep(AnimTime / 100)  # Sleep to simulate animation time

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
