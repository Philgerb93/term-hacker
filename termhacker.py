import random
import time
import util

def main():
    words = util.get_words(4)
    answer = random.choice(words)

    show_intro()

def show_intro():
    util.clear()
    util.dprint("Terminal hacking in progress", 0.05)
    util.dprint('...', 0.5)
    time.sleep(0.1)
    print(" Password required\n")
    time.sleep(0.5)

if __name__ == '__main__':
    main()

