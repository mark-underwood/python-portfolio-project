""" ppj """

from getpass import getpass # for hiding user input

# 1 need a queue for enemies to fight
# 2 generate enemy actors and enqueue
# 3 enemies will be fought on a first come first serve basis
# 4 defeated enemies may be added to a linked list and dequeued

def pause():
    """ silent pause before continuing """
    # pylint does not complain 'unused variable' if starts with underscore
    _dump_this = getpass(" [ press enter to continue ]")
    print('_____________________________')

class Actor(): # superclass
    """ generic actor template """
    def __init__(self, name, stat):
        # hp_max, ap_max, mp_max, sp_max):
        self.target = None
        self.name = name
        self.hp = stat['hp_max'] # health
        self.hp_max = stat['hp_max']
        self.ap = stat['ap_max'] # action
        self.ap_max = stat['ap_max']
        self.mp = stat['mp_max'] # mana
        self.mp_max = stat['mp_max']
        self.sp = stat['sp_max'] # stamina
        self.sp_max = stat['sp_max']
        self.damage_dealt = 0
        self.stats_str = (
            f"  HEALTH: {self.hp} / {self.hp_max}\n"
            f"  ACTION: {self.ap} / {self.ap_max}\n"
            f"    MANA: {self.mp} / {self.mp_max}\n"
            f" STAMINA: {self.sp} / {self.sp_max}\n"
        )

    def set_target(self, target):
        """ set focus target """
        # need target and datatype validation
        self.target = target # WIP
        print("Set target:", target)

    def weapon_attack(self, target):
        """ attack target """
        print("weapon_attack stub:", target)

    def use_item(self, target):
        """ use an item """
        print("use_item stub:", target)

    def show_stats(self):
        """ show actor stats """
        print(self.stats_str)

    def __str__(self):
        return self.stats_str

class Player(Actor): # subclass
    """ player character subclass """
    def __init__(self, name, stat):
        super().__init__(name, stat)
        print(f"{name.capitalize()} has entered the game.")

class NonPlayerCharacter(Actor): # subclass
    """ NPC subclass """
    def __init__(self, name, stat):
        super().__init__(name, stat)
        print(f"ENEMY SIGHTED: {name}")

class Combat():
    """ combat """
    def __init__(self):
        print('combat stub')

class Game():
    """ game """
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.player = None
        self.round_count = 0 # always start at zero
        self.rounds_ref = ({
            'easy': 1,
            'normal': 3,
            'hard': 5,
            'nightmare': 9
            },) # tuple + dict # a dictionary made read only by tuple encapsulation
        self.round_limit = self.rounds_ref[0][self.difficulty]
        # generate queue with initial node count = self.rounds_ref[0][difficulty]

    def start(self):
        """ begin running the game """
        print(f"Game start. Difficulty is: {self.difficulty.upper()}") # stub
        
        self.player = Player('PLAYER', {
            'hp_max': 100, # health
            'ap_max': 100, # action
            'mp_max': 100, # mana
            'sp_max': 100 ## stamina
            })

        print(f"A '{self.difficulty}' game should play",
              f"for {self.rounds_ref[0][self.difficulty]} rounds.")

        while True: # do rounds
            self.round_count += 1 # increment round counter
            print(f'STUB: Round {self.round_count} START')
            print('StubA) pre-round story/RP')
            print('StubB) combat')
            print('StubC) post combat story/RP')
            print(f"\n {self.player.name.capitalize()} was victorious!!\n")
            pause()
            if self.round_count >= self.rounds_ref[0][self.difficulty]:
                print("\n |\n | You found a way to safety.")
                while True:
                    choice = input(" |\n | Continue fighting?\n | \n\nType 'fight' or 'leave': ")
                    if choice.lower() == 'fight' or choice.lower() == 'more':
                        print('StubD) add another queue noded, increase rount_limit, and advance')
                        self.round_limit += 1
                        break
                    if choice.lower() == 'leave' or choice.lower() == 'exit' or choice.lower() == 'q':
                        print('StubD) Chance at final boss fight here !?')
                        break
                    print("Please type either 'fight' or 'leave'.")
            if self.round_count >= self.round_limit:
                break
        
        # post rounds conclusion
        if self.player.hp <= 0:
            # bad endings here
            print("\n GAME OVER\n") # generic game over message
        else:
            # good endings here
            print(f"{self.player.name} met ol' Trusty the horse and rode off into the sunset.")

def main():
    """ main """
    # main menu -> START, TUTORIAL
    game_title = 'FANTASY GAUNTLET PythonPPJ'
    print("Welcome.\n")
    while True: # menu loops
        print(f'\n |\n | {game_title}\n-|===============================>'+
        '\n | MAIN MENU\n |\n')
        print("1) Start NORMAL\n"+
              "2) Start HARD\n"+
              "3) Start NIGHTMARE\n"+
              "Q) Quit\n")
        choice = input("Select an option (# or Q): ")
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
        elif choice.lower() == 'exit' or choice.lower() == 'quit' or choice.lower() == 'q':
            print("Exiting ...")
            return
        else:
            print(f"\n Choice '{choice if (len(choice) <= 32) else '???'}' is not available.\n")

main()
