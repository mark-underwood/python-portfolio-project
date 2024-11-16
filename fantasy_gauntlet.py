""" fantasy gauntlet ppj """

from actor_pkg.player import Player
from actor_pkg.npc import NonPlayerCharacter
from utils_pkg.linked_list import Stack, Queue
from utils_pkg.press_enter import press_enter_to_continue

# 1 need a queue for enemies to fight
# 2 generate enemy actors and enqueue
# 3 enemies will be fought on a first come first serve basis
# 4 defeated enemies may be added to a linked list and dequeued

# class ActOne():
#     """ act one | searching """
#     def __init__(self):
#         pass

# class ActTwo():
#     """ act two | combat """
#     def __init__(self):
#         pass

#     def combat(self):
#         print('combat stub')
#         while True:

#             break
#         print(f"\n {self.actor['player'].name.capitalize()} was victorious!!\n")

# class ActThree():
#     """ act three | victory looting """
#     def __init__(self, actor):
#         pass

class Game():
    """ game """
    def __init__(self, difficulty, name = 'PLAYER', debug = False):
        self.difficulty = difficulty
        self.name = name
        self.debug = debug
        self.player = None
        self.round_count = 0 # always start at zero
        self.rounds_ref = ({
            'easy': 1,
            'normal': 3,
            'hard': 5,
            'nightmare': 9
            },) # tuple + dict # a dictionary made read only by tuple encapsulation
        self.round_limit = self.rounds_ref[0][self.difficulty]
        # generate queue with initial node count = self.rounds_ref[0][difficulty]

    def start(self):
        """ begin running the game """
        if self.debug:
            print(f"Game start. Difficulty is: {self.difficulty.upper()}") # stub

        self.player = Player(self.name, {
            'hp_max': 100, # health
            'ap_max': 100, # action
            'mp_max': 100, # mana
            'sp_max': 100 ## stamina
            })

        if self.debug:
            print(f"A '{self.difficulty}' game should play",
              f"for {self.rounds_ref[0][self.difficulty]} rounds.")

        while True: # do rounds
            self.round_count += 1 # increment round counter
            print(f'{self.player.name.capitalize()} enters cavern #{self.round_count}.')
            # weapon lottery goes here

            if self.player.stat['hp'] <= 0:
                print('')
                break
            print(f"\n {self.player.name.capitalize()} was victorious!!\n")
            press_enter_to_continue()
            # item lottery goes here
            if self.round_count >= self.rounds_ref[0][self.difficulty]: # stop at round limit
                print("\n |\n | You found a way to safety.")
                while True:
                    choice = input(" |\n | Continue fighting?\n | \n\nType 'fight' or 'leave': ")
                    if choice.lower() == 'fight' or choice.lower() == 'more':
                        self.round_limit += 1
                        break
                    if choice.lower() == 'leave' or choice.lower() == 'q':
                        if self.debug:
                            print('StubD) Chance at final boss fight here !?')
                        break
                    print("Please type either 'fight' or 'leave'.")
            if self.round_count >= self.round_limit:
                break

        # post rounds conclusion
        if self.player.stat['hp'] <= 0:
            # bad endings here
            print("\n GAME OVER\n") # generic game over message
        else:
            # good endings here
            print(f"{self.player.name} met ol' Trusty the horse and rode off into the sunset.")

    def __str__(self):
        return f"Game: {self.difficulty}"

def player_name(name):
    """ set player name """
    max_length = 16
    while True:
        print('What is your name?\n')
        new_name = input(f'[Current:{name}]' )
        if len(new_name) <= max_length:
            if new_name.isalpha():
                return new_name
            print('Enter only letters.')
        else:
            print(f"Name must be {max_length} characters or less.")

def main():
    """ main menu """
    game_title = 'FANTASY GAUNTLET PythonPPJ'
    print("You woke up in a dimly-lit cave near flowing water.\n")
    name = player_name('PLAYER')
    while True:
        # main menu loop
        print(f'\n |\n | {game_title}\n-|===============================>'+
        '\n | MAIN MENU\n |\n')
        print("1) Start NORMAL\n"+
              "2) Start HARD\n"+
              "3) Start NIGHTMARE\n"+
              "Q) Quit\n")
        choice = input("Select an option (# or Q): ")

        if choice == '1':
            difficulty = 'normal'
        elif choice == '2':
            difficulty = 'hard'
        elif choice == '3':
            difficulty = 'nightmare'
        elif choice.lower() == 'exit' or choice.lower() == 'quit' or choice.lower() == 'q':
            print("Exiting ...")
            return
        else:
            print(f"\n Choice '{choice if (len(choice) <= 32) else '???'}' is not available.\n")
            continue
        current_game = Game(difficulty, name) # setup
        current_game.start() # begin

main() # first run
