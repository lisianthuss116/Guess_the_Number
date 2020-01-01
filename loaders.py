import sys
import time, random
from os import system
from termcolor import colored, cprint

def game_start_message(color = 'green') :
    system("cls")
    print("[====== Entering the Game ======]\n")
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[===============================]")

def loading_message(color = 'green', clear = False) :
    if clear :
        system("cls")
        print("[==============================]\n")
        cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
        print("[==============================]"), system("cls")

    system("cls")
    print("[==============================]\n")
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[==============================]")

def loading_message_tips(color = 'green', clear = False) :
    if clear :
        system("cls")
        print("[==============================]\n")
        cprint(" --Tips: Happy New year 2k20--\n", color, file=sys.stderr)
        cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
        print("[==============================]"), system("cls")

    system("cls")
    print("[==============================]\n")
    cprint(" --Tips: Happy New year 2k20--\n", color, file=sys.stderr)
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[==============================]")

def error_message(color = 'red') :
    cprint("\n\nThere went error, closing the game", color, file=sys.stderr)

def time_sleep(min_val, max_val, clear = False) :
    if clear :
        sleep = time.sleep(random.randint(min_val, max_val)), system("cls")
        return sleep

    sleep = time.sleep(random.randint(min_val, max_val))
    return sleep