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

def get_words(words_length):
    NB_WORDS = 15
    words = []

    with open('words.txt', 'r') as file:
        for word in file:
            if len(word.strip()) == words_length:
                words.append(word.strip().upper())

    random.shuffle(words)

    return words[:NB_WORDS]
