import os
import sys
import Menu as menus
import loaders as loader
from Game.Single import Single
from Player.Player import Player
import Views.Menus as Menu
# from Game.Multiplayer import Multiplayer


class Selection:

    # Selected single player
    def SinglePlayer(is_play):
        # check if player is play
        if is_play:

            # display single-player menu
            Menu.MenuView.singlePlayerview()

            # player choice difficulity
            difficulity = input(">> ")
            difficulity = int(difficulity.lower().strip())

            # player create name
            name = Player.set_player_name(
                game_mode="singleplayer",
                players=None)

            # check if player has create name
            if name:
                # direct to check-difficulity
                Selection.Difficulity(difficulity, name)

    # Selected multiplayer
    def Multiplayer(is_play):
        # check if player is play
        if is_play:

            # display multiplayer menu
            Menu.MenuView.multiplayer_view()

            # all player create name
            name = Selection.set_player_name(
                game_mode="multiplayer",
                players=players)

            # if player has create name direct to check players
            if name:
                Player.check_how_many_players(players, name)

    # Selected Help
    def Help(is_play):
        # check if player is not play
        if not is_play:

            # diplay help menu
            Menu.MenuView.help_view()
            exit = input(">> ")

            # exit
            if str(exit.lower().strip()) == "y":
                loader.time_sleep(2, 3, True)
                menus.Menu()

        # if player is play, direct to main menu
        loader.time_sleep(2, 3, True)
        menus.Menu()

    @staticmethod
    def Difficulity(difficulity, name):
        loader.loading_message('green')

        diff = int(difficulity)
        hardship = [None, 'Easy', 'Normal', 'Hard', 'Master']
        set_hardship = getattr(Single, f'{hardship[diff]}')

        set_hardship(name)
