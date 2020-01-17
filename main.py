import time, random, sys
import Menu as menu
import loaders as loader
from os import system
from termcolor import colored, cprint

def main() :
    # Loading Game
    loader.game_start_message('green')

    # Enter the Game menus
    menu.Menu()

if __name__ == "__main__" :
    main()
