import time, random
import Menu as menu
from sys import stderr
from os import system
from termcolor import colored, cprint

def main() :
    system("cls")
    # Loading to the Game
    print("\n== Entering the Game ==\n")
    cprint("Please wait, checking data ...", "green", file=stdeer)
    time.sleep(random.randint(1, 3)), system("cls")

    # Entering the Game
    menu.start()

if __name__ == "__main__" :
    main()