import os
import sys
import random

from termcolor import colored, cprint

from src.helper import loading

from src.configurations._game.services.estimate import estimate
from src.configurations._game.services import __
from src.configurations._game.services import vars


player_guess = vars.PLAYER_GUESS
player_wins = vars.PLAYER_WIN
com_guess = vars.COMPUTER_GUESS
computer_wins = vars.COMPUTER_WIN
draw = vars.ROUND_DRAW
rounds = vars.TOTAL_ROUND


def normal(player_name, round_played):
    global player_guess, player_wins, com_guess, computer_wins, draw, rounds

    print("[======== Single Player ========]")
    print("■===============================■")
    print("■----- Difficulity: Normal -----■")
    print("\n")
    print("■ Player-name: {}".format(player_name))
    print("■ Number between 11 - 99")
    print("\n")

    while rounds <= round_played:
        rnumber = random.randint(11, 99)

        cprint(
            f"■■■■------ Round : {rounds} ------■■■■", 'green', file=sys.stderr)

        # player turn to guess
        print(f"[{player_name}] Guess the number\n")
        player_guess = int(input(">> "))

        print("\n")
        # computer turn to guess
        print(f"[Computer] Guess the number\n")
        com_guess = estimate("normal", rnumber=rnumber)
        print(f">> {str(com_guess)}")

        print("\n")
        winner = __.result_of_round(
            rnumber, player_name, player_guess, com_guess)

        if winner == "player":
            player_wins += 1

        elif winner == "computer":
            computer_wins += 1

        print("\n\n")
        rounds += 1

    __.game_result(player_name, player_wins, computer_wins)
