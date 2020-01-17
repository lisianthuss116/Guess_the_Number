import names
import loaders as loader

class Player :
    @staticmethod
    def check_how_many_players(players, name) :
        loader.loading_message('green')

        if players == "1" :
            print("playing with 2 players")

        elif players == "2" :
            print("playing with 3 players")

        elif players == "3" :
            print("playing with 4 players")
    
    @staticmethod
    def set_player_name(game_mode = None, players = None) :
        if players is None and game_mode == "singleplayer":
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
        elif players is not None and game_mode == "multiplayer" :
            loader.player_loading()

            if players == "2" :
                pass
            elif players == "3" :
                pass

            elif players == "4" :
                pass