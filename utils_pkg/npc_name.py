""" npc name """

def check_name(name, debug):
    """ sanity check npc name string """

    limit = (2, 16) # character

    if (
        isinstance(name, str) and # is str
        (limit[0] <= len(name) <= limit[1]) # is within limits
        ):

        num_invalid = 0
        num_spaces = 0

        for c in name: # c = characters
            if not (c == ' ' or c.isalpha()): # spaces or abc
                num_invalid += 1
            if c == ' ': # count spaces
                num_spaces += 1
        if debug:
            print(f"Name '{name}' has:\n{num_spaces} space(s)"+
                  f"\n{num_invalid} invalid characters.")

        if (not num_invalid and # all valid characters
            name[0] != ' ' and # space not at start
            name[-1] != ' ' and # space not at end
            num_spaces <= 1 # max 1 spaces
            ): # valid if zero
            return name # name acceptable
    if debug:
        print(f"Name '{name}' is not an alphabetic string.")
    return "Unknown" # name rejected
