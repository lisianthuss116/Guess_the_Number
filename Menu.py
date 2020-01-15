import time, random
import sys
import loaders as loader
from os import system
from Selection import Selection
from termcolor import colored, cprint

choice    = None
is_play   = False
system("cls")

def Menu() :
    print("\n[===== GUESS the NUMBERS =====]\n")
    print("■----------- Menus -----------■")
    print("|                             |")
    print("| 1 ) Singleplayer [computer] |")
    print("| 2 ) Multiplayer  [max:4]    |")
    print("| 3 ) How to play             |")
    print("| 4 ) Exit                    |")
    print("|                             |")
    print("|                             |\n")
    select = input(">> ")
    select = str(select.lower().strip())
    return Choice(select, is_play = True)


def Choice(select, is_play = False) :
    loader.loading_message('green')

    if select == "1" :
        loader.time_sleep(2, 3, True)
        Selection.Single_player(is_play, play_type = select)

    elif select == "2" :
        loader.time_sleep(2, 3, True)
        Selection.Multiplayer(is_play, play_type = select)

    elif select == "3" :
        loader.time_sleep(2, 3, True)
        Selection.Help(is_play = False)
        