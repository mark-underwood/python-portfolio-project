""" actor """

# from utils_pkg.linked_list import Queue # many-target queue

class Actor(): # superclass
    """ generic actor template """
    def __init__(self, name, stat):
        # stat = {"hp_max":100, "mp_max":100, "sp_max":100}):
        self.target = None
        self.actor_id = None # set in subclass
        self.name = name
        # add stats to validate here:
        self.valid_stats = ("hp", "hp_max", "ap", "ap_max",
                             "mp", "mp_max", "sp", "sp_max",
                             "is_player_faction", 'damage_dealt')
        self.stat = stat
        self.stat["is_player_faction"] = True # friendly by default
        self.stat['hp'] = stat['hp_max'] # health
        self.stat['ap'] = 0 # action ; start not ready
        self.stat['ap_max'] = 100 # action ; start not ready
        self.stat['mp'] = stat['mp_max'] # mana
        self.stat['sp'] = stat['sp_max'] # stamina
        self.stat['damage_dealt'] = 0
        self.info_str = (
            f"CURRENT TARGET OF '{self.name}' IS: {self.target}\n"
            f"  HEALTH: {self.stat['hp']} / {self.stat['hp_max']} HP\n"
            f"  ACTION: {self.stat['ap']} / {self.stat['ap_max']} AP\n"
            f"    MANA: {self.stat['mp']} / {self.stat['mp_max']} MP\n"
            f" STAMINA: {self.stat['sp']} / {self.stat['sp_max']} SP\n"
        )

    def set_target(self, target = None): # no target disengages
        """ set focus target """

        # need target and datatype validation
        old_target = self.target
        self.target = target
        if target is None:
            print(f"{self.name.capitalize()} stopped targeting {old_target}.")
        elif self.target is target:
            print(f"{self.name.capitalize()} changed target to {target}.")
        else:
            print("ERROR: failed to change target.")

    def print_target(self):
        """ print current target """

        print(f"{self.name.capitalize()} is targeting {self.target}.")

    def use_weapon(self): # attack queue based on action points budget?
        """ attack target with weapon """

        if self.target is None:
            print(f"{self.name.capitalize()} is not targeting anything.")
            return
        if self.target.stat["is_friendly"] and self.target.name is not self.name:
            print(f"{self.target.name.capitalize()} will remember this betrayal.")
            self.target.stat["is_friendly"] = False
        print("weapon_attack stub:", self.target)

    def use_item(self, target = None):
        """ use an item """

        print("use_item stub:", target)
        # if target == None:
        #     target == self.name (need actor id)
        # if target == FIRENDLY and item_type != harmful:
        #     do_the_thing
        # else:
        #     error?


    def show_stats(self):
        """ show all actor stats """
        print(f"Actor_id: {self.actor_id}, Name: {self.name.capitalize()}, Stats:\n", self.stat)

    def info(self):
        """ show pretty actor info card """

        print(self.info_str)

    def validate_stats(self):
        """ show missing actor stats """

        val_count = 0 # counter
        stats = tuple(self.stat) # snapshot current stats
        for stat in self.valid_stats:
            if not stats.count(stat): # check snapshot
                print(self.name.capitalize(),
                    f"(actor_id: {self.actor_id})",
                    f"does not have stat '{stat}'.")
                continue
            val_count += 1 # increment counter
        print(f"Validated {val_count} of {len(self.valid_stats)} "+
              f"stats exist for actor_id: {self.actor_id}")

    def get_stat(self, key): # type(key) must be str
        """ get a single stat """

        if not isinstance(key, str):
            print(f"Stat keys must be a string: {key}")
            return False
        stats = tuple(self.stat)
        if not stats.count(key): # does key exist?
            print(f"get_stat ERROR: Actor '{self.name}' had no stat key '{key}'.")
            return False
        return self.stat[key]

    def set_stat(self, key = None, value = None):
        """ get or set a single stat """

        if not isinstance(value, int) or not isinstance(key, str):
            print(f"{key}:{value} must be of type str:int.")
            return
        old_value = self.get_stat(key) # false if key does not exist
        if old_value is False: # check if false
            self.stat[key] = None # create key
        print(f"'{self.name}' '{key}' was: {self.stat[key]}") # old
        self.stat[key] = value # set the key
        print(f"'{self.name}' '{key}' now: {self.stat[key]}") # new
        return

    def __str__(self):
        return f"Actor name: {self.name}, actor_id: {self.actor_id}"
