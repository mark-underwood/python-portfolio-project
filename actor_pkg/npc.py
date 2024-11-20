""" non player character subclass """

import random
from actor_pkg.actor import Actor

class NonPlayerCharacter(Actor): # subclass
    """ NPC subclass """
    def __init__(self, name, stat, is_player_faction = False): # enemy by default
        super().__init__(name, stat)
        self.stat["is_player_faction"] = is_player_faction # override default
        self.new_id()

        if is_player_faction: # enemy unless otherwise stated
            print(f"An ally {self.name} has joined you!")
        else:
            print(f"ENEMY SIGHTED: {self.name}")

    def new_id(self):
        """ generate actor id """
        # run once, while loop ( check if unique -> run again ) # can break targeting

        self.actor_id = random.randint(1000, 65535)
