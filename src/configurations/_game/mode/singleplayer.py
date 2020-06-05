import os
import sys
import random

from termcolor import colored, cprint

from src.configurations._game.difficulity.easy import easy
from src.configurations._game.difficulity.normal import normal
from src.configurations._game.difficulity.hard import hard
from src.configurations._game.difficulity.master import master
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
        loading.time_wait(1, 4)
        loading.loading_message_tips()
        normal(player_name, round_played)

    # hard mode
    def hard(player_name, round_played):
        loading.time_wait(1, 4)
        loading.loading_message_tips()
        hard(player_name, round_played)

    # master mode
    def master(player):
        loading.time_wait(1, 4)
        loading.loading_message_tips()
        master(player_name, round_played)