""" non player character subclass """

import random
from actor_pkg.actor import Actor
from utils_pkg.npc_name import check_name

class NonPlayerCharacter(Actor): # subclass
    """ NPC subclass """
    def __init__(self, name, stat, is_player_faction = False, debug = False): # enemy by default
        super().__init__(name, stat, debug)
        self.stat["is_player_faction"] = is_player_faction # override default
        self.new_id()
        self.name = check_name(name=name,debug=debug)

        if is_player_faction: # enemy unless otherwise stated
            print(f"An ally, {self.name.capitalize()}, has joined you!")
        else:
            print(f"ENEMY SIGHTED: {self.name.upper()}")

    def new_id(self):
        """ generate actor id """
        # run once, while loop ( check if unique -> run again ) # can break targeting

        self.actor_id = random.randint(1000, 65535)
