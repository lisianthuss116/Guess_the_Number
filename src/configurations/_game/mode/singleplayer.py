import os
import sys
import random

from termcolor import colored, cprint

from src.configurations._game.difficulity.easy import easy
from src.configurations._game.services import __
from src.helper import loading


def play_mode(mode, player_name, round_played):
    getattr(SinglePlayer, mode)(player_name, round_played)

class SinglePlayer:

    # easy mode
    def easy(player_name, round_played):
        loading.time_wait(1, 4)
        loading.loading_message_tips()
        easy(player_name, round_played)

    # normal mode
    def normal(player_name, round_played):
        # NormalMode.normal()
        pass

    # hard mode
    def hard(player_name, round_played):
        # HardMode.Hard()
        pass

    # master mode
    def master(player):
        pass
        # print("\n[======= Single Player =======]\n")
        # print("■---- Difficulity: Master ----■")
        # print(f"■----- Player-name: {player}\n")

        # while rounds != 6:
        #     rand_num = Single.random_num(1, 1000)
        #     loader.time_sleep(1, 2)
        #     cprint(
        #         f"■■■■------ Round : {str(rounds)} ------■■■■", 'green', file=sys.stderr)
        #     print("Guess the number between 1 - 1000\n")

        #     # [ Player and Computer guessing ]
        #     # Player
        #     print(f"[{player}] Guess the number")
        #     player_guess = int(input(">> "))
        #     # Computer
        #     print(f"[Computer] Guess the number")
        #     com_guess = int(Single.random_num(rand_num-2, rand_num))

        #     loader.time_sleep(1, 3)
        #     print(">> " + str(com_guess))

        #     # [ Draw rounds ]
        #     if player_guess == rand_num == com_guess:
        #         draw = draw + 1
        #         com_win = com_win + 1
        #         player_win = player_win + 1
        #         Single.draw_round(rand_num)

        #     # [ Player win rounds ]
        #     elif player_guess == rand_num:
        #         player_win = player_win + 1
        #         Single.player_round_win(player, rand_num)

        #     # [ Computer win rounds ]
        #     elif com_guess == rand_num:
        #         com_win = com_win + 1
        #         Single.com_round_win(rand_num)

        #     # [ Both wrong ]
        #     else:
        #         Single.wrong(rand_num)

        #     rounds = rounds + 1
        #     ## Rounds Ended ##

        # # Count the numbers of wins
        # # [ Draw ]
        # if player_win == com_win:
        #     Single.draw(player, player_win, com_win)
        # # [ Player win ]
        # elif player_win > com_win:
        #     Single.player_win(player, player_win, com_win)
        # # [ Computer win ]
        # else:
        #     Single.computer_win(player, player_win, com_win)