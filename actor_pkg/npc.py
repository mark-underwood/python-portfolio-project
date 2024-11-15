""" NPC subclass """

from actor_pkg.actor import Actor

class NonPlayerCharacter(Actor): # subclass
    """ NPC subclass """
    def __init__(self, name, stat):
        super().__init__(name, stat)
        print(f"ENEMY SIGHTED: {name}")
