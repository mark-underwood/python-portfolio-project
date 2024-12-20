""" set player name """

def player_name():
    """ set player name """
    old_name = 'You'
    min_length = 2
    max_length = 16

    while True:
        print("What is your name?\n")
        new_name = input('Type name: ')

        if (new_name == '' or # keep old name if blank
            new_name.isalpha() and # skip following if not alpha
            (
                new_name in (
                'me', 'myself', 'i') or # accept any self pronoun
                new_name.lower() == old_name.lower() # accept old name
            )):
            print('\nYou do not know your name.\n')
            return 'You'
        if len(new_name) > max_length: # max len # 1st priority
            print(f"Name must not be more than {max_length} characters.")
            continue
        if len(new_name) < min_length: # min len # 2nd priority
            print(f'Name should be at least {min_length} characters.')
            continue
        if not new_name.isalpha(): # alpha check # 3rd priority
            print('Enter only letters.')
            continue
        print(f'\nYou are (?) {new_name}.\n')
        return new_name
