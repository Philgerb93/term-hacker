import random
import time
import util

def main():
    words = util.get_words(4)
    answer = random.choice(words)
    grid = set_grid(words)

    util.set_color('green')
    show_intro()
    show_grid(grid)

def show_intro():
    util.clear()
    util.dprint("Terminal hacking in progress", 0.05)
    util.dprint('...', 0.5)
    time.sleep(0.1)
    print(" Password required\n")
    time.sleep(0.5)

def set_grid(words):
    COLS = 30
    DATA = ['!', '@', '#', '$', '%', '?', '&', '*',
            '(', ')', ';', ',', '.', ':', "'", '^']
    grid = []

    for word in words:
        string = ""
        word_start = random.randint(0, COLS - len(word))

        for x in range(word_start):
            string += random.choice(DATA)
        string += word
        for x in range(COLS - word_start - len(word)):
            string += random.choice(DATA)

        grid.append(string)

    return grid

def show_grid(grid):
    print('=' * len(grid[0]))
    for line in grid:
        util.dprint(line + '\n', 0.005)
    print('=' * len(grid[0]))

if __name__ == '__main__':
    main()

