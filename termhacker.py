import random
import time
import util

def main():
    words = util.get_words(4)
    answer = random.choice(words)
    grid = set_grid(words)
    attempts = 4

    util.set_color('green')
    show_intro(attempts, grid)
    reprint(attempts, grid)

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

def show_intro(attempts, grid):
    util.clear()
    util.dprint("Terminal hacking in progress", 0.05)
    util.dprint('...', 0.5)
    time.sleep(0.1)
    print(" Password required\n")
    time.sleep(0.5)

    util.dprint("Attempts remaining : " + str(attempts) + '\n', 0.05)
    show_grid_intro(grid)

    util.dprint("Decrypting", 0.05)
    util.dprint('...\n', 0.5)

def show_grid_intro(grid):
    print('=' * len(grid[0]))
    for line in grid:
        util.dprint(line + '\n', 0.005)
    print('=' * len(grid[0]))

def reprint(attempts, grid):
    util.clear()
    print("Terminal hacking in progress... Password required\n")
    print("Attempts remaining : " + str(attempts))
    show_grid(grid)

def show_grid(grid):
    is_word = False

    print('=' * len(grid[0]))
    for line in grid:
        for char in line:
            if not is_word and char.isalpha():
                util.set_color('light green')
                is_word = True
            elif is_word and not char.isalpha():
                util.set_color('green')
                is_word = False
            print(char, end='')
        print('')
    print('=' * len(grid[0]))

if __name__ == '__main__':
    main()

