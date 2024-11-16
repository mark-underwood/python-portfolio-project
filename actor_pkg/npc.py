""" non player character subclass """

from actor_pkg.actor import Actor

class NonPlayerCharacter(Actor): # subclass
    """ NPC subclass """
    def __init__(self, name, stat, is_player_faction = False):
        super().__init__(name, stat)
        if is_player_faction: # enemy unless otherwise stated
            print(f"An ally {name} has joined you!")
        else:
            print(f"ENEMY SIGHTED: {name}")
