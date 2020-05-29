import sys
import time
import random
from os import system
from termcolor import colored, cprint


def time_wait(t1, t2):
    return time.sleep(random.randint(t1, t2))


def start_menu(color='green'):
    """Loading Start Game (Only when entering the game menu)."""

    system("cls")
    print("[====== Entering the Game ======]\n")
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[===============================]")
    time_wait(1, 3), system("cls")


def player_loading():
    """Loading player."""

    system("cls")
    print("[== Preparing ==]\n")
    cprint(" Please wait.. \n", 'green', file=sys.stderr)
    print("[===============]")
    time_wait(1, 3), system("cls")


def loading_message(color='green'):
    """Loading message (Check data)."""

    system("cls")
    print("[==============================]\n")
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[==============================]")
    time_wait(1, 3), system("cls")


def collecting_data(color='green'):
    """Loading collecting data."""

    system("cls")
    print("[==============================]\n")
    cprint(" Please wait, collecting data..\n", color, file=sys.stderr)
    print("[==============================]")
    time_wait(1, 3), system("cls")


def loading_message_tips(color='green'):
    """Loading message tips."""

    system("cls")
    print("[==============================]\n")
    cprint(" --Tips: Happy New year 2k20--\n", color, file=sys.stderr)
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[==============================]")
    time_wait(1, 3), system("cls")


def error_message(color='red'):
    """Error message."""
    print("\n\n")
    cprint("There went error, closing the game", color, file=sys.stderr)
