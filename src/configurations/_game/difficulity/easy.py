import os
import sys
import random

from termcolor import colored, cprint

from src.helper import loading

from src.configurations._game.services import estimated_rand as estimate
from src.configurations._game.services import __
from src.configurations._game.services import vars


player_guess = vars.PLAYER_GUESS
player_wins = vars.PLAYER_WIN
com_guess = vars.COMPUTER_GUESS
computer_wins = vars.COMPUTER_WIN
draw = vars.ROUND_DRAW
rounds = vars.TOTAL_ROUND


def easy(player_name, round_played):
    global player_guess, player_wins, com_guess, computer_wins, draw, rounds

    print("[======= Single Player =======]")
    print("■=============================■")
    print("■----- Difficulity: Easy -----■")
    print("\n")
    print("■ Player-name: {}".format(player_name))
    print("■ Guess the number between 1 - 10")
    print("\n")

    while rounds <= round_played:
        rnumber = random.randint(1, 10)

        cprint(
            f"■■■■------ Round : {rounds} ------■■■■", 'green', file=sys.stderr)

        # player turn to guess
        print(f"[{player_name}] Guess the number")
        player_guess = int(input(">> "))

        print("\n")
        # computer turn to guess
        print(f"[Computer] Guess the number")
        com_guess = estimate.estimate_and_set_random(1, 10)
        print(f">> {str(com_guess)}")

        print("\n")
        __.result_of_round(rnumber, player_name, player_guess,
                           com_guess, player_wins, computer_wins)

        print("\n\n")
        rounds += 1

    __.game_result(player_name, player_wins, computer_wins)
