from src.helper import loading

from src.configurations._game import view
from src.configurations._game.mode import singleplayer
from src.configurations._game.mode import multiplayer

from src.configurations._player.player_name import PlayerName

is_play = False
mode = ""


class GameMenu:
    def start_menu():
        print("\n")
        print("[===== GUESS the NUMBERS =====]")
        print("■=============================■")
        print("■----------- Menus -----------■")
        print("|                             |")
        print("| 1 ) Singleplayer            |")
        print("| 2 ) Multiplayer             |")
        print("| 3 ) How to play             |")
        print("| 4 ) Exit                    |")
        print("|                             |")
        print("|                             |")

        print("\n\n")
        print("You can choice and type 1 - 4\n")

        choice = str(input(">> "))
        GameMenu.check_choice(choice)

    def check_choice(choice):
        global is_play, mode

        loading.loading_message('green')

        Choices = {
            "1": (GameMenu.single_player, "singleplayer"),
            "2": (GameMenu.multiplayer, "multiplayer"),
            "3": (GameMenu.help),
            "4": "Exit",
        }

        is_play = True
        mode = Choices.get(choice)[1]
        return Choices.get(choice)[0]()

    def single_player():
        if is_play:
            print("\n")
            print("[======= Single Player =======]")
            print("■=============================■")
            print("■-------- Difficulity --------■")
            print("|                             |")
            print("| 1 ) Easy                    |")
            print("| 2 ) Normal                  |")
            print("| 3 ) Hard                    |")
            print("| 4 ) Master                  |")
            print("|                             |")
            print("|                             |")

            print("\n\n")
            print("You can select the difficulity by choosing 1 - 4")
            diffc = str(input(">> "))

            print("\n")
            print("Number of rounds to be played")
            round_played = int(input(">> "))

            difficulity = {
                "1": "easy",
                "2": "normal",
                "3": "hard",
                "4": "master",
            }

            diffc = difficulity.get(diffc)
            name = PlayerName.set_player_name(mode)

            # start play
            singleplayer.play_mode(diffc, name, round_played)

    def multiplayer():
        if is_play:
            print("[======== Multiplayer ========]")
            print("■=============================■")
            print("■---------- Players ----------■")
            print("|                             |")
            print("| 1 ) 1 player                |")
            print("| 2 ) 2 player                |")
            print("| 3 ) 3 player                |")
            print("| 4 ) 4 player                |")
            print("|                             |")

            print("\n\n")
            print("Under development ~")
            print("You will returned to start menu in 5s")
            loading.time_wait(1, 5)
            GameMenu.start_menu()

    def help():
        pass
