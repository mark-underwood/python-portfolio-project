""" player character subclass """

import random
from actor_pkg.actor import Actor

class Player(Actor): # subclass
    """ player character subclass """
    def __init__(self, name, stat, debug = False):
        super().__init__(name, stat, debug)
        self.location = 0 # start at the origin
        self.new_id()
        if self.name.lower() == "you":
            s = ''
        else:
            s = 's'
        self.s = s
        print(f"\n{self.name.capitalize()} stand{s} up and see{s} more light in one direction. ")

    def new_id(self):
        """ generate actor id """
        # run once, while loop ( check if unique -> run again ) # can break targeting

        self.actor_id = random.randint(0, 999)

    def next(self):
        """ move player to next cavern """

        print(f"{self.name} move{self.s} forward into the next cavern.")
        self.location += 1

    def back(self):
        """ move player to next cavern """

        if self.location <= 0: # 0 is origin, 1 is first cavern
            print("There is no further back to go.")
            self.location = 0 # in case of glitch, return to origin
            return False
        print(f"{self.name} backtrack{self.s} to the previous cavern.")
        self.location -= 1
        return True
