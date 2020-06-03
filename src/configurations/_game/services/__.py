import random
import sys

from src.helper import loading

from termcolor import colored, cprint


def generate_random_num(m1, m2):
    return random.randint(m1, m2)


def result_of_round(random_num, player_name, player_guessed, computer_guessed,
                    player_wins, computer_wins):
    loading.time_wait(1, 2)

    # computer guessed is correct
    if computer_guessed == random_num:
        result = computer_wins
        result += 1
        cprint(f"-- computer win --", 'white', file=sys.stderr)
        print("-- guessed number : ", random_num)
        loading.time_wait(2, 3)

    # player guessed is correct
    elif player_guessed == random_num:
        result = player_wins
        result += 1
        cprint(f"-- {player_name} win --", 'white', file=sys.stderr)
        print("-- guessed number : ", random_num)
        loading.time_wait(2, 3)

    # both of player guessed the correct number
    elif player_guessed == computer_guessed == random_num:
        result = None
        cprint("-- Draw --", 'white', file=sys.stderr)
        print("-- Number : ", random_num)
        loading.time_wait(2, 3)

    # both of player and computer, guessed wrong number
    else:
        result = None
        cprint("-- Wrong --", 'red', file=sys.stderr)
        print("-- Number  : ", random_num)
        loading.time_wait(2, 3)

    return result


def game_result(player_name, player_wins, computer_wins):
    loading.collecting_data()

    if player_wins < computer_wins:
        cprint(f"■-------- Computer Win ! --------■",
               'green', file=sys.stderr)
        print(f"■ [Computer] Rounds win : ", computer_wins)
        print(f"■ [{player_name}] Rounds win : ", player_wins)
        print(f"■")

    elif player_wins > computer_wins:
        cprint(f"■-------- {player_name} Win ! --------■",
               'green', file=sys.stderr)
        print(f"■ [{player_name}] Rounds win : ", player_wins)
        print(f"■ [Computer] Rounds win : ", computer_wins)
        print(f"■")

    else:
        cprint(f"■-------- Draw ! --------■",
               'green', file=sys.stderr)
        print(f"■ [Computer] Rounds win : ", computer_wins)
        print(f"■ [{player_name}] Rounds win : ", player_wins)
        print(f"■")
