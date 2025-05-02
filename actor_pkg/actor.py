"""Generic actor superclass."""

import threading
import weakref
from actor_pkg.defaults import valid_stats
# from utils_pkg.linked_list import Stack # inventory
# from utils_pkg.linked_list import Queue # many-target queue

class Actor(): # superclass
    """generic actor template"""

    # # solution to removing objects from lists:
    # https://stackoverflow.com/a/37233282
    instances = []
    r_lock = threading.RLock()

    @classmethod
    def _cleanup_ref(cls, ref):
        with cls.r_lock:
            try:
                cls.instances.remove(ref)
            except ValueError:
                pass

    def __init__(self, name, stat, debug = False):
        # stat = {"hp_max":100, "mp_max":100, "sp_max":100}):

        # # solution to removing objects from lists:
        # https://stackoverflow.com/a/37233282
        with self.r_lock:
            self.instances.append(weakref.ref(self, self._cleanup_ref))

        self.target = None # set_target()
        self.actor_id = None # set in subclass
        self.name = name

        # add stats to validate here:
        self.valid_stats = valid_stats()
        # start stat setup
        self.stat = stat
        self.stat["is_player_faction"] = True # friendly by default
        self.stat['hp'] = stat['hp_max'] # health
        self.stat['ap'] = 0 # action ; start not ready
        self.stat['ap_max'] = 100 # action ; start not ready
        self.stat['mp'] = stat['mp_max'] # mana
        self.stat['sp'] = stat['sp_max'] # stamina
        self.stat['damage_dealt'] = 0
        # end of init stat updates

        self.debug = debug

        self.info_str = ( # set info string
            f"CURRENT TARGET OF '{self.name.capitalize()}' IS: {self.target}\n"
            f"  HEALTH: {self.stat['hp']} / {self.stat['hp_max']} HP\n"
            f"  ACTION: {self.stat['ap']} / {self.stat['ap_max']} AP\n"
            f"    MANA: {self.stat['mp']} / {self.stat['mp_max']} MP\n"
            f" STAMINA: {self.stat['sp']} / {self.stat['sp_max']} SP\n"
        )

    def set_target(self, target = None): # no target disengages
        """set focus target"""

        # need target and datatype validation
        old_target = self.target
        self.target = target
        if target is None:
            print(f"{self.name.capitalize()} stopped targeting {old_target}.")
        elif self.target is target:
            print(f"{self.name.capitalize()} changed target to {target}.")
        else:
            print(f"ERROR: '{self.name}' actor # {self.actor_id} failed to change target.")

    def print_target(self):
        """print current target"""

        print(f"{self.name.capitalize()} is targeting {self.target}.")

    def use_weapon(self): # attack queue based on action points budget?
        """attack target with weapon"""

        if self.target is None:
            print(f"{self.name.capitalize()} is not targeting anything.")
            return
        if self.target.stat["is_friendly"] and self.target.name is not self.name:
            print(f"{self.target.name.capitalize()} will remember this betrayal.")
            self.target.stat["is_friendly"] = False
        print("weapon_attack stub:", self.target)

    def use_item(self, target = None):
        """use an item"""

        print("use_item stub:", target)
        # if target == None:
        #     target == self.name (need actor id)
        # if target == FIRENDLY and item_type != harmful:
        #     do_the_thing
        # else:
        #     error?

    def show_stats(self):
        """show all actor stats"""
        print(f"Actor_id: {self.actor_id}, Name: {self.name.capitalize()}, Stats:\n", self.stat)

    def info(self):
        """show pretty actor info card"""

        print(self.info_str)

    def validate_stats(self): # keyword-only for consistency
        """check that all valid stat keys exist"""

        val_count = 0 # valid stat counter
        miss_count = 0 # missing stat counter
        miss_list = []
        stats = tuple(self.stat) # snapshot current stats
        for stat in self.valid_stats: # for each valid stat
            if not stats.count(stat): # does it not exist in stat?
                if self.debug:
                    print(self.name.capitalize(),
                    f"(actor_id: {self.actor_id})",
                    f"does not have stat '{stat}'.")
                miss_count += 1
                miss_list.append(stat)
                continue
            val_count += 1 # increment counter
        if self.debug:
            print(f"Actor # {self.actor_id}: {val_count} of {len(self.valid_stats)} valid stats.")
        if val_count is len(self.valid_stats):
            return True
        if self.debug:
            print(f"Missing stats: {miss_list}")
        return False

    def invalidate_stats(self, *, stats = None, prune = True): # keyword-only
        """check for extraneous stat keys"""

        extra_count = 0 # extraneous count
        extra_list = []
        if stats is None and isinstance(self.stat, dict): # test current stats?
            stats_snap = tuple(self.stat) # snapshot current stats
        else:
            stats_snap = stats
        for i in stats_snap:
            if not self.valid_stats.count(i): # is stat valid?
                extra_count += 1
                extra_list.append(i)
                if prune and stats is None: # only works for current stats
                    del self.stat[i] # remove bespoke invalid key
                    if self.debug and not tuple(self.stat).count(i):
                        print(f"Extra stat '{i}' DELETED.")
                if prune and stats is not None:
                    del stats[i] # remove bespoke invalid key
                    if self.debug and not tuple(stats).count(i):
                        print(f"Extra stat '{i}' DELETED.")

        if self.debug:
            print(f"Actor # {self.actor_id}: {extra_count} extra, {len(self.stat)} total stats.")
        if extra_count:
            if self.debug:
                print(f"Extraneous stats: {extra_list}")
            return False # no-prune extra stats
        return True # no extra stats

    def check_stats(self, *, prune = False): # keyword-only
        """valid and invalid stat key check"""

        # first pass
        if (self.validate_stats() and
            self.invalidate_stats(prune = prune)):
            if self.debug:
                print('Checks passed.')
            return True

        # second pass checks if prune succeeded if applicable
        if self.invalidate_stats(prune = False):
            print('Prune successful. Checks passed.')
            return True

        if self.debug:
            print('One or more checks did not succeed.')
        return False

    def get_stat(self, key): # type(key) must be str
        """get a single stat"""

        if not isinstance(key, str):
            print(f"Stat keys must be a string: {key}")
            return False
        stats = tuple(self.stat)
        if not stats.count(key): # does key exist?
            print(f"get_stat ERROR: Actor '{self.name}' had no stat key '{key}'.")
            return False
        return self.stat[key]

    def set_stat(self, key = None, value = None):
        """get or set a single stat"""

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
