""" player character subclass """

import random
from actor_pkg.actor import Actor

class Player(Actor): # subclass
    """ player character subclass """
    def __init__(self, name, stat, debug = False):
        super().__init__(name, stat, debug)
        self.new_id()
        if self.name.lower() == "you":
            s = ''
        else:
            s = 's'
        print(f"{self.name.capitalize()} stand{s} up and see{s} more light in one direction. ")

    def new_id(self):
        """ generate actor id """
        # run once, while loop ( check if unique -> run again ) # can break targeting

        self.actor_id = random.randint(0, 999)
