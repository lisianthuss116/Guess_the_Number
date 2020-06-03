import names

from src.helper import loading


class PlayerName:
    def set_player_name(mode, player=None):
        def player_names(player=None):
            loading.player_loading()
            print("\n\n")

            if player:
                print("[========== Player {player} ===========]")
            else:
                print("[========== Player ===========]")

            print("■=============================■")
            print("■-------- Player name --------■")
            print("|                             |")
            print("| 1 ) Type name               |")
            print("| 2 ) Random                  |")
            print("|                             |")

            print("\n\n")
            choice = str(input(">> "))
            print("\n")

            if choice == "1":
                print("Type your name ")
                name = str(input(">> "))
                if len(name) >= 20:
                    print("username can't exceed more than 20 character")
                    loading.time(1, 2), player_names()

            else:
                name = names.get_first_name()
                name = str.upper(name[0]) + str(name[1:None])

            return name

        if mode == "singleplayer":
            return player_names()

        else:
            player_names = {
                "player 1": "",
                "player 2": "",
                "player 3": "",
                "player 4": ""
            }
            for i in range(1, player + 1):
                _ = f"player {i}"
                player_names[_] = player_names(player=i)

            return player_names

    def check_how_many_players(players, name):
        loading.loading_message('green')

        if players == "1":
            print("playing with 2 players")

        elif players == "2":
            print("playing with 3 players")

        elif players == "3":
            print("playing with 4 players")
