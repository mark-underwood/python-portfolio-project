""" fantasy gauntlet ppj """

import sys
from utils_pkg.game_engine import Game
from utils_pkg.player_name import player_name
from utils_pkg.press_enter import press_enter_to_continue

# 1 need a queue for enemies to fight
# 2 generate enemy actors and enqueue
# 3 enemies will be fought on a first come first serve basis
# 4 defeated enemies may be added to a linked list and dequeued

def main():
    """ main menu """
    game_title = 'FANTASY GAUNTLET PythonPPJ'
    print("You woke up in a dimly-lit cave near flowing water.\n")
    name = player_name()
    press_enter_to_continue()
    debug = False
    difficulty = 'normal'

    while True:
        # main menu loop
        print(f'\n |\n | {game_title}\n-|===============================>'+
        '\n | MAIN MENU\n |\n')
        print("1) Start EASY\n"+
              "2) Start NORMAL\n"+
              "3) Start HARD\n"+
              "4) Start NIGHTMARE\n"+
              "Q) Quit\n")
        choice = input("Select an option (# or Q): ")

        if choice in ('', '1'): # default
            difficulty = 'easy'
        elif choice == '2':
            difficulty = 'normal'
        elif choice == '3':
            difficulty = 'hard'
        elif choice == '4':
            difficulty = 'nightmare'
        elif choice.lower() == 'debug':
            if debug is False:
                debug = True
                print('Debug mode enabled.')
            else:
                debug = False
                print('Debug mode disabled.')
            continue
        elif choice.lower() == 'exit' or choice.lower() == 'quit' or choice.lower() == 'q':
            print("Exiting ...")
            sys.exit() # quit
        else:
            print(f"\n Choice '{choice if (len(choice) <= 32) else '???'}' is not available.\n")
            continue # invalid

        current_game = Game(difficulty, name) # setup
        current_game.start() # begin

if not sys.flags.interactive: # do not run immediately if shell is interactive
    main()
else:
    print("\n /!\\ Detected interactive shell.\n\nRun main() to start the game.\n")
