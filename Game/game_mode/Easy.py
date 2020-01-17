import os, sys, random  
sys.path.append('../../')
import loaders as loader
from termcolor import colored, cprint
from Game import Single as SinglePlayer

def Easy(player_guess,player_win,com_guess,com_win,draw,rounds,player) :
    print("\n[======= Single Player =======]\n")
    print("■----- Difficulity: Easy -----■")
    print(f"■----- Player-name: {player}\n")

    while rounds != 6 :
        rand_num = random.randint(1, 10)
        loader.time_sleep(1, 2)
        cprint(f"■■■■------ Round : {str(rounds)} ------■■■■", 'green', file=sys.stderr)
        print("Guess the number between 1 - 10\n")

        # [Player and Computer guessing]
        # Player
        print(f"[{player}] Guess the number")
        player_guess = int(input(">> "))
        # Computer
        print(f"[Computer] Guess the number")
        com_guess = random.randint(1, 10)
        loader.time_sleep(1, 4)
        print(">> " + str(com_guess))
        
        # [ Draw rounds ]
        if player_guess == rand_num == com_guess :
            draw = draw + 1
            com_win = com_win + 1
            player_win = player_win + 1
            SinglePlayer.Single.draw_round(rand_num)

        # [ Player win rounds ]
        elif player_guess == rand_num :
            player_win = player_win + 1
            SinglePlayer.Single.player_round_win(player, rand_num)

        # [ Computer win rounds ]
        elif com_guess == rand_num :
            com_win = com_win + 1
            SinglePlayer.Single.com_round_win(rand_num)

        # [ Both wrong ]
        else :
            SinglePlayer.Single.wrong(rand_num)

        rounds = rounds + 1
        ## Rounds Ended ##
    
    ## Count the numbers of wins
    # [ Draw ]
    if player_win == com_wiN :
        return SinglePlayer.Single.draw(player, player_win, com_win)
    # [ Player win ]
    elif player_win > com_win :
        return SinglePlayer.Single.player_win(player, player_win, com_win)
    # [ Computer win ]
    else :
        return SinglePlayer.Single.computer_win(player, player_win, com_win)