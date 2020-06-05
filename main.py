import time
import random
import sys

from src.configurations._game.menu import GameMenu
from src.helper import loading


def main():
    try:
        import names
        from termcolor import colored, cprint

        loading.start_menu('green')  # loading game
        GameMenu.start_menu()  # start menu

    except Exception as ex:
        raise Exception(
            """
            Are you sure you have installed the depedencies ?,
            You can install it using : pip install -r requirements.txt
            """
        )


if __name__ == "__main__":
    main()
