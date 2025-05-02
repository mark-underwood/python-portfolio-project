"""Post-menu core game loop."""

from actor_pkg.defaults import human_stats
from actor_pkg.player import Player
from core_pkg.cavern import Cavern
from core_pkg.wrap_up import wrap_up
# from utils_pkg.linked_list import Stack # inventory
# from utils_pkg.linked_list import Queue
from utils_pkg.press_enter import press_enter_to_continue

class Game():
    """Game class."""

    def __init__(self, difficulty, name = 'PLAYER', debug = False):
        self.difficulty = difficulty
        self.player = Player(
            name = name,
            stat = human_stats(),
            debug = debug)
        self.player.location = 0 # player start
        self.debug = debug
        self.round_count = 0 # always start at zero
        self.caverns = [] # persistent locations
        self.rounds_ref = ({
            'easy': 1,
            'normal': 3,
            'hard': 5,
            'nightmare': 9
            },) # tuple + dict # a dictionary made read only by tuple encapsulation
        self.round_limit = self.rounds_ref[0][self.difficulty]
        # generate queue with initial node count = self.rounds_ref[0][difficulty]

    def add_cavern(self):
        """add a cavern location"""

        self.caverns.append(
            Cavern( # must be added progressively
                cavern_id = self.round_count, # pass round count as id (caverns index)
                difficulty = self.difficulty,
                debug = self.debug
                ))

    def nav_menu(self):
        """navigation decision menu"""

        limit = (1, 3) # (lowest, highest) valid choice

        while True:
            print("What will you do?",
                "\n1) Look around",
                "\n2) Go backwards",
                "\n3) Go forwards",)
            choice = input("Enter a number: ")
            if not (len(choice) == 1 and choice.isnumeric):
                print("Enter only one number.")
                continue # one numeric character
            if not limit[0] <= int(choice) <= limit[1]:
                print(f"Enter a number from {limit[0]} to {limit[1]}")
                continue # out of range
            if choice == '1':
                self.caverns[self.player.location].observe()
                continue # no location change
            if choice == '2':
                if self.player.back():
                    break # can go back
                continue # ask again if can't go back
            if choice == '3':
                self.player.next()
                break # can always go forward
            print("ERROR: infinite loop prevention.")
            break # insurance

    def start(self):
        """begin running the game"""

        if self.debug:
            print(f"DEBUG: Game start. Difficulty is: {self.difficulty.upper()}")
            print(f"DEBUG: '{self.difficulty.capitalize()}' game should play",
              f"for {self.rounds_ref[0][self.difficulty]} rounds.")

        # origin cave
        self.caverns.append(
            Cavern(
                cavern_id = self.round_count,
                name = "Entry Alcove",
                difficulty = self.difficulty,
                debug = self.debug
            ))

        # do rounds
        while True:
            # "Entrance to cavern" if origin, no enemies. Maybe an ally.
            # Decision menu for current cavern:
            #    1) Search
            #    2) Move to next

            if self.player.location is self.round_count:
                self.round_count += 1 # increment round counter
                self.player.next() # move to next cavern
                if self.debug:
                    print('DEBUG: Player location:', self.player.location)
                    print('DEBUG: Caverns length:', len(self.caverns))
                    for cavern in self.caverns:
                        print(f'{cavern.name} #{cavern.cavern_id}', end = ' ')
                    print()
                if self.player.location > len(self.caverns) - 1:
                    self.add_cavern()

            self.caverns[self.player.location].observe()
            press_enter_to_continue()

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
        wrap_up(self.player)
        press_enter_to_continue()

    def __str__(self):
        return f"Game: {self.difficulty}"
