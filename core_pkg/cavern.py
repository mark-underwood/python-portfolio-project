"""Location template for caverns."""

from utils_pkg.dialog import say
from utils_pkg.linked_list import Stack # location inventory -> lootables

class Cavern():
    """Cavern class."""

    def __init__(self, cavern_id = None, name = "Unknown", difficulty = 'normal', debug = False):
        self.cavern_id = cavern_id
        self.name = name
        self.difficulty = difficulty
        self.debug = debug
        self.inventory = Stack() # inventory class for randomness?
        if self.debug:
            print(f'DEBUG: Discovered cavern "{self.name}". ID#{self.cavern_id}')

    def show_inv(self):
        """show lootable items"""

        print(f"Cavern #{self.cavern_id} items:\n{self.inventory}")

    def loot(self, item):
        """loot an item from here"""

        print(f"STUB: remove {item} from cavern # {self.cavern_id} inv stack.",
              "\nExternally add to player inventory within Game().")
        # check it item exists
        # self.inventory.del(item)

    def drop(self, item):
        """drop an item here"""

        print(f"STUB: place {item} in cavern # {self.cavern_id} inv stack.",
              "\nExternally remove from player inventory within Game().")
        # relies on external checking for item in player inventory
        # self.inventory.append(item)

    def observe(self):
        """describe the current cavern"""

        if self.cavern_id is None:
            print("ERROR: cavern_id was not set!")
            return

        if self.cavern_id <= 0:
            denominator = 20
            string_1 = "A loud stream of water takes up the majority of this small alcove."
            string_2 = "It is impossible to swim upstream."
            string_3 = "The water seems to disappear deep into the ground."

            say(string_1, denominator, self.debug)
            say(string_2, denominator, self.debug)
            say(string_3, denominator, self.debug)

            return

        print(f"Cavern #{self.cavern_id} is fairly large.")

        if self.inventory:
            print("There could be useful things in here.")

        print("The brighter tunnel could lead to a surface exit.")
        return
