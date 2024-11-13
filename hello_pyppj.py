""" ppj """

# 1 need a queue for enemies to fight
# 2 generate enemy actors and enqueue
# 3 enemies will be fought on a first come first serve basis
# 4 defeated enemies may be added to a linked list and dequeued

class Actor(): # superclass
    """ generic actor template """
    def __init__(self, target, hp, hp_max, ap, ap_max, mp, mp_max, sp, sp_max):
        self.target = None
        self.hp = hp # health
        self.hp_max = hp_max
        self.ap = ap # action
        self.ap_max = ap_max
        self.mp = mp # mana
        self.mp_max = mp_max
        self.sp = sp # stamina
        self.sp_max = sp_max
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
    def __init__(self, target, hp, hp_max, ap, ap_max, mp, mp_max, sp, sp_max):
        super().__init__(target, hp, hp_max, ap, ap_max, mp, mp_max, sp, sp_max)
        print("actor stub")
        self.hp = hp_max # health
        self.ap = ap_max # action
        self.mp = mp_max # mana
        self.sp = sp_max # stamina


class NonPlayerCharacter(Actor): # subclass
    """ NPC subclass """
    def __init__(self, target, hp, hp_max, ap, ap_max, mp, mp_max, sp, sp_max):
        super().__init__(target, hp, hp_max, ap, ap_max, mp, mp_max, sp, sp_max)
        print("npc stub")

class Game():
    """ combat loop """
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def start(self):
        """ begin running the game """
        print(f"Do something? Difficulty is: {self.difficulty.upper()}") # stub

        # define player as Player(arg)

        # while True:
        #     ???
        # return (game_state_goes_here?)

        print("???\nProfit.") # joke stub

        print("\n GAME OVER\n") # generic game over message

def main():
    """ main """
    # main menu -> START, TUTORIAL
    game_title = 'FANTASY GAUNTLET PythonPPJ'
    print("Welcome.\n")
    while True: # menu loops
        print(f'\n {game_title} | MAIN MENU \n')
        print("1) Start game on NORMAL\n"+
              "2) Start game on HARD\n"+
              "3) Start game on NIGHTMARE\n"+
              "9) Quit\n")
        choice = input("Select an option: ")
        # print(f"You chose {choice}")
        if choice == '1':
            current_game = Game('normal') # setup normal game
            current_game.start() # begin
        elif choice == '2':
            current_game = Game('hard') # setup hard game
            current_game.start() # begin
        elif choice == '3':
            current_game = Game('nightmare') # setup nightmare game
            current_game.start() # begin
        elif choice == '9' or choice.lower == 'exit' or choice.lower == 'quit':
            print("Exiting ...")
            return
        else:
            print(f"\n Choice '{choice if (len(choice) <= 32) else '???'}' is invalid.\n")

main()
