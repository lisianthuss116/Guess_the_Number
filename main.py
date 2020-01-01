import time, random, sys
import Menu as menu
import loaders as loader
from os import system
from termcolor import colored, cprint

def main() :
    # Loading to the Game
    loader.game_start_message('green')

    # Entering the Game
    loader.time_sleep(2, 3, True)
    menu.Menu()

if __name__ == "__main__" :
    main()
