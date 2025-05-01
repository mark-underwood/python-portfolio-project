"""Return default values as objects."""

def valid_stats():
    """Central location for valid stats."""

    return ("hp", "hp_max", "ap", "ap_max",
            "mp", "mp_max", "sp", "sp_max",
            "is_player_faction", 'damage_dealt')

def human_stats():
    """Default stat values for humans."""

    return {
                'hp_max': 100, # health
                'ap_max': 100, # action
                'mp_max': 100, # mana
                'sp_max': 100 ## stamina
            }
