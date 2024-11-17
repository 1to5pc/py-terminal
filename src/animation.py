""""
This module includes all functions that are used for animations.
"""
import time
import sys
import itertools

def progress(anim_time=0.7, message="Loading", width=30):
    """Enhanced progress bar with message and percentage"""

    for i in range(101):  # Loop through 0-100 (percent values)
        filled = width * i // 100  # Calculate filled portion of the bar
        prog_bar = '█' * filled + '░' * (width - filled)  # Create the progress bar
        print(f'\r{message}: |{prog_bar}| {i:.0f}%', end='', flush=True)  # Update the bar in place
        time.sleep(anim_time / 100)  # Sleep to simulate animation time

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
