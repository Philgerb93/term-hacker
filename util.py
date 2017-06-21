import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def dprint(string, speed):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
