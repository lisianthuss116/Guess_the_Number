import os, sys, random
sys.path.append('../')
import loaders as loader
from termcolor import colored, cprint

# Initialize player info
player_guess = 0
player_win   = 0

# Initialize computer info
com_guess = 0
com_win   = 0

# Another one
draw   = 0
rounds = 1

class Single :


    ## Easy Mode
    def Easy(player) :
        global player_guess, player_win, com_guess, com_win, draw, rounds

        print("\n[======= Single Player =======]\n")
        print("■----- Difficulity: Easy -----■")
        print(f"■----- Player-name: {player}\n")

        while rounds != 6 :
            rand_num = Single.random_num(1, 10)
            loader.time_sleep(1, 2)
            cprint(f"■■■■------ Round : {str(rounds)} ------■■■■", 'green', file=sys.stderr)
            print("Guess the number between 1 - 10\n")

            # [Player and Computer guessing]
            # Player
            print(f"[{player}] Guess the number")
            player_guess = int(input(">> "))
            # Computer
            print(f"[Computer] Guess the number")
            com_guess = Single.random_num(1, 10)
            loader.time_sleep(1, 4)
            print(">> " + str(com_guess))
            
            # [ Draw rounds ]
            if player_guess == rand_num == com_guess :
                draw = draw + 1
                com_win = com_win + 1
                player_win = player_win + 1
                Single.draw_round(rand_num)

            # [ Player win rounds ]
            elif player_guess == rand_num :
                player_win = player_win + 1
                Single.player_round_win(player, rand_num)

            # [ Computer win rounds ]
            elif com_guess == rand_num :
                com_win = com_win + 1
                Single.com_round_win(rand_num)

            # [ Both wrong ]
            else :
                Single.wrong(rand_num)

            rounds = rounds + 1
            ## Rounds Ended ##
        
        ## Count the numbers of wins
        # [ Draw ]
        if player_win == com_win :
            Single.draw(player, player_win, com_win)
        # [ Player win ]
        elif player_guess > com_win :
            Single.player_win(player, player_win, com_win)
        # [ Computer win ]
        else :
            Single.computer_win(player, player_win, com_win)

        
    ## Normal Mode
    def Normal(player) :
        global player_guess, player_win, com_guess, com_win, draw, rounds

        print("\n[======= Single Player =======]\n")
        print("■---- Difficulity: Normal ----■")
        print(f"■----- Player-name: {player}\n")

        while rounds != 6 :
            rand_num = Single.random_num(1, 20)
            loader.time_sleep(1, 2)
            cprint(f"■■■■------ Round : {str(rounds)} ------■■■■", 'green', file=sys.stderr)
            print("Guess the number between 1 - 20\n")

            # [ Player and Computer guessing ]
            # Player
            print(f"[{player}] Guess the number")
            player_guess = int(input(">> "))
            # Computer
            print(f"[Computer] Guess the number")
            if rand_num in range(1, 10) :
                com_guess = int(Single.random_num(1, 10))
            else :
                com_guess = int(Single.random_num(11, rand_num))
            loader.time_sleep(1, 3)
            print(">> " + str(com_guess))

            # [ Draw rounds ]
            if player_guess == rand_num == com_guess :
                draw = draw + 1
                com_win = com_win + 1
                player_win = player_win + 1
                Single.draw_round(rand_num)

            # [ Player win rounds ]
            elif player_guess == rand_num :
                player_win = player_win + 1
                Single.player_round_win(player, rand_num)

            # [ Computer win rounds ]
            elif com_guess == rand_num :
                com_win = com_win + 1
                Single.com_round_win(rand_num)

            # [ Both wrong ]
            else :
                Single.wrong(rand_num)

            rounds = rounds + 1
            ## Rounds Ended ##

        ## Count the numbers of wins
        # [ Draw ]
        if player_win == com_win :
            Single.draw(player, player_win, com_win)
        # [ Player win ]
        elif player_win > com_win :
            Single.player_win(player, player_win, com_win)
        # [ Computer win ]
        else :
            Single.computer_win(player, player_win, com_win)

                
    ## Hard Mode
    def Hard(player) :
        global player_guess, player_win, com_guess, com_win, draw, rounds

        print("\n[======= Single Player =======]\n")
        print("■----- Difficulity: Hard -----■")
        print(f"■----- Player-name: {player}\n")

        while rounds != 6 :
            rand_num = Single.random_num(1, 20)
            loader.time_sleep(1, 2)
            cprint(f"■■■■------ Round : {str(rounds)} ------■■■■", 'green', file=sys.stderr)
            print("Guess the number between 1 - 50\n")

            # [ Player and Computer guessing ]
            # Player
            print(f"[{player}] Guess the number")
            player_guess = int(input(">> "))
            # Computer
            print(f"[Computer] Guess the number")
            if rand_num in range(1, 11) :
                com_guess = int(Single.random_num(1, rand_num))
            else :
                com_guess = int(Single.random_num(rand_num-5, rand_num))

            loader.time_sleep(1, 3)
            print(">> " + str(com_guess))

            # [ Draw rounds ]
            if player_guess == rand_num == com_guess :
                draw = draw + 1
                com_win = com_win + 1
                player_win = player_win + 1
                Single.draw_round(rand_num)

            # [ Player win rounds ]
            elif player_guess == rand_num :
                player_win = player_win + 1
                Single.player_round_win(player, rand_num)

            # [ Computer win rounds ]
            elif com_guess == rand_num :
                com_win = com_win + 1
                Single.com_round_win(rand_num)

            # [ Both wrong ]
            else :
                Single.wrong(rand_num)

            rounds = rounds + 1
            ## Rounds Ended ##

        ## Count the numbers of wins
        # [ Draw ]
        if player_win == com_win :
            Single.draw(player, player_win, com_win)
        # [ Player win ]
        elif player_win > com_win :
            Single.player_win(player, player_win, com_win)
        # [ Computer win ]
        else :
            Single.computer_win(player, player_win, com_win)


    ## Master Mode
    def Master(player) :
        global player_guess, player_win, com_guess, com_win, draw, rounds

        print("\n[======= Single Player =======]\n")
        print("■---- Difficulity: Master ----■")
        print(f"■----- Player-name: {player}\n")

        while rounds != 6 :
            rand_num = Single.random_num(1, 1000)
            loader.time_sleep(1, 2)
            cprint(f"■■■■------ Round : {str(rounds)} ------■■■■", 'green', file=sys.stderr)
            print("Guess the number between 1 - 1000\n")

            # [ Player and Computer guessing ]
            # Player
            print(f"[{player}] Guess the number")
            player_guess = int(input(">> "))
            # Computer
            print(f"[Computer] Guess the number")
            com_guess = int(Single.random_num(rand_num-2, rand_num))

            loader.time_sleep(1, 3)
            print(">> " + str(com_guess))

            # [ Draw rounds ]
            if player_guess == rand_num == com_guess :
                draw = draw + 1
                com_win = com_win + 1
                player_win = player_win + 1
                Single.draw_round(rand_num)

            # [ Player win rounds ]
            elif player_guess == rand_num :
                player_win = player_win + 1
                Single.player_round_win(player, rand_num)

            # [ Computer win rounds ]
            elif com_guess == rand_num :
                com_win = com_win + 1
                Single.com_round_win(rand_num)

            # [ Both wrong ]
            else :
                Single.wrong(rand_num)

            rounds = rounds + 1
            ## Rounds Ended ##

        ## Count the numbers of wins
        # [ Draw ]
        if player_win == com_win :
            Single.draw(player, player_win, com_win)
        # [ Player win ]
        elif player_win > com_win :
            Single.player_win(player, player_win, com_win)
        # [ Computer win ]
        else :
            Single.computer_win(player, player_win, com_win)


    @staticmethod
    # Generate random number
    def random_num(val_1, val_2) :
        get_random = random.randint(val_1, val_2)
        return get_random
        

    ## METHODS ROUNDS ##
    @staticmethod
    # Player round win 
    def player_round_win(player, number) :
        loader.time_sleep(1, 3)
        cprint(f"\n\t-- {player} win --", 'white', file=sys.stderr)
        print("\t-- Number : " + str(number)), loader.time_sleep(1, 2)
    @staticmethod
    # Computer round win
    def com_round_win(number) :
        loader.time_sleep(1, 3)
        cprint("\n\t-- Com win --", 'white', file=sys.stderr)
        print("\t-- Number : " + str(number)), loader.time_sleep(1, 2)
    @staticmethod
    # Draw round
    def draw_round(number) :
        loader.time_sleep(1, 3)
        cprint("\n\t-- Draw --", 'white', file=sys.stderr)
        print("\t-- Number : " + str(number)), loader.time_sleep(1, 2)
    @staticmethod
    # Wrong
    def wrong(number) :
        loader.time_sleep(1, 3)
        cprint("\n\t-- Wrong ! --", 'red', file=sys.stderr)
        print("\t-- Number : " + str(number)), loader.time_sleep(1, 2)
    

    ## METHOD WINNER
    @staticmethod
    # Player win
    def player_win(player, player_win, com_win) :
        loader.loading_message()
        cprint(f"■-------- {player} Win ! --------■\n", 'green', file=sys.stderr)
        print(f"■ [{player}] Rounds win : " + str(player_win))
        print(f"■ [Computer] Rounds win : " + str(com_win))
        print(f"■")
    @staticmethod
    # Computer win
    def computer_win(player, player_win, com_win) :
        loader.loading_message()
        cprint(f"■-------- Computer Win ! --------■\n", 'green', file=sys.stderr)
        print(f"■ [Computer] Rounds win : " + str(com_win))
        print(f"■ [{player}] Rounds win : " + str(player_win))
        print(f"■")
    @staticmethod
    # Draw
    def draw(player, player_win, com_win) :
        loader.loading_message()
        cprint(f"■-------- Draw ! --------■\n", 'green', file=sys.stderr)
        print(f"■ [Computer] Rounds win : " + str(com_win))
        print(f"■ [{player}] Rounds win : " + str(player_win))
        print(f"■")