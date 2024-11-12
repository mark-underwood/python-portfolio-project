""" ppj """

# 1 need a queue for enemies to fight
# 2 generate enemy actors and enqueue
# 3 enemies will be fought on a first come first serve basis
# 4 defeated enemies may be added to a linked list and dequeued

class Actor(): # superclass
    """ generic actor template """
    def __init__(self, target, hp, hp_max, ap, ap_max, mp, mp_max):
        self.target = None
        self.hp = hp ; self.hp_max = hp_max
        self.ap = ap ; self.ap_max = ap_max
        self.mp = mp ; self.mp_max = mp_max
        damage_dealt = 0

    def set_target(self, target):
        """ set focus target """
        # need target and datatype validation
        self.target = target # WIP

    def weapon_attack(self, target):
        """ attack target """
        print("weapon_attack stub")

    def use_item(self, target):
        """ use an item """
        print("use_item stub")

class Player(Actor): # subclass
    """ player character subclass """
    def __init__(self, target, hp, hp_max, ap, ap_max, mp, mp_max):
        super().__init__(target, hp, hp_max, ap, ap_max, mp, mp_max)
        print("actor stub")


class NonPlayerCharacter(Actor): # subclass
    """ NPC subclass """
    def __init__(self, target, hp, hp_max, ap, ap_max, mp, mp_max):
        super().__init__(target, hp, hp_max, ap, ap_max, mp, mp_max)
        print("npc stub")

def game():
    """ combat loop """
    # while True:
    #     ???
    # return (game_state_goes_here?)

def main():
    """ main """
    # main menu -> START, TUTORIAL
    print('do something')

main()
