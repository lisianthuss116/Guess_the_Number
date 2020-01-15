import names
import Menu as menus
import loaders as loader
from Game.Single import Single
from Views.singleplayer_view import singlePlayerview
from Views.multiplayer_view import multiplayer_view
# from Game.Multiplayer import Multiplayer

class Selection :
    
    # Selected single player
    def Single_player(is_play, play_type) :
        singlePlayerview()
        difficulity = input(">> ")
        difficulity = str(difficulity.lower().strip())

        name = Selection.player_name(play_type = "singleplayer", players = None)
        if name :
            Selection.Difficulity(difficulity, name)

    # Selected multiplayer
    def Multiplayer(is_play, play_type) :
        multiplayer_view()
        players = input(">> ")
        players = str(players.lower().strip())
        
        if players == "1" :
            loader.time_sleep(2, 3, True)
            print("[=== Really ?, No. u can't play alone in multiplayer, do you have any friends dude ? ===]\n")
            print("# Back [y/n]")
            back = input(">> ")
            if str(back.lower().strip()) == "y" :
                loader.loading_message()
                Selection.Multiplayer(is_play = True, play_type = 2)

        name = Selection.player_name(
            play_type = "multiplayer", 
            players = players)
        if name :
            Selection.CheckPlayers(players, name)
    
    # Selected Help
    def Help(is_play) :
        if not is_play :
            help_view()
            exit = input(">> ")

            if str(exit.lower().strip()) == "y":
                loader.time_sleep(2, 3, True)
                menus.Menu()

        loader.time_sleep(2, 3, True)
        menus.Menu()

    @staticmethod
    def Difficulity(difficulity, name) :
        loader.loading_message('green')
            
        set_difficulity = int(difficulity)
        loader.time_sleep(2, 3, True)
        Single.Hardships(set_difficulity, name)
                    
    @staticmethod
    def CheckPlayers(players, name) :
        loader.loading_message('green')

        if players == "1" :
            print("playing with 2 players")

        elif players == "2" :
            print("playing with 3 players")

        elif players == "3" :
            print("playing with 4 players")


    @staticmethod
    def player_name(play_type = None, players = None) :
        if players is None and play_type == "singleplayer":
            loader.player_loading()
            print("\n[==========  Player ==========]\n")
            print("■-------- Player name --------■\n")
            print(" 1 ) Type name")
            print(" 2 ) Random\n")
            choice = input(" >> ")
            
            # Check 
            if choice.lower().strip() == "1" :
                loader.time_sleep(2, 3, True)
                print("\n[==========  Player ==========]\n")
                print("■-------- Player name --------■\n")
                print("Input your name")
                name = input(" >> ")
                name = str.upper(name[0])+str(name[1:None])
            else :
                name = names.get_first_name()
                name = str.upper(name[0])+str(name[1:None])

            return name
        elif players is not None and play_type == "multiplayer" :
            loader.player_loading()

            if players == "2" :
                set_player_name = 1
                player_one_name = ""
                player_two_name = ""
                print(f"\n[============ {players} Player ============]\n")
                while set_player_name != 3 :
                    print(f"■-------- Player [{set_player_name}] names --------■\n")
                    print(" 1 ) Type name")
                    print(" 2 ) Random\n")
                    choice = input(" >> ")
                    
                    # Check 
                    if choice.lower().strip() == "1" :
                        print("\n[==========  Player ==========]\n")
                        print("■-------- Player name --------■\n")
                        print("Input your name")
                        name = input(" >> ")
                        name = str.upper(name[0])+str(name[1:None])
                    else :
                        name = names.get_first_name()
                        name = str.upper(name[0])+str(name[1:None])

                    if set_player_name == 1 :
                        set_player_name += 1
                        player_one_name = name
                        return player_one_name
                    else :
                        set_player_name += 1
                        player_two_name = name
                        return player_two_name

                print(f"Player one : {player_one_name}\n")
                print(f"Player two : {player_two_name}")

            elif players == "3" :
                pass

            elif players == "4" :
                pass