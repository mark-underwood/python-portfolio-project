""" actor """

class Actor(): # superclass
    """ generic actor template """
    def __init__(self, name, stat):
        # hp_max, ap_max, mp_max, sp_max):
        self.target = None
        self.name = name
        self.stat = stat
        self.stat['hp'] = stat['hp_max'] # health
        self.stat['ap'] = stat['ap_max'] # action
        self.stat['mp'] = stat['mp_max'] # mana
        self.stat['sp'] = stat['sp_max'] # stamina
        self.stat['damage_dealt'] = 0
        self.stats_str = (
            f"  HEALTH: {self.stat['hp']} / {self.stat['hp_max']}\n"
            f"  ACTION: {self.stat['ap']} / {self.stat['ap_max']}\n"
            f"    MANA: {self.stat['mp']} / {self.stat['mp_max']}\n"
            f" STAMINA: {self.stat['sp']} / {self.stat['sp_max']}\n"
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
