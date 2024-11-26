""" game engine """

from actor_pkg.player import Player
# from actor_pkg.npc import NonPlayerCharacter
from utils_pkg.linked_list import Stack
# from utils_pkg.linked_list import Queue
from utils_pkg.press_enter import press_enter_to_continue

class Game():
    """ game """
    def __init__(self, difficulty, name = 'PLAYER', debug = False):
        self.difficulty = difficulty
        self.player = Player(name, {
            'hp_max': 100, # health
            'ap_max': 100, # action
            'mp_max': 100, # mana
            'sp_max': 100 ## stamina
            })
        self.debug = debug
        self.round_count = 0 # always start at zero
        self.sections = Stack() # saved round states
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
            print(f"Game start. Difficulty is: {self.difficulty.upper()}")
            print(f"A '{self.difficulty}' game should play",
              f"for {self.rounds_ref[0][self.difficulty]} rounds.")

        # do rounds
        while True:
            self.round_count += 1 # increment round counter
            print(f'\nYou enter cavern #{self.round_count}.\n')

            print('STUB: $ Pre-combat looting. $') # weapon lottery goes here
            print('\nSTUB: $$$ You found some weapons! $$$ Choose one.\n')
            press_enter_to_continue()

            print('STUB: /!\\ Combat things!') # combat things!
            if self.player.stat['hp'] <= 0:
                print('You were mortally wounded ...')
                press_enter_to_continue()
                break

            print("\n You were victorious!!\n")
            press_enter_to_continue()

            # item lottery goes here

            if self.round_count >= self.rounds_ref[0][self.difficulty]: # stop at round limit
                print(f"\n |\n | {self.player.name} found a way to safety.")
                while True:
                    choice = input(" |\n | Continue fighting?\n | \n\nType 'fight' or 'leave': ")
                    if choice.lower() == 'fight' or choice.lower() == 'more':
                        self.round_limit += 1
                        break
                    if choice.lower() in ('leave', 'q', 'qq', 'qqq', 'flee', 'exit'):
                        if self.debug:
                            print('StubD) Chance at final boss fight here !?')
                        break
                    print("Please type either 'fight' or 'leave'.")
            if self.round_count >= self.round_limit:
                break

        # conclusion
        if self.player.stat['hp'] <= 0:
            # bad endings here
            print("\n GAME OVER\n") # generic game over message
        else:
            # good endings here
            if self.player.name.lower() == 'you':
                print("\nYou woke up ...\n\n ... and remembered who you are.\n")
            else:
                print(f"\n{self.player.name} met ol' Trusty the horse",
                      "and rode off into the sunset.\n")
        press_enter_to_continue()

    def __str__(self):
        return f"Game: {self.difficulty}"
