import os
import random
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def dprint(string, speed):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def get_words(words_length, nb_words):
    words = []

    with open('words.txt', 'r') as file:
        for word in file:
            if len(word.strip()) == words_length:
                words.append(word.strip().upper())

    random.shuffle(words)

    return words[:nb_words]

def set_color(color):
    colors = {'green': '\033[0;32m',
              'light green': '\033[1;32m',
              'red': '\033[1;31m',
              'yellow': '\033[1;33m'}

    print(colors[color], end='')
