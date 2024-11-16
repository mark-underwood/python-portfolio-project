""" player character subclass """

from actor_pkg.actor import Actor

class Player(Actor): # subclass
    """ player character subclass """
    def __init__(self, name, stat):
        super().__init__(name, stat)
        print("You stand up and see more light in one direction. ")
