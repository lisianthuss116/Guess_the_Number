import names
import loaders as loader
from Game.Single import Single
# from Game.Multiplayer import Multiplayer

class Selection :
    
    # Selected single player
    def Single_player(is_play, play_type) :
        print("\n[======= Single Player =======]\n")
        print("■-------- Difficulity --------■")
        print("|                             |")
        print("| 1 ) Easy                    |")
        print("| 2 ) Normal                  |")
        print("| 3 ) Hard                    |")
        print("| 4 ) Master                  |")
        print("|                             |")
        print("|                             |\n")

        difficulity = input(">> ")
        difficulity = str(difficulity.lower().strip())

        name = Selection.player_name()
        if name != '' :
            Selection.Difficulity(difficulity, name)


    # Selected multiplayer
    def Multiplayer(is_play, play_type) :
        print("Multiplayer")

    @staticmethod
    def Difficulity(difficulity, name) :
        loader.loading_message('green')
        # Single [ Easy ]
        if difficulity == "1" :
            loader.time_sleep(2, 3, True)
            Single.Easy(name)

        # Single [ Normal ]
        elif difficulity == "2" :
            loader.time_sleep(2, 3, True)
            Single.Normal(name)

        # Single [ Hard ]
        elif difficulity == "3" :
            loader.time_sleep(2, 3, True)
            Single.Hard(name)

        # Single [ Master ]
        else : 
            loader.time_sleep(2, 3, True)
            Single.Master(name)

    @staticmethod
    def player_name() :
        loader.player_loading()

        print("\n[======= Single Player =======]\n")
        print("■-------- Player name --------■\n")
        print(" 1 ) Type name")
        print(" 2 ) Random\n")
        choice = input(" >> ")
        
        # Check 
        if choice.lower().strip() == "1" :
            name = input(" >> ")
            name = str.upper(name[0])+str(name[1:None])
        else :
            name = names.get_first_name()
            name = str.upper(name[0])+str(name[1:None])
        return name
