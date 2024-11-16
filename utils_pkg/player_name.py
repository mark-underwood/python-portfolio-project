""" set player name """

def player_name():
    """ set player name """
    old_name = 'You'
    min_length = 2
    max_length = 16

    while True:
        print("What is your name?\n")
        new_name = input('Type name: ')

        if new_name == '' or new_name.lower() == old_name.lower(): # is_blank default
            print('\nYou do not know your name.\n')
            return 'You'
        if len(new_name) > max_length: # max len
            print(f"Name must not be more than {max_length} characters.")
            continue
        if len(new_name) < min_length: # min len
            print(f'Name should be at least {min_length} characters.')
            continue
        if not new_name.isalpha(): # alpha check
            print('Enter only letters.')
            continue
        print(f'\nYou are (?) {new_name}.\n')
        return new_name
