import sys, os, time, random
import loaders as loader
from Views.Menus import MenuView
from Selection import Selection
from termcolor import colored, cprint

# Main menu
def Menu() :
    is_play   = False
    os.system("cls")

    # display main menu 
    MenuView.mainMenu()

    # player select menu
    select = input(">> ")
    select = str(select.lower().strip())

    # direct to selected player select menu
    return Choice(select, is_play = True)


def Choice(select, is_play = False) :
    loader.loading_message('green')

    # Player choice Single-player
    if select == "1" :
        loader.time_sleep(2, 3, True)
        Selection.SinglePlayer(is_play)

    # Player choice Multi-player
    elif select == "2" :
        loader.time_sleep(2, 3, True)
        Selection.Multiplayer(is_play)

    # Player choice How to play
    elif select == "3" :
        loader.time_sleep(2, 3, True)
        Selection.Help(is_play = False)
        