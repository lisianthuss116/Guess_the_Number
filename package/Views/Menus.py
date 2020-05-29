import Selection
import os
import sys
sys.path.append('../')


class MenuView:

    # Main menu view
    def mainMenu():
        print("\n[===== GUESS the NUMBERS =====]\n")
        print("■----------- Menus -----------■")
        print("|                             |")
        print("| 1 ) Singleplayer [computer] |")
        print("| 2 ) Multiplayer  [max:4]    |")
        print("| 3 ) How to play             |")
        print("| 4 ) Exit                    |")
        print("|                             |")
        print("|                             |\n")

    # Singleplayer menu view
    def singlePlayerview():
        print("\n[======= Single Player =======]\n")
        print("■-------- Difficulity --------■")
        print("|                             |")
        print("| 1 ) Easy                    |")
        print("| 2 ) Normal                  |")
        print("| 3 ) Hard                    |")
        print("| 4 ) Master                  |")
        print("|                             |")
        print("|                             |\n")

    # Multiplayer menu view
    def multiplayer_view():
        print("\n[======== Multiplayer ========]\n")
        print("■---------- Players ----------■")
        print("|                             |")
        print("| 1 ) 1 player                |")
        print("| 2 ) 2 player                |")
        print("| 3 ) 3 player                |")
        print("| 4 ) 4 player                |")
        print("|                             |\n")

        # player input [set how many player will play (max : 4)]
        players = input(">> ")
        players = str(players.lower().strip())

        # jokes? , yeah i think
        if players == "1":
            loader.time_sleep(2, 3, True)
            print(
                "[=== Really ?, No. u can't play alone in multiplayer, do you have any friends dude ? ===]\n")
            print("# Back [y/n]")
            back = input(">> ")
            if str(back.lower().strip()) == "y":
                loader.loading_message()
                Selection.Multiplayer(is_play=True)

    # Help menu view
    def help_view():
        print("\n[======= Help =======]\n")
        print("■-------- Help --------■")
        print("|                      |")
        print("| Just type the, tho   |")
        print("|                      |\n")
        print("Exit [y]")
