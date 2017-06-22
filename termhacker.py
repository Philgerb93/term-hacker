import random
import time
import util
import sys

ROWS = 15
COLS = 30

def main():
    playing = True
    while playing:
        words = util.get_words(4, ROWS)
        answer = random.choice(words)
        grid = set_grid(words)
        game_over = False
        attempts = 4

        util.set_color('green')
        show_intro(attempts, grid)

        while playing and not game_over and attempts > 0:
            reprint(attempts, grid)
            user_input = input('> ').upper()

            if len(user_input) == 0:
                confirm_exit(attempts, grid)
            elif user_input in words:
                game_over = validate_input(user_input, answer, words, grid)
                if not game_over:
                    attempts -= 1

        playing = end_game(attempts, answer, words, grid)

def set_grid(words):
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
    print('=' * COLS)
    for line in grid:
        util.dprint(line + '\n', 0.005)
    print('=' * COLS)

def reprint(attempts, grid):
    util.clear()
    print("Terminal hacking in progress... Password required\n")
    
    print("Attempts remaining :", end=' ')
    util.set_color('light green' if attempts > 0 else 'red')
    print(str(attempts))
    util.set_color('green')

    show_grid(grid)
    print('')

def show_grid(grid):
    is_word = False

    print('=' * COLS)
    for line in grid:
        if len(line) > COLS + 2:
            word_highlight = 'yellow'
        else:
            word_highlight = 'light green' if len(line) == COLS else 'red'

        for char in line:
            if not is_word and char.isalpha():
                util.set_color(word_highlight)
                is_word = True
            elif char == ' ':
                util.set_color(word_highlight)
                is_word = False
            elif is_word and not char.isalpha():
                util.set_color('green')
                is_word = False
            print(char, end='')
        print('')
        util.set_color('green')
    print('=' * COLS)

def confirm_exit(attempts, grid):
    while True:
        reprint(attempts, grid)
        print("Quit the game? (Y/N) ", end='')
        user_input = input('> ').lower()

        if user_input == 'y':
            sys.exit()

def validate_input(user_input, answer, words, grid):
    if user_input == answer:
        return True
    else:
        index = words.index(user_input)
        matches = calculate_matches(user_input, answer)
        grid[index] += ' ' + str(matches)

        return False

def calculate_matches(word, answer):
    matches = 0

    for x in range(len(word)):
        if word[x] == answer[x]:
            matches += 1

    return matches

def end_game(attempts, answer, words, grid):
    grid[words.index(answer)] += " <= PASSWORD"

    while True:
        reprint(attempts, grid)

        print('Hacking', end=' ')
        if attempts > 0:
            util.set_color('yellow')
            print('SUCCESSFUL')
        else:
            util.set_color('red')
            print('FAILED')
        util.set_color('green')

        print("\nPlay again? (Y/N) ", end='')
        user_input = input('> ').lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False

if __name__ == '__main__':
    main()

